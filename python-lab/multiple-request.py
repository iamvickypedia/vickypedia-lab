import requests
from threading import Thread

def run_local(nthreads):
	url = "http://localhost:8000/api/works/test_multiple/"
	print("Calling no "+str(nthreads))
	body = {"id":nthreads}
	r = requests.post(url,body).json()
	print(r)

def run_threads(nthreads):
	url = 'https://api.codezen.in/api/careers/all_openings/'
	store = {}
	print("Calling no "+str(nthreads))
	# for i in range(nthreads):
	store[nthreads] = requests.get(url).json()
	print(store.get(nthreads).get("message")[0].get('position'))

import time

def single_thread(n):
	print("Thread "+str(n)+" sleeping")
	time.sleep(3)
	print("Thread "+str(n)+" woken up")

def test_thread(n):
	t = Thread(name="Thread no "+str(n),target=run_local,args=(n,))
	t.start()

if __name__ == '__main__':
	for i in range(150):
		test_thread(i)