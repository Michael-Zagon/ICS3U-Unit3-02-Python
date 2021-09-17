#!/usr/bin/env python3

# Created by: Michael Zagon
# Created on: Sep 2021
# This program is a number guessing game

import constants


def main():
    # This function is the number guessing game

    # Input
    guessed_number = int(input("Pick a number between 0-9: "))
    print("")

    # Process and Output
    if guessed_number == constants.CORRECT_NUMBER:
        print("You guessed the correct number!")

    if guessed_number != constants.CORRECT_NUMBER:
        print("Incorrect, please run again.")
    print("")
    print("Done.")


if __name__ == "__main__":
    main()
