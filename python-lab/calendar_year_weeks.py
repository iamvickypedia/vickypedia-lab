import calendar,sys


c = calendar.Calendar()
calendar.setfirstweekday(calendar.SUNDAY)

def get_no_of_weeks(yy,mm):
	return len(calendar.month(yy,mm).split('\n')) -3

def get_data(yy):
        """calendar weeks addition. can be used for salt or token gen purposes"""
	week_count = 0
	data = []
	for i in range(1,13):
		weeks = get_no_of_weeks(yy,i)
		for j in range(weeks):
			data.append("y{}m{:02d}w{:02d}".format(yy,i,week_count))
			week_count += 1
	return data

try:
	yy = int(input("Enter the year\n"))
except:
	print("Wrong Input for Year")
	sys.exit()
else:
	data = get_data(yy)
	print(*data,sep="\n")
