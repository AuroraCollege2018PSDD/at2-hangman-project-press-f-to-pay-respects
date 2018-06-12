import random
c = 0
listy = ["chicken", "crow", "stork", "pigeon", "swan", "duck", "peacock", "parrot", "sparrow", "toucan", "penguin", "owl", "hummingbird", "seagull", "ibis", "emu", "kingfisher", "kiwi", "kookaburra", "dove", "conary", "puffin", "albatross", "eagle"]
z = (random.choice(listy))
letterlist = [ch for ch in z] 
print((len(z) * str(' _ ')))
guess = input("Welcome to hangman! A game that will make you pick letters until you get it right. Our theme here is birds. Mostly around the Australian area, some are also around other places too. Now, pick a letter or word to get started and see if you are wrong or right!" )
print("There may be an unexpected delay when you get the wrong guess as the graphics are loading...")
if guess == z:
  print("You won! On your first guess too!")
else:
  while guess != z:
   if guess in letterlist:
     print(guess + ' is in the word!')
     guess = input('You got it right! Guess again!' )
     if guess == z:
       print("You guessed the word! You win!")
       break
   elif guess == z:
     print("You guessed the word! You win!")
     break
   else:
     print(guess + ' is not in the word. Guess again.')
     c += 1
     guess = input('Guess again!' )
     print("You have used " + str(c) + " /10 guesses")
     if guess == z:
       print("You win!")
       break
     elif c == 1:
       print("_____________")
     elif c == 2:
       print("""|
|
|
|
|
|
|_____________""")
     elif c == 3:
         print("""|-----------
|
|
|
|
|
|_____________""")
     elif c == 4:
       print("""|-----------
|          o
|
|
|
|
|_____________""")
     elif c == 5:
       print("""|-----------
|          o
|          | 
|
|
|
|_____________""")
     elif c == 6:
       print("""|-----------
|          o
|         /| 
|
|
|
|_____________""")
     elif c == 7:
       print("""|-----------
|          o
|         /|\ 
|
|
|
|______________""")
     elif c == 8:
       print("""|-----------
|          o
|         /|\ 
|         /
|
|
|_____________""")
     elif c == 9:
       print("""|-----------
|          o
|         /|\ 
|         /\
|
|
|_____________""")
     elif c == 10:
       print("""|-----------
|          o
|         /|\ 
|         /\
|
|       Game Over
|_____________""")
       print("Oh no! The man has been hung try again next time.")
       break