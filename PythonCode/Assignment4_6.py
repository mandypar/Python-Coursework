def computepay(h,r) :
    if h > 40 :
        oh = h - 40
        h = 40
        ovr = r * 1.5
        p = (h * r) + (oh * ovr)
    else :
        p = h * r
    return p

try:
    hrs = raw_input("Enter Hours:")
    h = float(hrs)
    rate = raw_input("Enter Hourly Rate:")
    r = float(rate)
except:
    print "Error, please enter numeric input"

pay = computepay(h,r)

print pay
