'''
Created on 16 mar 2019

@author: Marco
'''

class Dipendente(object):
    '''
    Class del dipendente
    '''

    def __init__(self, rfidCode, asCode, nome):
        '''
        Constructor
        '''
        self.rfidCode = rfidCode
        self.asCode = asCode
        self.nome = nome
        
    def getAScode(self):
        return self.asCode