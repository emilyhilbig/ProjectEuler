number =  600851475143
counter = 3
upperbound = number

def isPrime(checkthis):
	isprime = True
	divisor = checkthis
	while (divisor > 2) and isprime:
		divisor = divisor - 1
		if checkthis % divisor == 0:
			isprime = False
	return isprime

def isFactor(brotentialfactor):
	if number % brotentialfactor == 0 :
		return True
	else:
		return False

largestprime = 0
while counter <= (upperbound):
	print counter
	if isFactor(counter):
		if isPrime(counter):
			largestprime = counter
			upperbound = upperbound / counter

	counter = counter + 2

print largestprime


