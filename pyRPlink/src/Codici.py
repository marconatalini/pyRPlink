'''
Created on 16 mar 2019

@author: Marco
'''

import xlrd
from Dipendente import Dipendente


class Codici(object):
    '''
    Class con l'elenco dei dipendenti e codici letti dal file XLS
    3 colonne: rfid | codice | nome
    '''

    def __init__(self, filepath):
        '''
        Constructor
        '''
        self.codici = []
        
        workbook = xlrd.open_workbook(filepath)
        sh = workbook.sheet_by_index(0)
        for row in range(sh.nrows):
            rfid = sh.cell_value(row, 0)
            code = sh.cell_value(row, 1)
            nome = sh.cell_value(row, 2)
            if rfid:
                newDip = Dipendente(str(int(rfid)), code, nome)
                self.codici.append(newDip)
                
    def getCodici(self):
        return self.codici
    
    def getLastNomeDipendente(self):
        return self.codici[-1].nome
    
    def findDipendenteByRfid(self, rfid):
        for dip in self.codici:
            if dip.rfidCode == rfid:
                return dip
        print("Cod: {} non trovato.".format(rfid))
        return False