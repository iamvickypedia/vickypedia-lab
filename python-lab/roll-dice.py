from random import randint

def get_res():
	return randint(1,6)
	
input("Welcome to the Roll Dice Program.\nPress ENTER to roll the dice and see the result")

print("\n\n"+str(get_res())+ "\n\n")