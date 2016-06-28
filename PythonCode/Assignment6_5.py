text = "X-DSPAM-Confidence:    0.8475";
loc = text.rpartition(' ')
answer = float(loc[2])
print answer


text = "X-DSPAM-Confidence:    0.8475";
position = text.find(':')
position = position + 1
answer = float(text[position:])
print answer