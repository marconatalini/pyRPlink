'''
Created on 17 mar 2019

@author: Marco
'''
from Codici import Codici
from Registrazione import Registrazione
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
timbrature = open("TIMBRATURE.TXT", "w")
print("OK")

print("Carico le timbrature dai terminali...")
registrazioni = []
for line in open("TRANSACTIONS.TXT", "r"):
    timbratura = Registrazione(line)
    dipendente = dipendenti.findDipendenteByRfid(timbratura.getCode())
    if dipendente:
        registrazioni.append(timbratura.getConvertedString(dipendente.getAScode())) 

print("Converto i codici dipendente e scrivo il file da importare...", end=' ')
timbrature.write("\n".join(registrazioni))
print("OK")


if __name__ == '__main__':
    pass