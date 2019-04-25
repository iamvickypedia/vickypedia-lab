# This program takes the limit as parameter and returns fibonacci number

def Fibonacci(n):
    if n<0:
        pass
    elif n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return Fibonacci(n-1) + Fibonacci(n-2)

fib_no = input("Enter Limit\n")
print(Fibonacci(int(fib_no)))
