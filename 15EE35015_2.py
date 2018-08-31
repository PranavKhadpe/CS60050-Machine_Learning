#Roll number: 15EE35015
#Name: Khadpe Pranav Ajay
#Assignment No: 2
#Specific Compilation/ Exectution flags: run using: python 15EE35015_2.py. Training data in same directory as data2.csv.
# Test data in same directory as test2.csv

import math

train_data_file = "data2.csv"
test_data_file = "test2.csv"

w, h = 9, 24; # training data size is fixed
train_data = [[0 for x in range(w)] for y in range(h)]

w, h = 8, 4; # test data size is fixed
test_data = [[0 for x in range(w)] for y in range(h)]

def func(p):
	if p == 0:
		return(0)
	else:
		return(p*math.log(p, 2))


def ID3(examples, attributes, num_attributes, root_loc, tree):
	# print(num_attributes)
	check = 0
	# Check if all examples are positive
	for x in range(len(examples)):
		if int(examples[x][8]) == 0:
			check = 1
			break
	# If all examples positive: return root with label "+"
	if check == 0:
		tree[root_loc] = '+'
		return
	# Check is all examples are negative
	for x in range(len(examples)):
		if int(examples[x][8]) == 1:
			check = 1
			break
	# If all examples are negative: return root with label "-"
	if check == 0:
		tree[root_loc] = '-'
		return
	# If attributes empty return Root with most common example of target attribute
	if num_attributes == 0:
		sum = 0
		for x in range(len(examples)):
			sum = sum + int(examples[x][8])
		frac = float(sum)/float(len(examples))
		if frac >= 0.5:
			tree[root_loc] = '+'
		else:
			tree[root_loc] = '-'
		return

	# Determining best attribute
	gain_list = list(attributes)
	for y in range(len(attributes)):
		# If attribute has been discarded
		if int(attributes[y]) == -1:
			gain_list[y] = -1
			continue
		# Compute Entropy(S) - Gain.
		s = len(examples)
		sum = 0
		for x in range(len(examples)):
			sum = sum + int(examples[x][y])
		s_1 = sum
		s_0 = s - s_1
		s1_positive, s1_negative, s0_positive, s0_negative = 0, 0, 0, 0;
		for x in range(len(examples)):
			if (int(examples[x][y]) == 1) and (int(examples[x][8]) == 1):
				s1_positive = s1_positive + 1
				continue
			if (int(examples[x][y]) == 1) and (int(examples[x][8]) == 0):
				s1_negative = s1_negative + 1
				continue
			if (int(examples[x][y]) == 0) and (int(examples[x][8]) == 1):
				s0_positive = s0_positive + 1
				continue
			if (int(examples[x][y]) == 0) and (int(examples[x][8]) == 0):
				s0_negative = s0_negative + 1
				continue
		if s_1 == 0:
			p1_1 = 0
			p1_0 = 0
		else:
			p1_1 = float(s1_positive)/float(s1_positive+s1_negative)
			p1_0 = float(s1_negative)/float(s1_positive+s1_negative)
		if s_0 == 0:
			p0_1 = 0
			p0_0 = 0
		else:
			p0_1 = float(s0_positive)/float(s0_positive+s0_negative)
			p0_0 = float(s0_negative)/float(s0_positive+s0_negative)
		gain_list[y] = (float(s_1)/float(s))*(- func(p1_1) - func(p1_0)) +(float(s_0)/float(s))*(- func(p0_1) - func(p0_0))
	# Pick the variable with the lowest Entropy-Gain difference
	iteration = 0;
	# Fix issues in this comparison
	for x in range(0, len(attributes)):
		if gain_list[x] == -1:
			continue
		if iteration == 0:
			lowest = gain_list[x]
			variable = x
			iteration = iteration + 1
			continue 
		if float(gain_list[x]) < lowest:
			lowest = gain_list[x]
			variable = x

	# variable is x
	tree[root_loc] = variable
	attributes[variable] = -1
	num_attributes = num_attributes -1
	# 0 is left child 1 is right child
	# Split data into corresponding variable values
	Examples_1 = [[-1 for x in range(9)] for y in range(1)]
	Examples_0 = [[-1 for x in range(9)] for y in range(1)]
	count_1 = 0;
	count_0 = 0;
	for x in range(len(examples)):
		if int(examples[x][variable]) == 0:
			if count_0 == 0:
				Examples_0[0] = list(examples[x])
				count_0 = count_0+1
			else:
				Examples_0.append(examples[x])
			continue
		if int(examples[x][variable]) == 1:
			if count_1 == 0:
				Examples_1[0] = list(examples[x])
				count_1= count_1+1
			else:
				Examples_1.append(examples[x])
			continue
	# if examples_vi is empty
	if Examples_1[0][0] == -1:
		sum = 0
		for x in range(len(examples)):
			sum = sum + int(examples[x][8])
		frac = float(sum)/float(len(examples))
		if frac >= 0.5:
			tree[2*root_loc+2] = '+'
		else:
			tree[2*root_loc+2] = '-'
	if Examples_0[0][0] == -1:
		sum = 0
		for x in range(len(examples)):
			sum = sum + int(examples[x][8])
		frac = float(sum)/float(len(examples))
		if frac >= 0.5:
			tree[2*root_loc+1] = '+'
		else:
			tree[2*root_loc+1] = '-'
	attributes_copy = list(attributes)
	if Examples_0[0][0] != -1:
		ID3(Examples_0, attributes, num_attributes, 2*root_loc+1, tree)
	attributes = list(attributes_copy)
	if Examples_1[0][0] != -1:
		ID3(Examples_1, attributes, num_attributes, 2*root_loc+2, tree)
	return

def Test(test_data, tree):
	f = open("15EE35015_2.out","w")
	for x in range(len(test_data)):
		test = 0
		test = Classify(test_data[x], tree, 0)
		f.write(str(test) + " ")
	f.close()

def Classify(example, tree, root_loc):
	if tree[root_loc] == '-':
		return(0)
	if tree[root_loc] == '+':
		return(1)
	if int(example[tree[root_loc]]) == 0:
		return(Classify(example, tree, 2*root_loc+1))
	if int(example[tree[root_loc]]) == 1:
		return(Classify(example, tree, 2*root_loc+2))




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

final_tree = [-1 for x in range(512)]
attributes = [1, 1, 1, 1, 1, 1, 1, 1]
num_attributes = 8
root_loc = 0
# Learn Tree
ID3(train_data, attributes, num_attributes, root_loc, final_tree)
# print(final_tree)
Test(test_data, final_tree)

