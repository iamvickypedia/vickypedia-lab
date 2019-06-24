import time,os,sys,math,random,pdb

def startm(sent,delay):
    #pdb.set_trace()
    start=len(sent)
    for i in range(1,delay*10):
        if i <= start:
            c= "\r{}{}".format(sent[i:]," "*i)
        elif i > start:
            c="\r{}{}".format(" "*(start-(i%start)),sent[:i%start])
        sys.stdout.write(c)
        sys.stdout.flush()
        time.sleep(0.1)


sent='Enter the number of seconds you want to see the loader'
#print('See the magic')
startm(sent,50)
