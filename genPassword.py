import random
import string


def genPass(length=12, useUpper=True, useDigits=True, useSymbols=True):
 characters=string.ascii_lowercase
 
  
 if useUpper: 
  characters+=string.ascii_uppercase

 if useDigits:
  characters+=string.digits

 if useSymbols:
  characters+=string.punctuation


 return "".join(random.choice(characters) for _ in range(length))
 
def main():
 print("Let's Generate your Password!\n")
 #Getting the input  and converting to integer
 try:
  inputLnt=input("Enter the length of your password: ").strip()
  lnt= int(inputLnt) if inputLnt else 12
 except ValueError:
  print("Invalid Input! Setting default length as 12!")
  lnt=12

 #Generate and print the password
 secPass=genPass(lnt);
 print(f"Your password is {secPass} for length: {lnt}")


if __name__=="__main__":
 main()
