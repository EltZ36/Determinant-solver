def solve():
 pass
def start():
 while True:
  try:
    Question1 = int(input("How many rows?"))
    Question2 = int(input("How many columns?"))
    break
  except ValueError:
    print("Not an int. please try again")
    start()
    continue
  return Question1
  return Question2
print("Welcome to the determinant solver!")
start()
