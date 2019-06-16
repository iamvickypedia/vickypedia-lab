def reverse_int(inp):
	newnum = 0
	if inp.isdigit():
		digits = len(inp) - 1
		inp = int(inp)
		while (inp > 0):
			count = inp % 10
			newnum = newnum * 10 + count
			inp = inp // 10
			
	return newnum

if '__main__' == __name__:
	num = input("Enter the Number to get the reverse \n")
	print(reverse_int(num))
	
