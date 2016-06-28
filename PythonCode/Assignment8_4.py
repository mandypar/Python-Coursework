fname = raw_input("Enter file name: ")
fh = open(fname)
lst = list()
for line in fh:
	sline = line.split()
	for word in sline:
				if word not in lst:
					lst.append(word)
            
lst.sort()            
print lst