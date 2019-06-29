### DEMO: Return statements

def end(n, d):
    """Print the final digits of N in reverse order until D is found.    

    >>> end(34567, 5)
    7
    6
    5
    """
    while n > 0:
        last, n = n % 10, n // 10
        print(last)
        if d == last:
            return None

### FINDING pattern

def find_digit(n, d):
	"""Return True if digit D is found in number N, otherwise False

	>>> find_digit(12345689,7)
	False
	>>> find_digit(12345689,5)
	True
	"""
	while n > 0:
		if n % 10 == d:
			return True
		n = n // 10
	return False

### FINDING pattern with HOFs, more general than just finding a digit

def finder(n, pred):
	"""Return True if digit D is found in number N, otherwise False

	>>> finder(31415926535,lambda d: d==8 or d==7)
	False
	>>> finder(3141592653589,lambda d: d==8 or d==7)
	True
	"""
	while n > 0:
		if pred(n % 10):
			return True
		n = n // 10
	return False

### REVERSE pattern

def reverse(n):
	"""Return a number with the digits of the input number N reversed

	>>> reverse(31415926535897932)
	23979853562951413
	"""
	rev = 0
	while n > 0:
		rev = rev*10 + n % 10
		n = n // 10
	return rev

### MAPPING pattern

def mapper(n, f):
	"""Return a number each digit of N transformed by function F

	>>> mapper(1234111,lambda d: d*2)
	2468222
	>>> mapper(1624690,lambda d: 9-d)
	8375309
	"""
	mapped, place = 0, 0
	while n > 0:
		mapped += f(n % 10)*10**place
		n = n // 10
		place += 1
	return mapped

### ABSTRACTION...GENERALIZING THESE PATTERNS INTO ONE

def process_digit(n, digit_mapper, digit_check, digit_retval):
	"""Process every digit of number N through DIGIT_CHECK, 
	which if True calls DIGIT_RETVAL. Otherwise, each digit
	passes through DIGIT_MAPPER which keeps track of the output
	fragment so far and updates the the mapped return value

	>>> new_finder = lambda n,pred: process_digit(n, \
	lambda mapped,place,d: False, \
	lambda d: pred(d), \
	lambda mapped,place,d: True)
	>>> new_finder(31415926535,lambda d: d==8 or d==7)
	False
	>>> new_finder(3141592653589,lambda d: d==8 or d==7)
	True

	>>> new_reverse = lambda n: process_digit(n, \
	lambda mapped,place,d: mapped*10+d, \
	lambda d: False, \
	lambda mapped,place,d: None)
	>>> new_reverse(31415926535897932)
	23979853562951413

	>>> new_mapper = lambda n,f: process_digit(n, \
	lambda mapped,place,d: mapped+f(d)*10**place, \
	lambda d: False, \
	lambda mapped,place,d: None)
	>>> new_mapper(1234111,lambda d: d*2)
	2468222
	>>> new_mapper(1624690,lambda d: 9-d)
	8375309
	"""	
	mapped, place = 0, 0
	while n > 0:
		d = n%10
		if digit_check(d):
			return(digit_retval(mapped,place,d))
		mapped = digit_mapper(mapped,place,d)
		n = n // 10
		place += 1
	return mapped
