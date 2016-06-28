try:
    hrs = raw_input("Enter Hours:")
    h = float(hrs)
    rate = raw_input("Enter Hourly Rate:")
    r = float(rate)
except:
    print "Error, please enter numeric input"
ovr = r * 1.5
if h > 40 :
    oh = h - 40
    h = 40
    p = (h * r) + (oh * ovr)
    print p
else :
    p = h * r
    print p