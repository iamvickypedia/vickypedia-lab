def get_row(c_n, n, limi):
    c = chr(c_n)

    right = []

    for i in range(1,n):
        if i < limi:
            right.append(chr(c_n+i))
        else:
            right.append('-')

    left = right[::-1]

    return "-".join(left+[c]+right)

def upper_design(n):
    limi = 1
    for i in range(97,n+97)[::-1]: 
        print(get_row(i,n,limi)) 
        limi += 1

def lower_design(n):
    limi = n - 1
    for i in range(98,n+97): 
        print(get_row(i,n,limi)) 
        limi -= 1

def print_rangoli(size):
    upper_design(size)
    lower_design(size)

if __name__ == '__main__':
    n = int(input("Enter the length of rangoli\n"))
    print_rangoli(n)