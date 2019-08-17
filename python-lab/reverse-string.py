def reverse_string(str):
    """
    This is a program which takes a string and reverses the string by having for loop based operation.
    """
    temp_str = ""
    for chr in str:
        temp_str = chr + temp_str

    return temp_str

string_l = input("Enter the string to reverse\n")
print(reverse_string(string_l))