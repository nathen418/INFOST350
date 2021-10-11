# Author: Nate Goldsborough
# Assignment: Homework 5
# Filename: h05_bmi.py
# Class: INFOST350
# Date: 10/11/2021
# Description: This program calculates the body mass index (BMI) for a user.

def main():
    height = float(input("Enter your height in inches: "))
    weight = float(input("Enter your weight in pounds: "))
    bmi = (weight * 720) / (height**2)
    print("Your BMI is:", bmi)

    if bmi < 19:
        print("You need to eat some more.")
    elif bmi >= 19 and bmi < 25:
        print("You are healthy.")
    elif bmi >= 25 and bmi < 30:
        print("You should go to the gym")


if __name__ == "__main__":
    main()

# Sample Output:
# Enter your height in inches: 66
# Enter your weight in pounds: 148
# Your BMI is: 24.462809917355372
# You are healthy.