#!/usr/bin/env python3
# Created By: Jayden Smith
# Date: May 17, 2025
# This code finds the max value out of 10 random numbers


import random

import constants


def max_num_finder(numbers):
    # Set max num to 0
    max_num = 0

    # Checks which number is biggest out of the 10 nums
    for counter in range(len(numbers)):
        # What happens if they are greater
        if max_num < numbers[counter - 1]:
            max_num = numbers[counter - 1]

        # If not use a continue statement to keep it going
        else:
            continue
    return max_num


def main():
    # Set the list
    values = []

    # Gets the random numbers
    for counter in range(0, 10, 1):
        random_number = random.randint(constants.MIN_NUM, constants.MAX_NUM)
        values.append(random_number)
        print(counter, "number:", random_number)

    # Calls function that finds the max value
    max_num = max_num_finder(values)

    # Displays the max value
    print("The max value is", max_num)


if __name__ == "__main__":
    main()
