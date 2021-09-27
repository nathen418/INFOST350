# Author: Nate Goldsborough
# Assignment: Homework 1
# Filename: h01_chaos.py
# Class: INFOST350
# Date: 9/15/2021
# Description: This program will print some random numbers from a user generated seed

def main():
    print("This program will print some random numbers from a user generated seed.\n") # a statement to guide a user
    x = float(input("Enter a number between 0 and 1:  "))
    # x = eval(input("Enter a number between 0 and 1:  "))
    #! Dangerous and could result in arbitrary code execution unless input is properly sanitized

    for i in range(15):
	    x = 3.9 * x * (1 - x)
	    print(x)


if __name__ == "__main__":
    main()

# Sample Output:
# This program will print some random numbers from a user generated seed.

# Enter a number between 0 and 1:  0.4
# 0.9359999999999999
# 0.2336256000000002
# 0.6982742481960964
# 0.8216805577588637
# 0.5714343131637907
# 0.9550988417209882
# 0.16725167263043805
# 0.5431863474677594
# 0.9677262636303364
# 0.12180535501057962
# 0.4171783609551725
# 0.9482482468131205
# 0.19138668599295894
# 0.6035555074286068
# 0.9331774018366947