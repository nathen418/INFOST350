from Mail import Mail
import re
import json
import os


def validateEmail(email):
    # Using regex, check if the email is valid
    if len(email) > 7:
        if re.match("^.+\\@(\\[?)[a-zA-Z0-9\\-\\.]+\\.([a-zA-Z]{2,3}|[0-9]{1,3})(\\]?)$", email) != None:
            return True
    return False


def listTemplates():
    # Get the list of templates from the templates folder and return it as a list
    templates = os.listdir('templates')
    print("These are a list of templates:")
    ret = []
    for template in templates:
        ret.append(template[:-5])
    return ret
    

def openTemplate(templateName):
    # try to open the template the user specified
    try:
        f = open('templates/' + templateName + '.json')
        data = json.load(f)
        return data
    except FileNotFoundError:
        print("Template not found. Please try again.")


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

    # List the templates and ask the user to choose one
    templates = listTemplates()
    print(*templates, sep = ", ")
    templateName = input("Please enter the name of the template that you want to fill out: ")
    while templateName not in templates:
        print("Template not found. Please try again.")
        templateName = input("Please enter the name of the template that you want to fill out: ")

    # Open the template and get the data from the user and combine it with the template data
    data = openTemplate(templateName)
    body = str(data['template_body'])
    for var in data['template_variables']:
        body = body.replace(var, input(var + ': '))
    print(body)

    # create the email object and send the email
    email = Mail(to_addr, subject, body)

    # Create the email object
    email.create()
    
    # Get the user to read over the final email and make sure it is all correct
    if (not email.validate()):
        # If the email is not valid, ask the user to re-enter the information
        main()
    else:
        # If everything is correct, send the email
        email.send()


if __name__ == "__main__":
    # Run the main function
    main()