from Mail import Mailsend

def main():
    print("This program will send an email to a user.")
    print("Please enter the following information:")
    to = input("To: ")
    subject = input("Subject: ")
    body = "some text here" #! some code to get input from the user and then fill out the appropriate email template. then assign it as a string to the body variable.
    email = Mailsend(to, subject, body)
    print(email.validateEmail())
    email.deliver()


if __name__ == "__main__":
    main()