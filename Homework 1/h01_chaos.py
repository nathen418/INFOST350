# Author: Nate Goldsborough
# Assignment: Homework 1
# Class: INFOST350
# Date: 9/15/2021
# Description: This program will get some random numbers from a user generated seed

def main():
    print("Hello") # a statement to guide a user
    x = float(input("Enter a number between 0 and 1:  "))
    # x = eval("Enter a number between 0 and 1:  ")) #! Dangerous and could result in arbitrary code execution unless input is properly sanitized

    for i in range(15):
	    x = 3.9 * x * (1 - x)
	    print(x)


if __name__ == "__main__":
    main()