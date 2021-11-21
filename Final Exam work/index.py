from Mail import Mail
import re
import json

def validateEmail(email):
    if len(email) > 7:
        if re.match("^.+\\@(\\[?)[a-zA-Z0-9\\-\\.]+\\.([a-zA-Z]{2,3}|[0-9]{1,3})(\\]?)$", email) != None:
            return True
    return False

def main():
    # Welcome the user and give them a startup message
    print("This program will send an email to a user.")
    print("Please enter the following information:")

    # Get the user's info, what template they want and the details of what they want to send
    while True:
        to_addr = input("To: ")
        if (validateEmail(to_addr)):
            break
        else:
            print("Invalid email address. Please type a correct one.")
    subject = input("Subject: ")
    templateName = input("Please enter the name of the template that you want to fill out: ")
    body = "Stuff"


    # create the email object and send the email
    email = Mail(to_addr, subject, body)
    email.create()
    email.send()

if __name__ == "__main__":
    main()