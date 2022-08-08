# CandySimplyFi hassio package 


based on https://github.com/jezcooke/haier_appdaemon/blob/main/checkappliance.py

prima di installare il pacchetto accertati che la tua lavatrice abbia un ip statico assegnato dal router,
se non hai la chiave criptata segui qui https://github.com/MelvinGr/CandySimplyFi-tool

###################################################
#installazione

aggiungi al tuo file apps.yaml il contenuto del pacchetto
compila i campi indirizzo ip e key

riavvia appdaemon
###############
aggiungi il package nella tua cartella package e ricarica 

sia entita modello che automazioni

troverai tra le tue entità il sensore sensor.candy_wifi con tutti gli attributi
dopo il caricamento dei template troverai anche 
##############
sensor.programma_attuale_lavatrice

sensor.temperatura_impostata_lavatrice

sensor.temperatura_attuale_lavatrice

sensor.giri_motore_lavatrice

sensor.lavaggio

sensor.igiene

sensor.antipiega

sensor.buonanotte

sensor.risciaquo

sensor.acquaplus

sensor.opt9   - al momento funzione sconosciuta

sensor.vapore

sensor.livello_sporco

##################

ci sono anche automazioni di esempio ma va configurato il servizio di notifica. 

io ho usato questo https://hassiohelp.eu/2020/11/09/centro-notifiche-3-0-appdaemon/

https://camo.githubusercontent.com/9b2ecad5985da7742d9bca779b2d69cc35c286635c68d44b549fa978869fa2f8/68747470733a2f2f63646e2e6275796d6561636f666665652e636f6d2f627574746f6e732f617269616c2d626c61636b2e706e67
