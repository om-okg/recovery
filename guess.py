import random
def guess_me():
 print("Welcome to the guessing game")
 guessNo=random.randint(1,100)
 attmpts=0

 while True:
  try:
   guess=int(input("Guess a number between 1 to 100: "))
   attmpts+=1

   if guess<guessNo:
    print("Too Low")
   elif guess>guessNo:
    print("Too High")
   else:
    print(f"Found it! in {attmpts} attmpts")
    break

  except ValueError:
   print("Enter a correct value between 1 to 100")

   
if __name__=="__main__":

 guess_me();
