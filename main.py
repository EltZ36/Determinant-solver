import numpy as np

def Calculator():
  Question = int(input("Which option do you want to do? \n (1) Addition or (2) Multiplication))
  rows = int(input("\nHow many rows?"))
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
    pass
  else:
    print("Please put in the number next to the option you want.")
    Calculator()

def Determinant():
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
                       
def Start():
   Question = "Calculator (1) or Solve a 2 by 2 Determinant? (2)"
  print(Question)
  dictonary = {
    "1":Calculator, "2":Determinant 
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

