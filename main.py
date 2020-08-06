def solve():
 pass
def start():
  '''
  while True:
    try:
      Question1 = int(input("How many rows?"))
      Question2 = int(input("How many columns?"))
  except ValueError:
    print("Not an int. please try again")
    start()
    continue
  else:
    break
  return Question1
  return Question2
  '''
  row = 3
  column = 3
  for i in range(0,row):
    a = 1
    b = 1
    c = 1
    d = 1
    e = 1
    f = 1
    g = 1
    h = 1
    i = 1
    A = [[a,b,c], [d,e,f], [g,h,i]]
    if len(A) == column:
      break
  return A 
start()
