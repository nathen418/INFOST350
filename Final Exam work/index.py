from Mail import Mail

def main():
    # Welcome the user and give them a startup message
    print("This program will send an email to a user.")
    print("Please enter the following information:")


    # Get the user's info, what template they want and the details of what they want to send
    to_addr = input("To: ")
    from_addr = "nathen418@playantares.com" #! Do not change this email address. All emails coming form this program will use this email address.
    subject = input("Subject: ")
    templateName = input("Please enter the name of the template that you want to fill out: ")
    body = "some text here" #! some code to get input from the user and then fill out the appropriate email template. then assign it as a string to the body variable.

    # create the email object and send the email
    email = Mail(to_addr, from_addr, subject, templateName, body)
    if (email.deliver()):
        print("Email sent successfully")
    else:
        print("Email failed to send")
    

if __name__ == "__main__":
    main()