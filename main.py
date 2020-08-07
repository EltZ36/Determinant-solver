import numpy as np
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
  for i in range(0,row):
    x = 1
    y = 1
    z = 1
    c1 = 0
    x2 = 1
    y2 = 1
    z2 = 1
    c2 = 0
    x3 = 1
    y3 = 1
    z3 = 1
    c3 = 0
    matrix = np.array([[x,y,z,c1], [x2,y2,z2,c2], [x3,y3,z3,c3]])
  return matrix 
start()

