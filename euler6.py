import math
number = 100
def getPowerOfSum(n):
	if (n % 2 == 0):
		powerofsum = (n + 1) * (n/2)
	else:
		powerofsum = n*(math.floor(n/2))
	return math.pow(powerofsum, 2)

sumofpowers = 0

for x in range(1, number + 1):
	sumofpowers = sumofpowers + math.pow(x, 2)

print "sumofpowers {}".format(sumofpowers)
print " getPowerOfSum(number) {}".format(getPowerOfSum(number))
print "10 power of sum {}".format(getPowerOfSum(number) - sumofpowers)