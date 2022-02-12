import sys

print('''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/_____ /
*******************************************************************************
''')
print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.") 

first = input("As you enter the room, you notice levers. One red and one blue. To progress you must choose which one to pull. Type 'red' or 'blue':")

firstlower = first.lower()

if firstlower == "blue":
  print ("You return to life with contented ignorance. Game over.")
  sys.exit()
elif firstlower == "red":
  second = input("A door opens infront of you and a whole new world becomes visible. Do you wish to enter? Type 'yes' or 'no': ")
else:
    print("Incorrect input. Please try again")
    sys.exit()


secondlower = second.lower()

if secondlower == "no":
  print ("You decide to leave, vowing to never return but never feeling the same.")
  sys.exit()
elif secondlower == "yes":
  third = input("As you enter the room, a chill overtakes your body as you see the treasure chest directly in front of you. Do you want to go directly to the chest or search around? Type direct or search: ")
else:
    print("Incorrect input. Please try again")
    sys.exit()

thirdlower = third.lower()

if thirdlower == "direct":
  print("A trap activates killing you instantly. Game over.")
  sys.exit()
elif thirdlower == "search":
  four = input("You notice a trap ahead, and a switch to deactivate it. It has three wires exposed. Which wire would you like to cut? Please choose yellow, black or white. ")
else:
    print("Incorrect input. Please try again")
    sys.exit()

fourlower = four.lower()

if fourlower == "yellow":
    print("As you cut yellow, everything turns dark and as you tumble backwards you hit your head. Game over. ")
    sys.exit()
elif fourlower == "white":
    print("You cut the wire and the switch instantly exploads. Game over. ")
    sys.exit()
elif fourlower == "black":
    print("The chest creeks open and reveals exactly what you had hoped to find. Well done!")
else:
    print("Incorrect input. Please try again")
    sys.exit()