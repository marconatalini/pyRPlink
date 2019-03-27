'''
Created on 27 mar 2019

@author: Marco
'''

class CONFIG():
    "Classe con la definizione delle variabili lette dai file di configurazione"
    
    def __init__(self):
        self.ini = {}
        ini = open('config.ini', 'r')
        for line in ini:
            k,v = line.split('=')
            self.ini[k.strip()] = v.strip()
            
    def getIPS(self):
        return self.ini['IP'].split(',')
    
    def getTimeout(self):
        return self.ini['FTPtimeout']
    
    def getFileTimbrature(self):
        return self.ini['fileTimbrature']
    
    def getFileDipendenti(self):
        return self.ini['fileDipendenti']
    