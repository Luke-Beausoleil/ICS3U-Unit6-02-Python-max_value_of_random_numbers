#!/usr/bin/env python3

# Created by: Luke Beausoleil
# Created on: June 2021
# This program finds the max value of random numbers in a list

import random


def max_of_numbers(numbers):
    # this function finds the max value of the list
    temp_max = numbers[0]

    for loop_counter in range(1, len(numbers)):
        if numbers[loop_counter] >= temp_max:
            temp_max = numbers[loop_counter]

    return temp_max


def main():
    # this function generates random numbers and calls another function

    # list declaration
    numbers = []

    # process -- generate numbers
    for loop_counter in range(0, 10):
        single_number = random.randint(1, 100)
        numbers.append(single_number)
    print("The numbers are {0}".format(numbers))  # output
    maximum = max_of_numbers(numbers)  # call function
    print("The greatest number is {0}\nDone.".format(maximum))  # output


if __name__ == "__main__":
    main()
