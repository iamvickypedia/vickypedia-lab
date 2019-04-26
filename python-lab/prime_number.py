#This is an optimised function to check for prime number using 6k + i concept
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
  
  
if (isPrime(11)) : 
    print(" true") 
else : 
    print(" false") 
      
if(isPrime(15)) : 
    print(" true") 
else :  
    print(" false")