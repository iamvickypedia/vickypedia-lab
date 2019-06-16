import time,os,sys,math,random,pdb

def startm(sent,delay):
    #pdb.set_trace()
    start=len(sent)
    for i in range(1,delay*10):
        print(sent[:start-i],end='\r')


sent='Enter the number of seconds you want to see the loader'
print('See the magic')
startm(sent,50)
