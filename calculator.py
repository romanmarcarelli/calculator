def add(x, y):
	return x + y

def mult(x, y):
	return x*y

def div(x, y):
	return float(x)/y

def sub(x, y):
	return x-y

def exp(x):
	return 2.718281828**x

def criticalPoly(a, b):
	return div(-b, 2*a)

def fact(x):
	if x==0: return 1
	else: return x*fact(x-1)
	
def modulo(x, y):
	divided = div(x,y)
	multiply = mult(y, divided)
	return abs((sub(x, multiply)))
