# Author: Nate Goldsborough
# Assignment: Homework 2
# Filename: h01_01.py
# Class: INFOST350
# Date: 9/25/2021
# Description: This program will print out the name, age, and insurance status of a person, but fail due to a syntax error.


def main():
    Fname = "Johnson"
    Mname = "Glendson"
    Lname = " Winter"
    age = 89
    has_insurance = True
    print(age, Lname, has_insurance, ffname)

if (__name__ == "__main__"):
    main()


# Sample Output Error:
# Traceback (most recent call last):
#   File "c:\Users\nathe\Github\INFOST350\Homework 2\h01_01.py", line 14, in <module>
#     main()
#   File "c:\Users\nathe\Github\INFOST350\Homework 2\h01_01.py", line 11, in main
#     print(age, Lname, has_insurance, ffname)
# NameError: name 'ffname' is not defined