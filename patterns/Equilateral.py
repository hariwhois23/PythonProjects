n = 5 
pattern = '*'
whitespace = 4 
for i in range(1, n+1):
  for j in  range(whitespace):
    print(' ', end='')
  whitespace -= 1
  for k in range(1,i*2):
      print(pattern, end='')
  print()
