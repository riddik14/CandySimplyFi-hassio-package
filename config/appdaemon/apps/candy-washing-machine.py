# based on https://github.com/jezcooke/haier_appdaemon/blob/main/checkappliance.py
import hassapi as hass
import requests
import json
import codecs
from datetime import datetime, timedelta, timezone

appliance_entity = "sensor.candy_wifi" # The name of the entity to use/create in Home Assistant (the stats use the same value with '_stats' appended)
status_root = "statusLavatrice"             # The root level JSON element returned by 'http-read'
power_attribute = "MachMd"                  # The name of the JSON attribute that containes the power on/off state.
stats_root = "statusCounters"               # The root level JSON element returned by 'http-getStatistics'
polling_interval = 10                       # How frequently check for the latest status.
request_timeout =  20                        # Request timeout should be less than the polling interval to prevent threads backing up from failing requests.

max_retry_before_unavailable = 3


class CandyWashingMachine(hass.Hass):
    def initialize(self):
        self.retry = 0
        self.previous_end = None
        self.run_every(self.check_appliance, "now", polling_interval)
        self.encryption_key = self.args["encryption_key"]
        self.log(f"encryption_key: {self.encryption_key!r}")
        self.appliance_host = self.args["appliance_host"]

    def check_appliance(self, kwargs):
        try:
            status = self.get_status()
            power = int(status[status_root][power_attribute])
            if power > 5:
                state = "Finito"
            elif power == 1:
                state = "Ferma"
            elif power == 2:
                state = "In lavaggio"
            elif power == 3:
                state = "In Pausa"
            elif power == 5:
                state = "Partenza ritardata"
            else:
                state = "Sconosciuto"
            attributes = status[status_root]
            self.set_state(appliance_entity, state=state, attributes=attributes)
            self.retry = 0
            remaining_minutes = int(attributes["RemTime"]) // 60 + int(attributes["DelVal"])
            now_rounded = datetime.now(timezone.utc).replace(second=0, microsecond=0) + timedelta(minutes=1)
            end = now_rounded + timedelta(minutes=remaining_minutes)
            # If there is less than 1 minutes differences between the previous and the current calculated end times,
            # we keep the one farther in the future
            # This avoid alternating between two values
            if self.previous_end is not None:
                if abs(end - self.previous_end) <= timedelta(minutes=1):
                    end = max(end, self.previous_end)
            self.previous_end = end
            entity_id = appliance_entity + "_program_end"
            self.set_state(
                entity_id,
                state=end.isoformat(),
                attributes={
                    "device_class": "timestamp",
                    "remaining_minutes": remaining_minutes,
                },
            )
        except Exception as e:
            self.log(f"error when getting status: {e}")
            self.retry += 1
            if self.retry > max_retry_before_unavailable:
                self.set_state(appliance_entity, state="unavailable")
                entity_id = appliance_entity + "_program_end"
                self.set_state(
                    entity_id,
                    state="unavailable",
                    attributes={"device_class": "timestamp"},
                )
                previous_end = None
            return

        try:
            entity_id = appliance_entity + "_stats"
            stats = self.get_stats()[stats_root]
            total = 0
            for (key, value) in stats.items():
                if key.startswith("PrCode"):
                    total += int(value)
            self.set_state(entity_id, state=total, attributes=stats)
        except:
            pass

    def get_status(self):
        return self.get_data("read")

    def get_stats(self):
        self.get_data("prepareStatistics")
        return self.get_data("getStatistics")

    def get_data(self, command):
        res = requests.get(
            "http://" + self.appliance_host + "/http-" + command + ".json?encrypted=1",
            timeout=request_timeout,
        )
        return json.loads(self.decrypt(codecs.decode(res.text, "hex"), self.encryption_key))

    def decrypt(self, cipher_text, key):
        decrypted = ""

        for i in range(len(cipher_text)):
            decrypted += chr(cipher_text[i] ^ ord(key[i % len(key)]))

        return decrypted
