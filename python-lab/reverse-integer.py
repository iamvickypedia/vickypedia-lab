def reverse_int(inp):
	"""
	This is a program which takes an intreger and reverses the number by having some calculation based operation.
	We can also easily reverse a number by converting it to string and returning the reversed string which you can convert to number again.
	But this is an approach circumventing that hack.
	"""
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
	
