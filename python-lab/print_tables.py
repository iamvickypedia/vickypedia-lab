def print_table(n):
    for i in range(1,11):
        print(n,' * ',i,' = ',i*n)
      
print('Welcome to Tables generator. Tell your teachers the table of any number in a second')
inp = input('Enter the number to generate its table\t')

print_table(int(inp))
