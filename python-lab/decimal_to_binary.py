def get_binary(num):
    neg = False
    if num < 0:
        num = -num
        neg = True
    binary = []
    while num > 0:
        binary.insert(0,num%2)
        num >>= 1
    if neg:
        return "-0b"+"".join(str(e) for e in binary)
    else:
        return "0b"+"".join(str(e) for e in binary)

try:
    num = int(input('Enter the Decimal Number : \t'))
except:
    raise ValueError('Invalid Input')

print(f"Binary equivalent for the number {num} is {get_binary(num)}")
