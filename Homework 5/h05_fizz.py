# Author: Nate Goldsborough
# Assignment: Homework 5
# Filename: h05_fizz.py
# Class: INFOST350
# Date: 10/11/2021
# Description: This program is a version of the game FizzBuzz.

def main():
    for i in range(1, 101):
        if i % 3 == 0 and i % 5 == 0:
            print("FizzBuzz")
        elif i % 3 == 0:
            print("Fizz")
        elif i % 5 == 0:
            print("Buzz")
        else:
            print(i)

if __name__ == "__main__":
    main()

# Sample Output:
# 1
# 2
# Fizz
# 4
# Buzz
# Fizz
# 7
# 8
# Fizz
# Buzz