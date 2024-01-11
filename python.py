import random
import os

os.system('cls')

def sum(array):
    """Return sum of array which is in argument"""
    result = 0
    for n in array:
        result += n
    return result

def rand():
    """Returns random integer value from 1 to 10."""
    return random.randint(1, 10)

def format_ace(array):
    """This function is used to assign the value to Ace, either 1 or 11 on the basis of sum of cards. Return the formatted array which is passed."""
    if array.count(1):
        if sum(array) < 21:
            array[array.index(1)] = 11
    if array.count(11):
        if sum(array) > 21:
            array[array.index(11)] = 1
    return array        
    
def computer_format(computer):
    """This function returns a formatted array. It decides the cards of computer."""
    while(sum(computer) < 16):
        computer.append(rand())
        computer = format_ace(computer)
    return computer
            
human = [1, rand()]
computer = [rand(), rand()]

print("Welcome to the game of BLACKJACK!")
input("Press enter to continue...")

while (1):
    human = format_ace(human)
    computer = format_ace(computer)
    print(f"\nYour card: {human}")
    print(f"Your current score: {sum(human)}")
    print(f"Computer's single card: [{computer[0]}]") 
    pick = input("Pick a card? y or n: ")
    if pick == 'y':
        human.append(rand())
        human = format_ace(human)
        if sum(human) > 21:
            break
    else:
        break

computer = computer_format(computer)

print(f"\nYour cards: {human}")
print(f"Your score: {sum(human)}")
print(f"Computer's card: {computer}")
print(f"Computer's score: {sum(computer)}\n")

if sum(human) > 21:
    print("Your score is above 21, You LOST!")
elif sum(computer) > 21:
    print("Computer's socre is greater than 21, You WIN!")
elif sum(human) > sum(computer):
    print("Your score is greater than computer, You WIN!")
elif sum(human) < sum(computer):
    print("Your score is less than computer, You LOST!")
elif sum(human) == sum(computer):
    print("It's a DRAW!")