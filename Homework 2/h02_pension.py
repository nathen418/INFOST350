# Author: Nate Goldsborough
# Assignment: Homework 2
# Filename: h02_pension.py
# Class: INFOST350
# Date: 9/25/2021
# Description: A program to compute the value of an investment
#              carried 30 years into the future.


def main():
    principal =  float(input("Enter the initial principal: "))        
    apr = float(input("Enter the annual interest rate: "))

    for i in range(30):
        principal += (principal * apr)
    print('The value in 30 years is $' + '{:.2f}'.format(principal))


if(__name__ == "__main__"):
    main()


# Sample Output:
# Enter the initial principal:   1000
# Enter the annual interest rate:    0.05
# The value in 30 years is $4321.94