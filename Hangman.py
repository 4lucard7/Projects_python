import random

words = ['morocco', 'spain', 'egypt', 'poland', 'japan']
random_word = random.choice(words)
display=[]

for word in random_word:
    display.append("_")
print(display)
lives = 6

while "_" in display and lives>0:
   
   guess = input("Please guess a letter:").lower()
   if guess not in random_word:
       lives -=1
   
   for position in range(len(random_word)):
       if random_word[position] == guess:
        display[position] = guess
print(display)
print(f"You have {lives} more tries")  

if lives ==0:
   print("""
         ******You!Lose!!
+---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========
""")
else:
   print("""
*****You!Won*****""")
   

       
          


