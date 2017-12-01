import sys
import csv
import itertools
from collections import defaultdict

#http://blog.hackerearth.com/beginners-tutorial-apriori-algorithm-data-mining-r-implementation

# min_sup = sys.argv[2]
# min_conf = sys.argv[3]
min_sup = 0.01
min_conf = 0.5

file_name = sys.argv[1]
with open(file_name) as f:
	rows = csv.reader(f)
	biglist = list(rows)
	#populate dictionary for k=1 itemsets|frequency
	sets1 = {}
	for row in biglist:
		for i in range(0, len(row)):
			row[i] = str(i) + "-" + row[i]		#attach column number to the item

			'''
			consider doing if i == column number, round(int(row[i]), 0) for some columns
			'''
			if row[i] not in sets1:
				sets1[row[i]] = 1
			else:
				sets1[row[i]] += 1

min_sup_count = int(min_sup*len(biglist))

#fill in listsets1, initialize stuff for while loop
list1 = []
for item in sets1:
	if sets1[item] >= min_sup_count:
		list1.append(list1[item])
first = True
frequents = 1
frequentsets = []
while frequents > 0 {
	#generate listk - k+1 itemset from the previous iteration's itemset
	if first == True:
		temp = list(itertools.combinations(temp, 2))
		first = False
	else:
		listk = []
		for k, v in dictk:
			endings = itertools.combinations(v, 2)
			for e in endings:
				listk.append(k + e)
	#populate dictionary for k+1 itemset - itemset|frequency
	setsk = {}
	for row in biglist:
		for itemset in listk:
			if itemset in row:
				if itemset not in setsk:
					setsk[pair] = 1
				else:
					setsk[pair] += 1
	#create dict of disscted items for use in the next iteration
	dictk = defaultdict(list)
	for item in setsk:
		if setsk[item] >= min_sup_count:
			dictk[item[:-1]].append(item[-1])
			#store the frequent sets in a list for making association rules from
			frequentsets.append(item)
	#update loop condition
	frequents = len(tempdict)
}

#generate all possible association rules that follow the format {a,b,c,...} -> y
rules = {}		#(leftside, rightside) | frequency of leftside
for itemset in frequentsets:
	for i in range(len(itemset)):
		dupe = itemset
		y = dupe.pop(i)
		rules[(dupe, y)] = 0

#confidence of an association rule x -> y is (support of x U y)/(support of x)
#calculate the frequency to calculate the support, y frequencies are already in sets1
for row in biglist:
	for ru in rules:
		leftside = ru[0]
		if leftside in row:
			rules[ru] += 1
for ru, lf in rules:
	support = lf/sets1[ru[1]]
	lf = support	#ho ho ho swept the rug out from under ur feet, this is support now!!
	if support < min_conf:
		del rules[ru]

#print
for ru, support in rules:
	print ru, "-", support, "%"