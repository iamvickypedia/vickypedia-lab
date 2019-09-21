import calendar,sys

c = calendar.Calendar()
calendar.setfirstweekday(calendar.SUNDAY)

def get_no_of_weeks(yy,mm):
	w,_ = calendar.monthrange(yy,mm)
	new_day = True if w == 6 else False
	new_day = True if mm == 1 else new_day
	week_count = len(calendar.month(yy,mm).split('\n')) -3
	return new_day,week_count

def get_data(yy,continuos=False):
	"""calendar weeks addition. can be used for salt or token gen purposes"""
	week_count = 1
	data = []
	for i in range(1,13):
		new_day,weeks = get_no_of_weeks(yy,i)
		if new_day is False and continuos is False:
			week_count -= 1
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
	data = get_data(yy) # add continuos=True if you dont want overlapping weeks check On
	print(*data,sep="\n")