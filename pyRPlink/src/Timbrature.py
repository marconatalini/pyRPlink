'''
Created on 20 mar 2019

@author: Marco
'''

from ftplib import FTP
import os

class Timbrature(object):
    "Classe per lo scarico delle trimbrature"
    
    def __init__(self, ip, fileTransactionsPath):
        
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
        except :
            print("Nessuna nuova timbratura trovata")
            
    def getFileTransactionsPath(self):
        return fileTransactionsPath