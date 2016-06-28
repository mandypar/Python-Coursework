# Use the file name mbox-short.txt as the file name
fname = raw_input("Enter file name: ")
fh = open(fname)
total=0
count=0
for line in fh:
    if line.startswith("X-DSPAM-Confidence:") :
		position = line.find(':')
		position += 1
		value = float(line[position:])
		count += 1
		total += value
    continue
average = total / count
print ("Average spam confidence: " + str(average))
