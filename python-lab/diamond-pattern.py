def print_pattern(lim):
    arr = [i for i in range(lim+1)] + [i for i in range(lim)[::-1]]

    for a_arr in arr:
        print((' *'*a_arr).center(lim*2,' '))

lim = int(input('Enter the pattern limit\n'))
print_pattern(lim)

