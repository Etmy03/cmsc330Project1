from functools import reduce

def is_present(lst,x):
  if lst.count(x) > 0:
    return True

def count_occ(lst,target):
  return lst.count(target)

def uniq(lst):
  rlst=[]
  
  for i in lst:
    if rlst.count(i) == 0:
      rlst.append(i)
        
  return rlst

def find_max(matrix):
  myMax = 0
  for x in matrix:
    myMax = max(myMax,max(x))
  return myMax

def count_ones(matrix):
  one = 0
  for x in matrix:
    one += x.count(1)
  return one

def addgenerator(x):
  return lambda y : y+x

def apply_to_self():
  return lambda x, lamb : x + lamb(x)

def ap(fns,args):
  return fns(args)

def map2(matrix,f):
  newX = []
  newY = []
  
  for x in matrix:
    for y in x:
      newY.append(f(y))
    newX.append(newY.copy())
    newY.clear()
  
  return newX
