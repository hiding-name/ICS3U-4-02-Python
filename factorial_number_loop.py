#!/usr/bin/env python3

# Created by: Matsuru Hoshi
# Created on: Oct 2019
# This is program loop number multiplier


def main():
    # funciton calculates the number added up to number

    # variable
    answer = 1
    repeater = 0

    # Welcome statement
    print("Welcome, I will multiply numbers the number of times that you "
          "tell me.")
    print("Ex. 1 * 2 * 3 * 4 = 24")
    input("\nPress Enter to continue.")

    # input
    number = int(input("What is your number: "))

    # process
    while repeater < number:
        repeater = repeater + 1
        answer = answer * repeater

    print("The answer is " + str(answer) + ".")


if __name__ == "__main__":
    main()
