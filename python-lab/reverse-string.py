# This program would contain a function which contains the string as a parameter and then returns the reversed string 

def reverse_string(str):
    temp_str = ""
    for chr in str:
        temp_str = chr + temp_str

    return temp_str

string_l = 'Lorem ipsum dolor sit amet'
print(string_l)
print(reverse_string(string_l))

