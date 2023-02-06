#let's import the ability to pull a random integer first
from random import randint
#here's our greeting message
print("Welcome to Mr. Alex's Patented Dice Rolling App (patent pending)!")
#now we declare a variable and ask the user how many dice to roll
#we'll store that number in the variable
pile_of_dice = int(input("How many dice should we roll? "))
print(f"Okay, we'll roll {pile_of_dice} dice.") 
#now we find out how many sides are on each die by asking the user
dice_sides = int(input("How many sides on each dice? "))
print(f"Okay, we're going to roll D {dice_sides} s.")
print("Sounds good to me! Let's ROLL DEM BONEZ!")
#here comes the math
# rolls = int(pile_of_dice)+1
#the plus one on line previous accounts for how python counts with integers
# x = range(1,rolls)
#declare a variable to store our total value rolled
total = 0
for n in range(pile_of_dice):
    damage_per_die = randint(1,int(dice_sides))
    total += damage_per_die
    print(damage_per_die)
print (f"Wow, that's {total} total.")

