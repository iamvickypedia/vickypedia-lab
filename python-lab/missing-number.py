# This program will take an array as input and then return the missing number

def missing_number(arr):
    n = len(arr)
    total = (n+1)*(n+2)/2
    sum_of_A = sum(arr)

    return total - sum_of_A



A = [1,2,3,5,6]

print(missing_number(A))
