# CandySimplyFi hassio appdaemon + automations 


based on https://github.com/jezcooke/haier_appdaemon/blob/main/checkappliance.py

prima di installare il pacchetto accertati che la tua lavatrice abbia un ip statico assegnato dal router,
se non hai la chiave criptata segui qui https://github.com/MelvinGr/CandySimplyFi-tool

oppure

vai a questo link sostituendo l'ip statico della lavatrice
http://192.168.1.127/http-read.json?encrypted=1
copia il risultato che è tipo 

1977636167343C553F0F343E0E27381910130A0D677D333941734E5038381F04310E081C30346A0E694B655E625B5064403F1B1A677D6A0469564A7866587B2003190125216572167A586B7F6558504F32084B5267766A1846704E7B4D012B3D0A58534A7565643941734E503F231A02061F4B526776701667774D7B66730A21070C0C04677D6A0569564A7866587B390717194A7F65781667774D7B66730A1D0B143A18677D6A0C69564A7866587B22120E584A7F65781667774D7B6673161D16484B5267776A1846704E7B4D1E29195158534A7565643941734E5020212D5940404B58676B453E4273653D1F256C4F5858594A694A423D425808021B677B57404A4B44484D413D693537065873634F525845654F4E4116040A334A4D6B7B5D405664624C4E6A7B3B0E7E505573694F4E7763614C651B402E1B2A505573694F4E7763614C650C46322E65484D617B416F70606167032D581D1B2B505573694F4E7763614C651A51262E2E1F0A73634F50495D58676B453E427365200A32301D07330D4A7F65781667774D7B6673150C0C1D4B5267776A1846704E7B4D1730010E284B5267776A1846704E7B4D15301E361F1A1C0A296A0E694A655E625B5064403E001B11223B40191F34505573694F4E7763614C650B5C2E192C271F022D0C161F4B5267776A1846704E7B4D05693A40404B58676B453E4273652626067B57404A4B44484D413D692E77204D6B7B5D405664624C4E6A5A3E1701505573694F4E7763614C653D5A293C65484D617B416F7060616732265608587D505F7375606873604A0B332B63694065405E607B416F70606167093C570F587D50597375606873604A28283C67694065424D7D54676B734B29151427522D587D505F7375606873604A04171B52391F365055736F5F51485D4A694A423D4258241A0E232D2140404B58674A423D36774D0F

incolla la tua chiave qui alla riga 9 e premere il tasto play
sotto apparira la tua chiave 
https://www.online-python.com/pm93n5Sqg4

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

<a href="https://www.buymeacoffee.com/T1Pqksy" target="_blank"><img src="https://cdn.buymeacoffee.com/buttons/arial-black.png" alt="Buy Me A Coffee" style="height: 51px !important;width: 217px !important;" ></a>

------------------------------------


Se il progetto ti è piaciuto clicca <a href="https://www.paypal.me/DomenicoCeccarelli">qui</a> per offrirmi un caffè
