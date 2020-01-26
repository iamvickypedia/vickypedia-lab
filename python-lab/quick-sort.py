# This program will take array as input and return sorted array
from random import randint

def quick_sort(arr):
    if len(arr) <= 1:
        return arr
    else:
        pivot = arr.pop()
        left = []
        right = []
        arrLength = len(arr)

        for a_arr in arr:
            if a_arr <= pivot:
                left.append(a_arr)
            else:
                right.append(a_arr)
        return quick_sort(left) + [pivot] + quick_sort(right)


def manually():
    try:
        limit = int(input("Enter the limit of the Array\n"))
    except:
        return print("Wrong Entry")
    else:
        arr = []
        for i in range(limit):
            ind = input("Enter array element\n")
            arr.append(int(ind))

        print('Final Array {}'.format(arr))
        print(quick_sort(arr))
def randomly():
    arr = [randint(0,9) for i in range(10)]
    print(arr)
    print(quick_sort(arr))

choice = input('1. Enter the array Elements manually\n2. Randomly generate an array and sort it\n')
choices = {1:manually,2:randomly}
choice = choice if choice else 2
c = choices.get(int(choice),"Wrong input")()

