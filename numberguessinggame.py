#!/usr/bin/env python3

# Created by: Lauren Wheatley
# Created on: May 2021
# This program plays the number guessing game


def main():
    # this function plays the number guessing game

    # input
    n = int(input("Enter a number between 1-10: "))
    print("")

    # process & output
    if n != 10:
        print("Wrong number!")
    if n == 10:
        print("Correct!")


if __name__ == "__main__":
    main()
