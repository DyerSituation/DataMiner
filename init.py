# DataMiner
from collections import defaultdict
#code so far:


#create list of all items
def c1Generator(dataSet):
  #try to use set instead?
  allItems = []
  for marketBasket in dataSet:
    for item in marketBasket:
      if not [item] in allItems:
        allItems.append([item]);

  allItems.sort()
  return list(map(frozenset, allItems)) 


#return list of items that meet support threshhold
def supportList(Ck, Doc, threshhold):
  itemcount = defaultdict(int)
  totalSize = len(Doc)
  supportList = []
  for transaction in Doc:
    for candidate in Ck:
      if candidate.issubset(transaction):
        itemcount[candidate] += 1
  for item in itemcount:
    support = float(itemcount[item])/float(totalSize)
    if support >= threshhold:
      supportList.append(item)
  return supportList



  
#return Ck
#def aprioriGen(lkPrev):

def main():
  
  dataSet = [[1, 3, 4], [2, 3, 5], [1, 2, 3, 5], [2, 5]]
  
  Lall = []
  #proccess data 
  C1 = c1Generator(dataSet)
  L1 = supportList(C1, dataSet, supportThresh)
  Lall.append(L1)
  k = 2
  supportThresh = .3
  totalSize = len(C1)
#  while(len(Lall[k-1])>0):
#    Ck =

  print supportList(C1, dataSet, supportThresh)
  
  
  #create list of Ck
  
  #Actual Apriori Algo
  """
  L1 = {large 1 item sets}
  while(Lk-1 not empty):
    Ck = aprioriGen(Lk-1)
    for transaction in dataset
      Ci = subset(Ck, transaction) // candidates contained in transaction 
      for candidates in Ci
        c.count++
  #Check confidence
  
  #association rule maker
"""  
  
if __name__ == '__main__': main()
