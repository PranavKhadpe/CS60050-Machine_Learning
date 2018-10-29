#Roll number: 15EE35015
#Name: Khadpe Pranav Ajay
#Assignment No: 3
#Specific Compilation/ Exectution flags: run using: python 15EE35015_3.py. Training data in same directory as data3.csv.
# Test data in same directory as test3.csv

import math

train_data_file = "data3.csv"
test_data_file = "test3.csv"

w, h = 9, 20; # training data size is fixed
train_data = [[0 for x in range(w)] for y in range(h)]

w, h = 8, 4; # test data size is fixed
test_data = [[0 for x in range(w)] for y in range(h)]

# compute P(label=0) and P(label=1)
with open(train_data_file) as f:
	lines = f.read().split("\n")
	i = 0;
	for line in lines:
		currentline = line.split(",")
		if len(currentline) != 9:
			break
		train_data[i] = list(currentline)
		i = i + 1

with open(test_data_file) as f:
		lines = f.read().split("\n")
		i = 0;
		for line in lines:
			currentline = line.split(",")
			if len(currentline) != 8:
				break
			test_data[i] = list(currentline)
			i = i + 1

# split into positive and negative instances
positive = []
negative = []
for x in range(len(train_data)):
	if int(train_data[x][8]) == 1:
		positive.append(train_data[x])
	else:
		negative.append(train_data[x])
# computing P(positive) and P(negative)
p_1 = float(len(positive) + 1)/float(len(positive)+len(negative) + 2)
p_0 = float(len(negative) + 1)/float(len(positive)+len(negative) + 2)

#compute p(x|0) and p(x|1) for each attribute
conditionals = []
p_x1_0 = 0
p_x1_1 = 0
for x in range(8):
	for y in range(len(positive)):
		if int(positive[y][x]) == 1:
			p_x1_1 = p_x1_1 + 1
	p_x1_1 = float(p_x1_1 + 1)/float(len(positive) + 2)

	for y in range(len(negative)):
		if int(negative[y][x]) == 1:
			p_x1_0 = p_x1_0 +1
	p_x1_0 = float(p_x1_0 + 1)/float(len(negative) + 2)
	conditionals.append([p_x1_0, p_x1_1])
	p_x1_1 = 0
	p_x1_0 = 0

f = open("15EE35015_3.out","w")
p_yes = math.log10(p_1)
p_no = math.log10(p_0)
for x in range(len(test_data)):
	for y in range(8):
		if int(test_data[x][y]) == 1:
			p_yes = p_yes + math.log10(conditionals[y][1])
			p_no = p_no + math.log10(conditionals[y][0])
		else:
			p_yes = p_yes + math.log10(float(1) - conditionals[y][1])
			p_no = p_no + math.log10(float(1) - conditionals[y][0])
	if p_yes > p_no :
		f.write(str(1)+ " ")
	else:
		f.write(str(0)+ " ")
	p_yes = math.log10(p_1)
	p_no = math.log10(p_0)
f.close()
