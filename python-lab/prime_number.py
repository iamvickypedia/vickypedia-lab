#This is an optimised function to check for prime number using 6k + i concept
# we also print the milliseconds required to run this program
import time

def checkPrime(n) :
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


in_number = input("Enter Number to check Prime\n")
st = time.time()
is_prime = checkPrime(int(in_number))
print('Time taken to run is {}'.format(time.time() - st))
if (is_prime) :
    print("{} is a Prime Number".format(in_number))
else :
    print("{} is not a Prime Number".format(in_number))