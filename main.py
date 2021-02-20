import numpy as np

def Calculator():
  Question = int(input("Which option do you want to do? \n Addition (1) \n Multiplication (2) \nSubtraction (3")))
  rows = int(input("How many rows?"))
  columns = int(input("\nHow many columns?"))
  print("Fill in the matrix below")
  Array = input().split()
  #list() creates an empty list and map runs the int function with the arguments of the input of rows and columns. the list cannot go over the inputed amount of rows or columns. Ex. I put 2 rows in the input and 2 columns in the input as well. When I fill in the matrix, I can't put in 3 rows and 1 column. 
  Fill_in = list(map(int, Array))
  A = np.array(Fill_in).reshape(rows, columns)
  print("Fill in the second matrix below with " + str(rows) +" row(s) and "+ str(columns)+" column(s)")
  Array2 = input().split()
  Fill_in = list(map(int, Array2))
  B = np.array(Fill_in).reshape(rows, columns)
  if Question == 1:
    Add = A + B 
    print(Add)
  elif Question == 2:
    Mult = A.dot(B)
    print(Mult)
  elif Question == 3:
    Sub = np.subtract(A, B)
    print(Sub)
  else:
    print("Please put in the number next to the option you want again.")
    Calculator()

def two_matrix():
  row1 = 2
  print("Fill in the 1st row below.")
  Array = input().split()
  Fill_in = list(map(int, Array))
  M1 = np.array(Fill_in).reshape(row1)
  row2 = 2 
  print("Fill in the 2nd row below.")
  Array2 = input().split()
  Fill_in = list(map(int,Array2))
  M2 = np.array(Fill_in).reshape(row2)
  ad = M1[0] * M2[1]
  bc = M1[1] * M2[0]
  print(ad - bc)

def three_matrix():
  row1 = 3
  row2 = 3
  row3 = 3
  print("Fill in the 1st row")
  # a much more condensed version of the previous one on lines 33-34
  Array = list (map (int, input().strip().split()))
  M1 = np.array(Array).reshape(row1)
  print("Fill in the 2nd row")
  Array2 = list (map(int, input().strip().split()))
  M2 = np.array(Array2).reshape(row2)
  print("Fill in the 3rd row")   
  Array3 = list(map(int, input().strip().split()))
  M3 = np.array(Array3).reshape(row3)
  '''
  These variables are to solve the determinant and kind of go into the matrix like this:
  [a b c 
   d e f 
   g h i] except a is M1[0], b is M1[1], and c is M1[2]
  '''
  ei = M2[1]*M3[2]
  fh = M2[2]*M3[1]
  di = M2[0]*M3[2]
  fg = M2[2]*M3[0]
  dh = M2[0]*M3[1]
  eg = M3[0]*M2[1]
  Determinant = ((M1[0]*(ei - fh))-(M1[1]*(di-fg))+(M1[2]*(dh-eg)))
  print(Determinant)
                       
def Start():
  Question = "Calculator (1) \nSolve the determinant of a 2x2 matrix? (2) \nSolve the determinant of a 3x3 matrix? (3)"
  print(Question)
  dictonary = {
    "1":Calculator, "2":two_matrix, "3":three_matrix
  }
  while True:
    try:
      Option = input("Please select a number:")
      dictonary[Option]()
    except KeyError:
      print("Please type in the number again.")
      continue
    else:
      break
Start()

