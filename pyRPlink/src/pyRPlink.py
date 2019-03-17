'''
Created on 17 mar 2019

@author: Marco
'''

from Codici import Codici
from Registrazione import Registrazione
import shutil
from _datetime import datetime
import os

print("""
############################################################
##
## pyRPlink v0.1 by Marco Natalini 03/2019
##
############################################################

""")

print("Carico i codici dipendente...", end=' ')
dipendenti = Codici('dipendenti.xls') 
print("OK")
print("    Caricato {} dipendenti.".format(len(dipendenti.getCodici())))
print("    Ultimo dipendente: {} {}".format(dipendenti.getLastNomeDipendente(),dipendenti.getCodici()[-1].rfidCode))

print("Creo il file da importare...", end=' ')
timbPath = "TIMBRATURE.TXT"
timbrature = open(timbPath, "w")
print("OK")

print("Carico le timbrature dai terminali...")
registrazioni = []
errori = []
ftpFilepath = "TRANSACTIONS.TXT"
logPath = "log"
ftr = open(ftpFilepath, "r")

for line in ftr:
    timbratura = Registrazione(line)
    dipendente = dipendenti.findDipendenteByRfid(timbratura.getCode())
    if dipendente:
        registrazioni.append(timbratura.getConvertedString(dipendente.getAScode()))
    else:
        errori.append(line)
        
ftr.close()

if len(errori):
    print("Il file dipendenti non era completo. Completalo e riprova.", end=' ')
else:
    print("Converto i codici dipendente e scrivo il file da importare...", end=' ')
    timbrature.write("\n".join(registrazioni))
    timbrature.close()
    shutil.move(ftpFilepath, os.path.join(logPath,"{}.txt".format(str(datetime.utcnow()).replace(':',''))))
    print("OK")



if __name__ == '__main__':
    pass