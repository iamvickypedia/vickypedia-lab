from string import ascii_lowercase as asc_lower

def check(s):
    res = set(asc_lower) - set(s.lower())

    if res == set([]):
        return True
    else:
        return False

s = input('Enter text to check for pangrams\n')

res = check(s)
if res:
    print('Entered text is a pangram')
else:
    print("entered text isn't a pangram")
