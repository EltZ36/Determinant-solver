import numpy as np

def Multiplication():
  rows = int(input("\nHow many rows?"))
  columns = int(input("\nHow many columns?"))
  print("Fill in the matrix below")
  Array = input().split()
  '''
  list() creates an empty list and map runs the int function with the arguments of the input of rows and columns. 
  The list cannot go over the inputed amount of rows or columns. 
  Example: I put 2 rows in the input and 2 columns in the input as well. When I fill in the matrix, I can't put in 3 rows and 1 column. 
  '''
  Fill_in = list(map(int, Array))
  A = np.array(Fill_in).reshape(rows, columns)
  print("Fill in the second matrix below with " + str(rows) +" row(s) and "+ str(columns)+" column(s)")
  Array2 = input().split()
  Fill_in = list(map(int, Array2))
  B = np.array(Fill_in).reshape(rows, columns)
  Add = A.dot(B)
  print(Add) 

def addition():
  rows = int(input("\nHow many rows?"))
  columns = int(input("\nHow many columns?"))
  print("Fill in the matrix below")
  Array = input().split()
  Fill_in = list(map(int, Array))
  A = np.array(Fill_in).reshape(rows, columns)
  print("Fill in the second matrix below with " + str(rows) +" row(s) and "+ str(columns)+" column(s)")
  Array2 = input().split()
  Fill_in = list(map(int, Array2))
  B = np.array(Fill_in).reshape(rows, columns)
  Add = A + B
  print(Add) 
  
def start():
  Question = int(input("Which option do you want to do? \n Addition(1) Multiplication (2) Division (3) Find Determinant(4)"))
  print(Question)
  if Question == 1:
    addition()
  elif Question == 2:
    Multiplication()
  elif Question == 3:
    pass
  elif Question == 4:
    pass
  else:
    print("Please put in the number next to the option you want.")
    start()
start()


