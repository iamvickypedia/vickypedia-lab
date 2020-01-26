# This program takes the limit as parameter and returns fibonacci number
import sys,time
memoization = {}
memoization_activated = True
total_recur = 0


def with_memoization(n):
    """
    In computing, memoization or memoisation is an optimization technique used 
    primarily to speed up computer programs by storing the results of expensive function calls 
    and returning the cached result when the same inputs occur again.
    Eg : Fibonacci(35) takes 8-9 seconds and increases exponentially in processing time without memoization,
    but without memoization every request is completed within a second
    """
    if n in memoization.keys():
         return memoization[n]
    else:
         memoization[n] = Fibonacci(n-1) + Fibonacci(n-2)
         return memoization[n]

def without_memoization(n):
    return Fibonacci(n-1) + Fibonacci(n-2)

def Fibonacci(n):
    global total_recur

    total_recur += 1
    if n<0:
        pass
    elif n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        if memoization_activated:
            return with_memoization(n)
        else:
            return without_memoization(n)


fib_no = input("Enter Limit\n")
start = time.time()
try:
    print("\n\nAnswer -------> "+str(Fibonacci(int(fib_no)))+"\n\n")
except:
    print("\n\n-------!!!!Maximum Recursion Occured!!!!-------\n\n")

print("Memoization Activated : ",memoization_activated)
print("Total milliseconds used: ",time.time() - start)
print("\nTotal Recursion occured :",total_recur)
print("Maximum Recursion Supported by System : ",sys.getrecursionlimit()) #https://stackoverflow.com/questions/3323001/what-is-the-maximum-recursion-depth-in-python-and-how-to-increase-it
