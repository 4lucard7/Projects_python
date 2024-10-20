import random

# Rock Paper Scissors ASCII Art
# Rock
rock="""
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
"""

# Paper
paper="""
     _______
---'    ____)____
           ______)
          _______)
         _______)
---.__________)
"""

# Scissors
scissors="""
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
"""

print("Welcome to the Rock, Paper, Scissors game:")
rules=input("Press 'Enter' to continue or type (help) for the rules:")

if rules.lower() == "help":
    print(""""
          ********RULES*********
          1) you choose and the computer chooses
          2)Rock smashes Scissors -> Rock wins
          3)Scissors cut papper -> scissors wins
          4)paper covers Rock -> Paper wins
          """)
    
choice = input(print("Enter your choice (Rock, Paper, scissors)")).lower()

if choice not in ['rock', 'paper', 'scissors']:
        print("Invalid choice! Please choice one of this tree choices ['rock', 'paper', 'scissors']")

else:
        if choice=="rock":
            print(f"\nYou choose:\n{rock}")
        elif choice=="paper":  
            print(f"\nYou choose:\n{paper}")
        else:
            print(f"\nYou choose:\n{scissors}")  

computer_choice = random.choice(['rock', 'paper', 'scissors'])

if computer_choice=="rock":
            print(f"\ncomputer choose:\n{rock}")
elif computer_choice=="paper":  
            print(f"\ncomputer choose:\n{paper}")
else:
            print(f"\ncomputer choose:\n{scissors}") 

if choice == computer_choice:
    print(f"Its a tie!{choice} \n {computer_choice}")

elif ((choice =="rock" and computer_choice == "scissors")
 or (choice =="paper" and computer_choice == "rock") 
 or(choice =="scissors" and computer_choice == "paper")): 
    print(f" You win! {choice} beats {computer_choice}")
else:
    print(f"You lose! {computer_choice} beats {choice}")   






 