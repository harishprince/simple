def my_range(first=0, num=10, step=1):
	current_range = first
	count = 0
	while count < 10:
		yield current_range
		current_range += step
		count +=1
		for i in my_range():
			print i