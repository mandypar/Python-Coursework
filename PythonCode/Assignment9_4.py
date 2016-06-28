name = raw_input("Enter file:")
if len(name) < 1 : name = "mbox-short.txt"
handle = open(name)  
d = dict()
for line in handle:
    line = line.rstrip()
    if not line.startswith('From ') : continue
    words = line.split()
    email = words[1]
    if email in d:
        d[email] += 1
    else:
        d[email] = 1
# make list of values so I can take the max
lst = d.values()
m = max(lst)
# look through all email and compare max to value, print max email, value pair
for address in d:
    if d[address] >= m:
        print address, d[address]