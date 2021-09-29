# Author: Nate Goldsborough
# Assignment: Homework 3
# Filename: h03_int_remainder.py
# Class: INFOST350
# Date: 9/29/2021
# Description: This program will take two integers and divide them and return the quotient and remainder

def main():
    try:
        num1 = int(input("Please enter an integer for the dividend: "))
        num2 = int(input("Please enter an integer for the divisor: "))
    except(ValueError,TypeError):
        print("Invalid input")
        return
    
    print(f'Quotient is {num1//num2} and the remainder is {num1%num2}')

if __name__ == '__main__':
    main()

# Sample Output:
# Please enter an integer for the dividend: 55
# Please enter an integer for the divisor: 5
# Quotient is 11 and the remainder is 0