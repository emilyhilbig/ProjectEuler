flag = True
fibval = 0
counter = 0
sum = 0

def fib(n):
	if n == 0 :
		return 0
	elif n == 1:
		return 1
	else:
		temp = fib(n - 1) + fib(n - 2)
		return temp

while flag:
	fibval = fib(counter)

	if fibval > 4000000:
			flag = False
	else:
		if fibval % 2 == 0:
			sum += fibval

	counter = counter + 1
	print fibval
	#print counter
print "sum is:"
print sum
