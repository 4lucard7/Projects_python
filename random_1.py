import random

print("""Welcome to the Coin Guessing Game!
Choose a method to toss the coin:
1.Using random.random()
2.Using random.randint()""")

choice=input(print("Enter your choice (1 or 2):"))

if choice== "1":
    random_number = random.random()
    if random_number >= 5:
      computer_result = "KING"
    else:
        computer_result = "CROWN"
elif choice == "2":
     random_numb2 = random.randint(0.1) 
     if random_numb2 == 0:
        computer_result = "KING"
     else:
        computer_result = "CROWN"
else:
    print("Sorry! choice 1 or 2.") 

choice_1=input(print("choice KING or CROWN:")).lower()

if choice_1 == computer_result:
    print("Congrulations!You Won.")

else:
    print(f"""Sorry! you lose wrong choice.
    the right choice is :{computer_result}.""")