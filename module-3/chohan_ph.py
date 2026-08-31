"""
Title: Cho-Han Dice Game
Author: Prince Hubbard
Date: August 31, 2026
Assignment: CSD325 Module 3.2 - Brownfield + Flowchart(s)

Purpose:
    Simulate the traditional Japanese Cho-Han dice game. The player bets on
    whether the sum of two dice will be even (CHO) or odd (HAN).

Changes made to the original program:
    1. Changed both user input prompts to "PH: ".
    2. Changed the house fee from 10 percent to 12 percent.
    3. Added an introduction notice explaining the 10 mon bonus.
    4. Added bonus logic for dice totals of 2 or 7.
"""

import random
import sys


JAPANESE_NUMBERS = {
    1: "ICHI",
    2: "NI",
    3: "SAN",
    4: "SHI",
    5: "GO",
    6: "ROKU",
}


print("""Cho-Han, by Al Sweigart al@inventwithpython.com

In this traditional Japanese dice game, two dice are rolled in a bamboo
cup by the dealer sitting on the floor. The player must guess if the
dice total to an even (cho) or odd (han) number.

BONUS: If the dice total is 2 or 7, you receive a 10 mon bonus.
""")

purse = 5000

while True:  # Main game loop.
    # Ask the player to enter a wager.
    print("You have", purse, "mon. How much do you bet? (or QUIT)")

    while True:
        pot = input("PH: ")

        if pot.upper() == "QUIT":
            print("Thanks for playing!")
            sys.exit()
        elif not pot.isdecimal():
            print("Please enter a number.")
        elif int(pot) > purse:
            print("You do not have enough to make that bet.")
        else:
            pot = int(pot)
            break

    # Roll two six-sided dice.
    dice1 = random.randint(1, 6)
    dice2 = random.randint(1, 6)

    print("The dealer swirls the cup and you hear the rattle of dice.")
    print("The dealer slams the cup on the floor, still covering the")
    print("dice and asks for your bet.")
    print()
    print("    CHO (even) or HAN (odd)?")

    # Ask for CHO or HAN until the player enters a valid selection.
    while True:
        bet = input("PH: ").upper()

        if bet != "CHO" and bet != "HAN":
            print('Please enter either "CHO" or "HAN".')
            continue
        break

    # Reveal the dice and calculate their total.
    print("The dealer lifts the cup to reveal:")
    print("  ", JAPANESE_NUMBERS[dice1], "-", JAPANESE_NUMBERS[dice2])
    print("    ", dice1, "-", dice2)

    dice_total = dice1 + dice2

    # Award 10 mon whenever the dice total is 2 or 7.
    if dice_total == 2 or dice_total == 7:
        print(f"The dice total is {dice_total}! You received a 10 mon bonus.")
        purse += 10

    # Determine whether the total is even or odd and check the player's bet.
    roll_is_even = dice_total % 2 == 0

    if roll_is_even:
        correct_bet = "CHO"
    else:
        correct_bet = "HAN"

    player_won = bet == correct_bet

    # Update the purse based on the result.
    if player_won:
        print("You won! You take", pot, "mon.")
        purse += pot

        house_fee = pot * 12 // 100
        print("The house collects a", house_fee, "mon fee.")
        purse -= house_fee
    else:
        purse -= pot
        print("You lost!")

    # End the game when the player has no money remaining.
    if purse <= 0:
        print("You have run out of money!")
        print("Thanks for playing!")
        sys.exit()
