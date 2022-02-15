import random
rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

user_choice = input("What do you choose? Type 0 for Rock, 1 for Paper, or 2 for scissors. ")

user_choiceint = int(user_choice)

gamer = [rock, paper, scissors]

computer = random.choice(gamer)
if user_choiceint >= 3 or user_choiceint <0:
  print("You typed an invalid number. Try again.")
else:
  print(f"\nYou choose {gamer[user_choiceint]}")
  print(f"The computer choose {computer}")

  if user_choiceint == 0 and computer == gamer[0]:
      print("You draw")
  elif user_choiceint == 0 and computer == gamer[1]:
      print("You lose")
  elif user_choiceint == 0 and computer == gamer[2]:
      print("You win")

  if user_choiceint == 1 and computer == gamer[1]:
      print("You draw")
  elif user_choiceint == 1 and computer == gamer[2]:
      print("You lose")
  elif user_choiceint == 1 and computer == gamer[0]:
      print("You win")


  if user_choiceint == 2 and computer == gamer[2]:
      print("You draw")
  elif user_choiceint == 2 and computer == gamer[0]:
      print("You lose")
  elif user_choiceint == 2 and computer == gamer[1]:
      print("You win")
