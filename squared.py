# !/user/bin/env python3

# Created by Trent Hodgins
# Created on 010/01/2021
# This is the Squared Loop program
# The user enters in a positive integer
# The program tells the user the squared answer
# To all the numbers from 0 to the number typed in


def main():
    # this function uses a for loop and calculates the square
    loop_counter = 0

    # input
    number_as_string = input("Enter in a integer >= 0: ")
    print("")

    # process and output
    try:
        number_as_integer = int(number_as_string)
        range_number = number_as_integer + 1
        for loop_counter in range(range_number):
            answer = loop_counter * loop_counter
            print("{0}² = {1}".format(loop_counter, answer))

    except Exception:
        print("You didn’t enter in a positive integer.")

    print("\nDone")


if __name__ == "__main__":
    main()
