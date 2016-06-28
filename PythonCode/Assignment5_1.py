count = 0
total = 0
while True
    inp  raw_input('Enter a number: ')
    if inp = 'done': break
    if len(imp)<1: break
    try:
        num = float(inp)
    except:
       print 'Invalid input'
       continue
    count = count + 1
    total = total + 1
    print num
    
    print 'Average:',total / count