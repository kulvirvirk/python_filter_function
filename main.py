# The filter() method filters the given sequence with the help of a function that tests each element in the sequence to be true or not.

def fun(variable):
  letters = ['a', 'e', 'i', 'o', 'u']
  if (variable in letters):
    return True
  else: 
    return False

sequence = ['g', 'e','e', 'j', 'k', 's', 'p', 'r']
#using filter function
filtered = filter(fun, sequence)

print('The filtered letters are:' )
for s in filtered: 
  print(s)
