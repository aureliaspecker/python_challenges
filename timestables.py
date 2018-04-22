"""
Aurelia Specker - 2018

Create a programme that will print the timetables (functions, lists, loops)

Four functions
1. Main
2. To get information from user (which times tables, how many entries)
3. Function to calculate timestables - not just print, but return a list to the main
4. Final function which displays (takes the list as an argument and prints it out)
"""

import os
import sys

def get_number():
    num = int(raw_input("Please insert a number: "))
    print ">>"

    return num


def calculation(num):
    #list_Multipliers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    new_list = []
    for i in range(0,11):
        new_list.append(i * num)

    return new_list

def displaying(new_list, num):
    for i, n in enumerate(new_list):
        print "{} * {} = {}".format(num, i , n)


def main():
    user_input = get_number()

    calculate = calculation(user_input)

    display = displaying(calculate, user_input)

if __name__ == "__main__":
    main()
