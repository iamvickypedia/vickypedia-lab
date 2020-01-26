from random import randint
import time
def get_res():
	return randint(1,6)
	
#input("Welcome to the Roll Dice Program.\nPress ENTER to roll the dice and see the result")
print("Rolling...")
time.sleep(0.5)
print("\n\n"+str(get_res())+ "\n\n")
