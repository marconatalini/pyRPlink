'''
Created on 17 mar 2019

@author: Marco
'''

from Codici import CODICI
from Registrazione import REGISTRAZIONE
from Timbrature import TIMBRATURE
from Config import CONFIG
import shutil
import os
import datetime
from time import strftime, localtime

# Exception raised when an error or invalid response is received
class Error(Exception): pass
class stop_error(Error): pass        

def main():

    print("""
#################################################
##                                             ##
## pyRPlink v0.1 by Marco Natalini 03/2019     ##
##                                             ##
#################################################
    
    """)
    
    print("Carico configurazione...", end=' ')
    ini = CONFIG()
    print("OK")
    print("Carico i codici dipendente...", end=' ')
    dipendenti = CODICI(ini.getFileDipendenti()) 
    print("OK")
    print("    Caricato {} dipendenti.".format(len(dipendenti.getCodici())))
    print("    Ultimo dipendente: {} {}".format(dipendenti.getLastNomeDipendente(),dipendenti.getCodici()[-1].rfidCode))
    
    fileTransactionsPath = 'TRANSACTIONS.TXT'
    try:
        filesecs = os.path.getmtime(fileTransactionsPath)
        fileLenght = os.path.getsize(fileTransactionsPath)
        if filesecs and fileLenght:
            dataFile = strftime('%d.%m.%Y %H:%M', localtime(filesecs))
            print("Le timbrature del {} non sono ancora state importate tutte.".format(dataFile))
            raise stop_error
    except FileNotFoundError:
        os.remove(fileTransactionsPath)
        pass
    
    print("Controllo timbrature...")
    for ip in ['192.168.29.212','192.168.29.213','192.168.39.212']:
        transactions = TIMBRATURE(ip, fileTransactionsPath)
    
    registrazioni = []
    errori = []
    
    logPath = "log"
    
    try:
        ftr = open(fileTransactionsPath, "r")
        
        for line in ftr:
            timbratura = REGISTRAZIONE(line)
            dipendente = dipendenti.findDipendenteByRfid(timbratura.getCode())
            if dipendente:
                registrazioni.append(timbratura.getConvertedString(dipendente.getAScode()))
            else:
                errori.append(line)
                
        ftr.close()
    
    
        print("Creo il file da importare...", end=' ')
        timbPath = "TIMBRATURE.TXT"
        timbrature = open(timbPath, "w")
        print("OK")
    
        if len(errori):
            print("Il file dipendenti non era completo. Completalo e riprova.", end=' ')
        else:
            print("Converto i codici dipendente e scrivo il file da importare...", end=' ')
            timbrature.write("\n".join(registrazioni))
            timbrature.close()
            shutil.move(fileTransactionsPath, os.path.join(logPath,"{}.txt".format(str(datetime.datetime.utcnow()).replace(':',''))))
            print("OK")
            print("File TIMBRATURE.TXT pronto da importare.")
    except OSError:
        print("Nessuna nuova timbratura scaricata.")
        
    raise stop_error

if __name__ == '__main__':
    try:
        main()
    except stop_error:
        input("FINITO.\n\nPremi INVO per uscire")