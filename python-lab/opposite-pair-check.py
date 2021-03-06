import random

print("This Program checks for the occurence of any pairs whose sum is 0")
choice = input(
    "1. Generate Random array and show result\n2. Enter array elements yourself\n"
)


def check_opp_pair(arr):
    uniq_arr = []
    for i in range(len(arr)):
        if -arr[i] in arr[i:]:
            if abs(arr[i]) not in uniq_arr:
                uniq_arr.append(abs(arr[i]))
    if len(uniq_arr) > 0:
        for a in uniq_arr:
            print("Opposite pair of {} is present".format(a))
    else:
        print("There are no opposite pairs present.")


if choice == "1":
    arr = [random.randint(-9, 9) for _ in range(20)]
    while 0 in arr:
        arr.remove(0)
    print("Original Array {}".format(arr))
    check_opp_pair(arr)
elif choice == "2":
    arr = list(
        map(int, input("Enter space separated Array elements\n").split(" ").remove(" "))
    )
    check_opp_pair(arr)
else:
    print("Wrong Choice")
