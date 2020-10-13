#Author: John Turnbach

def run():
  grade = input("Enter your CMPSC 131 grade: ")
  grade = int(grade)
  if grade >=93.0:
    letter = 'A'
  elif grade >=90.0:
    letter = 'A-'
  elif grade >=87.0:
    letter = 'B+'
  elif grade >=83.0:
    letter = 'B'
  elif grade >=80.0:
    letter = 'B-'
  elif grade >=77.0:
    letter = 'C+'
  elif grade >=70.0:
    letter = 'C'
  elif grade >=60.0:
    letter = 'D'
  elif grade <60.0:
    letter = 'F'

  print(f"Your letter grade for CMPSC131 is {letter}.")

if __name__ == "__main__":
  run()