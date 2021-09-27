# Author: Nate Goldsborough
# Assignment: Homework 2
# Filename: h01_03.py
# Class: INFOST350
# Date: 9/25/2021
# Description: The program combines a first and last name with a greeting,
#              then prints the result to the screen.


def main():
    first_name = "Nathen"
    last_name = "Goldsborough"
    full_name = first_name + " " + last_name

    message = "I am " + full_name.title() + ".\n"
    message2 = "Hello " + "class 350" + "!"
    greetings = message + message2

    print(greetings) 


if (__name__ == '__main__'):
    main()


# Sample Output:
# I am Nathen Goldsborough.
# Hello class 350!