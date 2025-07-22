n = 5 
pattern = '*'
whitespace = n-1
for i in range(1, n+1):
  for j in  range(whitespace):
    print(' ', end='')
  whitespace -= 1
  for k in range(i):
       print(pattern, end='')
  print()