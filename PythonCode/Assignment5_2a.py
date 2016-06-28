largest = None
smallest = None
while True:
	num=raw_input('Enter a number:')
	if num == "done": break
	try:
		    	numfinal = int(num)
	except:
		    	print 'Invalid input'
	    		continue
	if numfinal>largest:
	    largest=numfinal
	    continue
	if numfinal is not smallest:
		smallest=numfinal
		continue
	if numfinal<smallest:
		smallest=numfinal
		
	
print "Maximum is", largest
print "Minimum is", smallest