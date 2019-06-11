'''
Created on 11 giu 2019

@author: Marco

Utility per convertire btransaction.loc nel file transaction.txt

source:
:00002031201906100550130        0014736000000000000001+00000000     00000174 07           0000
result:
01  0000171 27/05/17 0648 0
'''

import os

def converti(l):
    r = {}
    r['anno'] = l[11:13]
    r['mese'] = l[13:15]
    r['gg']= l[15:17]
    r['ora']= l[17:19]
    r['min']= l[19:21]
    r['eu']= l[23:24]
    r['codice']= l[32:39]
    
    return "00  {codice} {gg}/{mese}/{anno} {ora}{min} {eu}\n".format(**r)

#locFile = open(raw_input('File da convertire: '),'r')

pathbase = r'c:\Users\marco\Downloads'
inputList = os.listdir(pathbase)
resFile = open(os.path.join(pathbase,"TRANSACTIONS.TXT"),'a')

for file in inputList:
    #print(file)
    if file[-3:] == 'loc':
        print(file)
        locFile = open(os.path.join(pathbase,file),'r')
        for line in locFile:
            result = converti(line)
            resFile.write(result)
            #print (result)
     

resFile.close()

