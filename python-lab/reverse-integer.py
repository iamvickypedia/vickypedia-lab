def reverse_int(inp):
	newnum = 0
	if type(inp) == int:
		digits = len(str(inp))
		for i in range(1,digits+1):
			count = inp%(10**i)
			inp -= count
			count = count/(10**(i-1))
			# print(count)
			newnum += count*10**(digits - i)
			
	return int(newnum)

if '__main__' == __name__:
	num = input("Enter the Number to get the reverse \n")
	print(reverse_int(int(num)))
	
