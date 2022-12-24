import random

#random number generating
num=random.randint(1,100)
# print(num)

guess=None
guesses=0
flag=False

print("You have 10 guesses to guess the correct number..")

while guess!=num and guesses<10 :
   guess=int(input("Enter the guess number: "))
   guesses+=1
   if(guess==num):
      flag=True
      break
   else:
      if(guess>num):
         print("You have guessed higher..Guess a lower number")
      else:
         print("You have guessed lower..Guess a higher number")

if(flag):
   print(f"\nYou guessed the correct answer in {guesses} guesses")
else :
   print("\nGame over ...Guesses over, try again!")
