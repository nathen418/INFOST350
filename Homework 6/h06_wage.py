# Author: Nate Goldsborough
# Assignment: Homework 5
# Filename: h06_wage.py
# Class: INFOST350
# Date: 10/18/2021
# Description: calculate an employees weekly wages

def calculate_wage(hours, rate):
    if hours > 40:
        overtime = hours - 40
        pay = (40 * rate) + (overtime * (rate * 1.5))
    else:
        pay = hours * rate
    return pay

def main():
    try:
        hours = float(input("Enter the number of hours worked: "))
        rate = float(input("Enter the hourly rate: "))
    except (ValueError, TypeError):
        print("Error: Please enter a number")
        main()
    print("The weekly pay is: $", format(calculate_wage(hours,rate), '.2f'), sep='')

if __name__ == "__main__":
    main()

# Sample Output:
# Enter the number of hours worked: 49
# Enter the hourly rate: 9.25
# The weekly pay is: $494.88