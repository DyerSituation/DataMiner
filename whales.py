import sys
import csv
import itertools
from collections import defaultdict
import copy
from operator import itemgetter

# min_sup = sys.argv[2]
# min_conf = sys.argv[3]
min_sup = 0.00
min_conf = 0.0


def find_sets(dictk):
	listk = []
	for k, v in dictk.iteritems():
		endings = itertools.combinations(v, 2)
		for e in endings:
			listk.append(list(k) + list(e))
	return listk


def find_freqs(listk):
	#populate dictionary for k+1 itemset - itemset|frequency
	setsk = {}
	for row in biglist:
		for itemset in listk:
			itemset = frozenset(itemset)
			if itemset.issubset(row):
				itemset = frozenset(itemset)
				if itemset not in setsk:
					setsk[itemset] = 1
				else:
					setsk[itemset] += 1
	return setsk

def prune(listk):
	dictk = defaultdict(list)
	for item in setsk:
		if setsk[item] >= min_sup_count:
			freqfreqs[frozenset(item)] = setsk[item]
			item = list(item)
			dictk[frozenset(item[:-1])].append(item[-1])
			#store the frequent sets in a list for making association rules from
			frequentsets.append(item)
	return dictk


file_name = sys.argv[1]
with open(file_name) as f:
	rows = csv.reader(f)
	biglist = list(rows)
	#populate dictionary for k=1 - itemset|frequency
	sets1 = {}
	for row in biglist:
		for i in range(0, len(row)):
			row[i] = str(i) + "-" + row[i].rstrip()		#attach column number to the item in case same values are allowed in multiple columns
			if row[i] not in sets1:
				sets1[row[i]] = 1
			else:
				sets1[row[i]] += 1
		row = frozenset(row)		#convert to frozenset to be able to use issubset() later

#initialize stuff for while loop, start the k=1 case
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
		listk = find_sets(dictk)
	setsk = find_freqs(listk)
	dictk = prune(setsk)
	
	frequents = len(dictk)	#if set is empty, stop

#generate association rules that follow the format {a,b,c,...} -> y
rules = {}		#(leftside, rightside) | frequency of leftside
for itemset in frequentsets:
	if len(itemset) > 1:
		dupe = copy.deepcopy(itemset)
		for i in range(len(itemset)):
			y = dupe.pop()
			entry = (frozenset(dupe), y)
			#conf of rule is (support of x U y)/(support of x)
			confidence = freqfreqs[frozenset(itemset)]/float(freqfreqs[frozenset(dupe)])
			supportx = freqfreqs[frozenset(itemset)]/float(len(biglist))
			rules[entry] = [confidence, supportx]
			dupe.insert(0, y)

# print "rules--------------------------\n"
# for k,v in rules.items():
# 	print k, '-->', v

listrules = []
for ru in rules:
	support = rules[ru]
	if support >= min_conf:
		listrules.append((ru, support))


print "==Frequent itemsets (min_sup="+str(min_sup*100)+"%)"
for k,v in freqfreqs.items():
	support = v/float(len(biglist))
	print str(list(k))+', '+str(int(support*100))+"%"

print "==High-confidence association rules (min_conf="+str(min_conf*100)+"%"
for rule in sorted(listrules, key=itemgetter(1)):
	print list(rule[0][0]), "=>", rule[0][1], "Conf:", str(int(rule[1][0]*100))+"%,", "Support:", str(int(rule[1][1]*100))+"%"