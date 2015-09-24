import math
# get all prime factors
#                2 3 5 7 11 13 17 19
primefactors =  [0,0,0,0, 0, 0, 0, 0]
primesbetween = [2,3,5,7,11,13,17,19]
smallestmultiple = 1

def getPrimeFactors(n):
	for x in range( 0 , len(primesbetween)):
		powercounter = 0
		while(n % primesbetween[x] == 0 ):
			n = n / primesbetween [x]
			powercounter += 1
		if primefactors[x] < powercounter:
			primefactors[x] = powercounter

for x in range( 2 , 21 ):
	getPrimeFactors(x)

for x in range( 0 , len(primesbetween) ):
	print "{} to the power of {}".format(primesbetween[x], primefactors[x])
	smallestmultiple = smallestmultiple * math.pow(primesbetween[x], primefactors[x]);

print smallestmultiple;