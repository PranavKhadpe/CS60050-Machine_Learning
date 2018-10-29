#Roll number: 15EE35015
#Name: Khadpe Pranav Ajay
#Assignment No: 4
#Specific Compilation/ Exectution flags: run using: python 15EE35015_4.py. Training data in same directory as data4.csv.
# Test data in same directory as test4.csv

import math
import numpy as np 

def EucDist(arr1, arr2):
	dist = float(0)
	for i in range(len(arr2)):
		dist = dist + math.pow(float(float(arr2[i]) - float(arr1[i])), 2)
	return dist

train_data_file = "data4.csv"# alternately train.csv
test_data_file = "test4.csv"# alternately test.csv

w, h = 5, 74; # training data size is fixed
train_data = [[0 for x in range(w)] for y in range(h)]

w, h = 4, 26; # test data size is fixed
test_data = [[0 for x in range(w)] for y in range(h)]

with open(train_data_file) as f:
	lines = f.read().split("\n")
	i = 0;
	for line in lines:
		currentline = line.split(",")
		if len(currentline) != 5:
			break
		train_data[i] = list(currentline)
		i = i + 1

with open(test_data_file) as f:
		lines = f.read().split("\n")
		i = 0;
		for line in lines:
			currentline = line.split(",")
			if len(currentline) != 4:
				break
			test_data[i] = list(currentline)
			i = i + 1

f = open("15EE35015_4.out","w")
minim = float(0)
min_index = 0
dist = []
for i in range(len(test_data)):
	for y in range(len(train_data)):
		dist_y = EucDist(train_data[y], test_data[i])
		dist.append(dist_y)
	distance = np.asarray(dist)
	k = 4
	sort = np.argpartition(distance, k)
	sum = float(0)
	for j in range(5):
		sum = sum + float(train_data[int(sort[j])][4])
	sum = sum/5
	if sum < 0.5 :
		f.write(str(0)+" ")
	else:
		f.write(str(1) + " ")
	dist = []

f.close()







