from string import ascii_lowercase as ascii_l
import re
from collections import Counter
letters = list(ascii_l)
result = {}
sent = input('Enter the sentence\n')
cleaned_sent = "".join(re.findall('[a-zA-Z]+',sent)).lower()
for a in ascii_l:
    result[a] = cleaned_sent.count(a)
print(result)
total_letters = sum(result.values())
for i in result.keys():
    result[i] = (result[i]*100)/total_letters

def get_final_data(result,pivot='key',rev = False):
    response = []
    if pivot == 'key':
        for i in sorted(result,reverse=rev):
            response.append((i,result[i]))
    else:
        return sorted(result.items(),key= lambda kv:(kv[1],kv[0]),reverse=rev)
    return response
print('Sorting -- please chose from the following')
inp_choice = input('A1 - Sort by letters ascending\nA0 - Sort by letters descending\nB1 - Sort by percentage ascending\nB0 - Sort by percentage descending(default)\n')
if inp_choice == '':
    rev = True
    pivot = 'val'
else:
    if inp_choice == 'A1':
        rev = False
        pivot = 'key'
    elif inp_choice == 'A0':
        rev = True
        pivot = 'key'
    elif inp_choice == 'B1':
        rev = False
        pivot = 'val'
    elif inp_choice == 'B0':
        rev = True
        pivot = 'val'
    else:
        rev = False
        pivot = 'key'

    
result = get_final_data(result,pivot=pivot,rev=rev)

print('----RESULT----')
print('--letter percentages are as follows --')
for k,v in result:
    print(f" {k} : {v :.2f} %")



