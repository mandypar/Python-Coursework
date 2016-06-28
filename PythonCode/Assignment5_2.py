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
	if largest is None or numfinal>largest:
	    largest=numfinal
#	    continue
	if smallest is None or numfinal<smallest:
		smallest=numfinal
#		continue
	if numfinal<smallest:
		smallest=numfinal
		
	
print "Maximum is", largest
print "Minimum is", smallest