from itertools import product

# lists with length k and elements 1-n
#input: (str, integer)
#output: tuple of k length 


def all_lists(n, k):
  chars = list(n)
  results = []
  for x in product(chars, repeat = k):
    results.append(x)  
  for item in results:
      print (item)
  print (len(results))
  

all_lists('012', 3)
