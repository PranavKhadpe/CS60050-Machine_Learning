#Roll number: 15EE35015
#Name: Khadpe Pranav Ajay
#Assignment No: 1
#Specific Compilation/ Exectution flags: run using: python 15EE35015_assignment1.py <filename.csv>

import sys

file_name = sys.argv[1]
count = 0
hypothesis = [0,0,0,0,0,0,0,0]
current_ex = [0,0,0,0,0,0,0,0]
with open(file_name) as f:
	lines = f.read().split("\n")
	for line in lines:
		currentline = line.split(",")
		if len(currentline) != 9:
			break
		# Negative examples are neglected
		if int(currentline[8]) == 0:
			continue
		# For first training example
		if count == 0:
			for i in range(0,8):
				if int(currentline[i]) == 1:
					hypothesis[i] = 1
				else:
					hypothesis[i] = -1
			count = count + 1
			continue
		# For all but first training example
		for i in range(0,8):
			if int(currentline[i]) == 1:
				current_ex[i] = 1
			else:
				current_ex[i] = -1
		# Minimal Generalisation
		for i in range(0,8):
			if hypothesis[i] != current_ex[i]:
				hypothesis[i] = 0 
conjunction = []
num = 8
for i in range(0,8):
	if hypothesis[i] == 1:
		conjunction.append(i+1)
		continue
	elif hypothesis[i] == -1:
		conjunction.append(-(i+1))
		continue
	else:
		num = num - 1
print repr(num)+",",
for i in range(0, len(conjunction)):
	if i == (len(conjunction)-1):
		print repr(conjunction[i]),
		break
	print repr(conjunction[i])+",",
print


