# Author: Nate Goldsborough
# Assignment: Homework 5
# Filename: h05_int.py
# Class: INFOST350
# Date: 10/11/2021
# Description: Detect if a number is positive, negative, or zero

def main():
    num = float(input("Enter a number as a decimal please: "))
    if (num > 0):
        print("Positive")
    elif (num < 0):
        print("Negative")
    else:
        print("Zero")
    
if __name__ == "__main__":
    main()

# Sample Output:
# Enter a number as a decimal please: 3.23
# Positive