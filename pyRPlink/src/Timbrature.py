'''
Created on 20 mar 2019

@author: Marco
'''

from ftplib import FTP, error_perm
import os
from socket import timeout

class TIMBRATURE(object):
    "Classe per lo scarico delle trimbrature"
    
    def __init__(self, ip, fileTransactionsPath):
        
        try:
            print("Connessione al terminale {}...".format(ip), end=' ')
            ftp = FTP(ip, timeout=2)
            ftp.login('admin', 'admin')
            ftp.rename('TRANSACTIONS.TXT', 'T-TEMP.TXT')
            timbrature = open(fileTransactionsPath, 'ab')
            ftp.retrbinary('RETR T-TEMP.TXT', timbrature.write)
            ftp.delete('T-TEMP.TXT')
            ftp.quit()
            print('OK')
            timbrature.close()
        except timeout:
            print("Connessione fallita. TIMEOUT!")
        except TimeoutError:
            print("Connessione fallita. TIMEOUT!")
        except error_perm as err:
            print("Errore imprevisto :{}".format(err.args[0]))