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
def supportList(Ck, threshhold):
  itemcount = {}
  
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
  while(L1 not empty):
    Ck = aprioriGen()

  #Check confidence
  
  #association rule maker
  
  
if __name__ == '__main__': main()
