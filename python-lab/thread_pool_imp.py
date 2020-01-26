from threading import Thread
from time import sleep
from multiprocessing.dummy import Pool as ThreadPool
import random 
def working(n,ind=0):
    ind += 1
    print('worker {} sleeping for {:.2f} secs'.format(ind,n))
    sleep(n)
    print('worker {} Woke up'.format(ind))

sleeping_time = 5
no_of_workers = 50
pool = ThreadPool(sleeping_time)
pool.map(working,[5]*no_of_workers)
pool.close()
pool.join()
for i in range(no_of_workers):
    #sleeping_time_w = sleeping_time*random.random()
    sleeping_time_w = sleeping_time
    th = Thread(target=working,args=(i,sleeping_time_w,))
    #working(i,sleeping_time)
    #th.start()
