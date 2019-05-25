import time, sys, os, math, random

text = input("Enter Text\n")

v = chr(random.randint(65,90))
s = 5*10

def get_shuffled_txt(text,se):
	temp = ""
	for a_text in text:
		if a_text.isalpha():
			temp += chr(random.randint(65,90))
		else:
			temp += a_text

	if se == s-1:
		return text.upper()
	else:
		return temp

os.system('setterm -cursor off')
for i in range(s):
	sys.stdout.write("\r"+get_shuffled_txt(text,i))
	sys.stdout.flush()
	time.sleep(0.1)

sys.stdout.write('\n')
sys.stdout.flush()
os.system('setterm -cursor on')