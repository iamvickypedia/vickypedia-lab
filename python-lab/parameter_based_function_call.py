# Since there is not a native switch case in python there is a way to do this (without using the if Statement)

switcher = {
        1:'First',
        2:'Second',
        3:'Third',
        4:'Fourth'
        }

print("We create a dictionary with case names as key and the value as potential functions.")

getter = input('Input a key from 1 to 4\n')
print(switcher.get(int(getter),'Not Available\n'))
