import sys
import csv
import itertools
from collections import defaultdict
import copy

# min_sup = sys.argv[2]
# min_conf = sys.argv[3]
min_sup = 0.00
min_conf = 0.5


def populate_setdict(listk):
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
	return setsk

def generate_list(dictk):
	listk = []
	for k, v in dictk.iteritems():
		endings = itertools.combinations(v, 2)
		for e in endings:
			listk.append(list(k) + list(e))
	return listk

def generate_dissected_dict(listk):
	dictk = defaultdict(list)
	for item in setsk:
		if setsk[item] >= min_sup_count:
			freqfreqs[frozenset(item)] = setsk[item]
			item = list(item)
			dictk[tuple(item[:-1])].append(item[-1])
			#store the frequent sets in a list for making association rules from
			frequentsets.append(item)
	return dictk


file_name = sys.argv[1]
with open(file_name) as f:
	rows = csv.reader(f)
	biglist = list(rows)
	#populate dictionary for k=1 itemsets|frequency
	sets1 = {}
	for row in biglist:
		for i in range(0, len(row)):
			row[i] = str(i) + "-" + row[i].rstrip()		#attach column number to the item
			#consider doing if i == column number, round(int(row[i]), 0) for some columns
			if row[i] not in sets1:
				sets1[row[i]] = 1
			else:
				sets1[row[i]] += 1
		row = set(row)		#convert to set to be able to use issubset() later

#initialize stuff for while loop, fill in listsets1
first = True
frequents = 1
frequentsets = []
freqfreqs = {}
min_sup_count = int(min_sup*len(biglist))

list1 = []
for item in sets1:
	if sets1[item] >= min_sup_count:
		list1.append(item)
		frequentsets.append([item])
		freqfreqs[frozenset([item])] = sets1[item]

while frequents > 0:
	if first == True:
		listk = list(itertools.combinations(list1, 2))
		first = False
	else:
		listk = generate_list(dictk)	#dictk is from previous iteration
	setsk = populate_setdict(listk)

	dictk = generate_dissected_dict(setsk)
	#update loop condition
	frequents = len(dictk)

#generate all possible association rules that follow the format {a,b,c,...} -> y
rules = {}		#(leftside, rightside) | frequency of leftside
print "freqfreqs--------------------------\n",
for k,v in freqfreqs.items():
	print k, '-->', v

for itemset in frequentsets:
	if len(itemset) > 1:
		dupe = copy.deepcopy(itemset)
		for i in range(len(itemset)):
			y = dupe.pop()
			entry = (tuple(dupe), y)
			print "f xUy", tuple(itemset), "is", freqfreqs[frozenset(itemset)]
			print "f x", tuple(dupe), "is", freqfreqs[frozenset(dupe)]
			print "support is ", freqfreqs[frozenset(itemset)]/float(freqfreqs[frozenset(dupe)])
			rules[entry] = freqfreqs[frozenset(itemset)]/float(freqfreqs[frozenset(dupe)])
			dupe.insert(0, y)

#confidence of an association rule x -> y is (support of x U y)/(support of x)
#calculate the frequency to calculate the support, y frequencies are already in sets1
# print "rules--------------------------\n"
# for k,v in rules.items():
# 	print k, '-->', v

listrules = []
for ru in rules:
	support = rules[ru]
	if support >= min_conf:
		listrules.append((ru, support))



for rule in listrules:
	print rule[0][0], "->", rule[0][1], "-", rule[1]*100, "%"