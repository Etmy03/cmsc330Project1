from collections import Counter

def isPalindrome(n):
  n_str = str(n)
  n_len = int(len(n_str))
  
  # if input is one char return true
  if n_len==1:
    return True
  
  # loop through the tring and check is the corresponding char are the same
  for x in range(0,int(n_len/2)):
    #if the char at x is not equal char at last index -x : return false
    if n_str[x] != n_str[n_len-x-1]:
      return False
    
    #else return true
    return True

def nthmax(n, a):
  return_index = len(a)-1-n
  #if there is none
  if return_index < 0:
    return None
  
  #sort the array
  newArr = sorted(a, reverse=True)
  
  #return the nth larger
  return newArr[n]

def freq(s):
  #if s is empty
  if s=="":
    return ""
  
  #else
  return Counter(s).most_common()[0][0]

def zipHash(arr1, arr2):
  if len(arr1) != len(arr2):
    return None
  
  #creat dict
  return_Dict = dict(zip(arr1, arr2))
  return return_Dict

def hashToArray(hash):
  arrOfArr = []
  #if empty hash return empty arr
  if len(hash)==0:
    return []
  
  #else
  for x,y in hash.items():
    arrOfArr.append([x, y])
  
  return arrOfArr

def maxLambdaChain(init, lambdas):
  #use max contiguous subarray from cmsc351 
  #turn init to int
  i=int(init)
  lst=[i]
  lst2=[]
  
  # create loop and figure out the max
  for thisLambda in lambdas:
    for x in lst:
      lst2.append(thisLambda(x))
    lst = lst+lst2
  
  return max(lst)
