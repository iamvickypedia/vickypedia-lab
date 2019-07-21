#This is an optimised function to check for prime number using 6k + i concept
# we also print the milliseconds required to run this program
import time,sys, os, math

def checkPrime2(n) :
    if (n <= 1) :
        return False
    if (n <= 3) :
        return True

    if (n % 2 == 0 or n % 3 == 0) :
        return False

    i = 5
    while(i * i <= n) :
        if (n % i == 0 or n % (i + 2) == 0) :
            return False
        i = i + 6
    return True

def checkPrime(n) :
    if (n == 1) :
        return False
    if (n == 2) :
        return True
    if n>2 and n%2 == 0 :
        return False

    d = math.floor(math.sqrt(n))
	    
    for i in range(3,d+1,2):
        if n % i == 0 :
            return False
    return True

print("Welcome to the Prime Program\n")
while True:
    choice = input("1. Check if number is Prime \n2. Get i'th Prime number\n3. Exit\nEnter the choice number\n")
    if choice == '1':
        in_number = input("Enter Number to check Prime\n")
        is_prime = checkPrime(int(in_number))
        print("-"*10)
        if (is_prime) :
            print("{} is a Prime Number".format(in_number).center(50,"-"))
        else :
            print("{} is not a Prime Number".format(in_number))
        print("-"*10)

    elif choice == '2':
        in_number = input("Enter the value of i\n")
        in_number = int(in_number)
        counter = 0
        st = time.time()
        candidate = 2
        os.system('setterm -cursor off')
        while True:
            print("Loading {0:.2f}%".format((counter/in_number)*100),end="\r")
            if counter >= in_number:
                break
            if checkPrime(candidate):
                # print("candidate",candidate,"counter",counter)
                counter += 1
            candidate += 1
        os.system('setterm -cursor on')
        print("\n"+"-"*10)
        print("The Prime number at {} place is {}".format(in_number,candidate-1))
        print("-"*10)
        print('Time taken to search the Prime number is {}\n'.format(time.time() - st))
    elif choice == 'dd4ff':
    	start = time.time()
    	for i in range(100000):
    		print(f"{(i/100000)*100:.2f} %",end='\r')
    		checkPrime(i)
    	print(f'time taken is {time.time() - start:.2f}')
    else:
        print("Thank you for your interest")
        break
