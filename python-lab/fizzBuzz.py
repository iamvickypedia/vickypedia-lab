"""
A short program that prints each number from 1 to 100 on a new line. 

For each multiple of 3, print "Fizz" instead of the number. 

For each multiple of 5, print "Buzz" instead of the number. 

For numbers which are multiples of both 3 and 5, print "FizzBuzz" instead of the number.

"""
def fizzBuzz(lim):
    for i in range(1,lim+1):
        f="Fizz"
        b="Buzz"
        x=i%3==0
        y=i%5==0
        u=f+b if x and y else f if x else b if y else i
        print(u)

if __name__ == "__main__":
    try:
        lim = int(input("Enter the Limit for FizzBuzz\t"))
    except Exception as ex:
        print(ex)
    else:
        fizzBuzz(lim)