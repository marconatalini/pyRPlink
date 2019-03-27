'''
Created on 15 mar 2019

@author: Marco
'''

import re

class REGISTRAZIONE(object):
    '''
    Classe definizione registrazione del rilevatore presenze
    '''

    def __init__(self, txtline):
        '''
        Constructor: dalla stringa del rilevatore ricava tutti i parametri
        012345678901234567890123456
        01  0000171 27/05/17 0648 0
        00  CCCCCCC DD/MM/YY hhmm V
        
        0 = ingresso, 1 = uscita
        '''
        self.txtline = txtline
        
        if len(self.txtline):
            match = re.match("^00  00(?P<rfidCode>\d{5}) (?P<timestamp>\d{2}\/\d{2}\/\d{2} \d{2}\d{2}) (?P<inOut>[01])$", txtline)
            if match:
                self.rfidCode = match.group('rfidCode')
                self.timestamp = match.group('timestamp')
                self.inOut = match.group('inOut')
            else:
                print("Registrazione FALLITA: {}".format(self.txtline))
        
    def getCode(self):
        return self.rfidCode
    
    def getTimestamp(self):
        return self.timestamp
    
    def getInOut(self):
        return self.inOut
    
    def getConvertedString(self, asCode):
        return "00  {:0>7} {} {}".format(asCode, self.timestamp, self.inOut)