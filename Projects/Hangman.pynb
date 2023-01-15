import random

def hangman():
   options=["pikachu","iota" ,"charizard" ,"togepi","coc","pokemon","altaf"]
   word=random.choice(options)

   validLetters='abcdefghijklmnopqrstuvwxyz'
   turns=10
   guessmade=''

   while len(word)>0 :
      main=""
      missed=0

      # to give hint no of chars in the word
      for letter in word:
         if letter in guessmade:
            main += letter
         else:
            main=main+"_"+" "

      if main==word:
         print(main)
         print("You win!")
         break

      print("Guess the word:",main)
      guess=input()

      if guess in validLetters:
         guessmade += guess
      else:
         print("Enter a valid character")
         guess=input()

      if guess not in word:
         turns -=1

         if turns==9:
            print("9 turns left")
            print(" ------- ")

         if turns==8:
            print("8 turns left")
            print(" ------- ")
            print("    0    ")

         if turns==7:
            print("7 turns left")
            print(" ------- ")
            print("    0    ")
            print("    |    ")

         if turns==6:
            print("6 turns left")
            print(" ------- ")
            print("    0    ")
            print("    |    ")
            print("   /    ")

         if turns==5:
            print("5 turns left")
            print(" ------- ")
            print("    0    ")
            print("    |    ")
            print("   / \   ")

         if turns==4:
            print("4 turns left")
            print(" ------- ")
            print("  \ 0    ")
            print("    |    ")
            print("   / \   ")

         if turns==3:
            print("3 turns left")
            print(" ------- ")
            print("  \ 0 /  ")
            print("    |    ")
            print("   / \   ")

         if turns==2:
            print("2 turns left")
            print(" ------- ")
            print("  \ 0 /| ")
            print("    |    ")
            print("   / \   ")

         if turns==1:
            print("1 turns left")
            print("Last breaths counting, Take care!")
            print(" ------- ")
            print("  \ 0_/|  ")
            print("    |    ")
            print("   / \   ")

         if turns==0:
            print("You loose")
            print("You killed a kind man")
            print(" ------- ")
            print("    0_|  ")
            print("   /|\   ")
            print("   / \   ")
            break


name=input("Enter your name ")
print("Welcome",name)
print("--------------")
print("try to guess the word in less than 10 attempts")
hangman()

