import sys
import csv
import itertools
from collections import defaultdict

#http://blog.hackerearth.com/beginners-tutorial-apriori-algorithm-data-mining-r-implementation

# min_sup = sys.argv[2]
# min_conf = sys.argv[3]
min_sup = 0.00
min_conf = 0.5

file_name = sys.argv[1]
with open(file_name) as f:
	rows = csv.reader(f)
	biglist = list(rows)
	#populate dictionary for k=1 itemsets|frequency
	sets1 = {}
	for row in biglist:
		for i in range(0, len(row)):
			row[i] = str(i) + "-" + row[i].rstrip()		#attach column number to the item

			'''
			consider doing if i == column number, round(int(row[i]), 0) for some columns
			'''
			if row[i] not in sets1:
				sets1[row[i]] = 1
			else:
				sets1[row[i]] += 1
		row = set(row)
min_sup_count = int(min_sup*len(biglist))

#fill in listsets1, initialize stuff for while loop
first = True
frequents = 1
frequentsets = []
list1 = []
for item in sets1:
	if sets1[item] >= min_sup_count:
		list1.append(item)
		frequentsets.append([item, sets1[item]])
while frequents > 0:
	#generate listk - k+1 itemset from the previous iteration's itemset
	listk = []
	if first == True:
		listk = list(itertools.combinations(list1, 2))
		first = False
	else:
		for k, v in dictk.iteritems():
			endings = itertools.combinations(v, 2)
			for e in endings:
				listk.append(list(k) + list(e))
	#populate dictionary for k+1 itemset - itemset|frequency
	setsk = {}
	for row in biglist:
		for itemset in listk:
			itemset = set(itemset)
			if itemset.issubset(row):
				itemset = tuple(itemset)
				if itemset not in setsk:
					setsk[itemset] = 1
				else:
					setsk[itemset] += 1
	#create dict of disscted items for use in the next iteration
	dictk = defaultdict(list)
	for item in setsk:
		if setsk[item] >= min_sup_count:
			item = list(item)
			dictk[tuple(item[:-1])].append(item[-1])
			#store the frequent sets in a list for making association rules from
			frequentsets.append([item, setsk[item]])
	#update loop condition
	frequents = len(dictk)

#generate all possible association rules that follow the format {a,b,c,...} -> y
rules = {}		#(leftside, rightside) | frequency of leftside
for itemset in frequentsets:
	if len(itemset) > 1:
		for i in range(len(itemset)):
			dupe = itemset
			y = dupe.pop()
			entry = (tuple(dupe), y)
			rules[entry] = 0
			dupe.insert(0, y)
			#print "entry is", entry

#confidence of an association rule x -> y is (support of x U y)/(support of x)
#calculate the frequency to calculate the support, y frequencies are already in sets1
for row in biglist:
	for ru in rules:
		leftside = set(ru[0])
		if leftside.issubset(row):
			rules[ru] += 1

listrules = []
for ru in rules:
	support = rules[ru]/sets1[ru[1]]
	lf = support	#ho ho ho swept the rug out from under ur feet, this is support now!!
	if support >= min_conf:
		listrules.append((ru, support))

#print
for rule in listrules:
	print rule[0], "-", rule[1], "%"