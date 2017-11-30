# DataMiner

#code so far:


#create list of all items
def itemLister(dataSet):
  #try to use set instead?
  allItems = []
  for marketBasket in dataSet:
    for item in marketBasket:
      if not item in allItems:
        allItems.append(item)
  return allItems


#return list of items that meet support threshhold
def supportList(Ck, Doc, threshhold):
  itemcount = defaultdict(int)
  for transaction in Doc:
    for candidate in Ck:
      if candidate issubset(transaction)
        itemcount[candidate] += 1
  for item, count in itemcount:
    print "item:"
    print item
    print "count:"
    print count

  
#return Ck
def aprioriGen(lkPrev):

def main():
  
  dataSet = [[1, 3, 4], [2, 3, 5], [1, 2, 3, 5], [2, 5]]
  

  #proccess data 
  C1 = c1Generator(dataSet)
  
  print C1
  

  supportThresh = .3
  totalSize = len(myList)
  
  
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
  
  
if __name__ == '__main__': main()
