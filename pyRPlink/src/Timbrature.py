'''
Created on 20 mar 2019

@author: Marco
'''

from ftplib import FTP
import os
from time import strftime, localtime

fileTransactionsPath = 'TRANSACTIONS.TXT'

class Timbrature(object):
    "Classe per lo scarico delle trimbrature"
    
    def __init__(self, ip):
        
        try:
            filesecs = os.path.getmtime(fileTransactionsPath)
            dataFile = strftime('%d.%m.%Y %H:%M', localtime(filesecs))
            print("Le timbrature del {} non sono ancora state importate tutte.".format(dataFile))
            return None
        except FileNotFoundError:
            pass
    
        try:
            print("Connessione al terminale {}...".format(ip), end=' ')
            ftp = FTP(ip)
            ftp.login('admin', 'admin')
            ftp.rename('TRANSACTIONS.TXT', 'T-TEMP.TXT')
            timbrature = open(fileTransactionsPath, 'ab')
            ftp.retrbinary('RETR T-TEMP.TXT', timbrature.write)
            ftp.delete('T-TEMP.TXT')
            ftp.quit()
            print('OK')
            timbrature.close()
        except TimeoutError:
            print("Connessione fallita. TIMEOUT!")
            
    def getFileTransactionsPath(self):
        return fileTransactionsPath