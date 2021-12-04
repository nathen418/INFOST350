import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import json

class Mail:
    # Constructor, get data from user and env.json
    def __init__(self, to_addr, subject, contents):
        f = open('env.json')
        data = json.load(f)
        self.__to = to_addr
        self.__subject = subject
        self.__contents = contents
        self.__asp = data['asp']
        self.__host = 'smtp.mail.me.com'
        self.__port = 587
        self.__username = data['username']
        self.__from = data['from_addr']
        
    #add all getters and setters
    def getTo(self):
        return self.__to
    
    def setTo(self, to):
        self.__to = to
    
    def setSubject(self, subject):
        self.__subject = subject
    
    def setContents(self, contents):
        self.__contents = contents
    
    def getContents(self):
        return self.__contents
    
    def getSubject(self):
        return self.__subject
        
    def create(self):
        # Setup and format the email itself
        message = MIMEMultipart()
        message['From'] = self.__from
        message['To'] = self.__to
        message['Subject'] = self.__subject
        textPart = MIMEText(self.__contents, 'plain')
        message.attach(textPart)
        # set the message object created to the class var
        self.__message = message

    def send(self):
        # Create the server object
        server = smtplib.SMTP(self.__host, self.__port)
        # Initiate a secure connection to the mail server
        server.starttls()
        try:
            # Try to login using the secure connection and the username and application specific password
            server.login(self.__username, self.__asp)
        except:
            print('Login failed. Please try again later')
            return False
        try:
            # Try to send the email over the previously created secure connection
            server.send_message(self.__message)
        except:
            print('Message failed to send. Please try again later')
            return False
        # Close the connection to the server and exit
        server.quit()
    
    def validate(self):
        # Get the user to validate that the contents of the email and associated data are correct
        print("Lets double check this is all correct")
        print("To: " + self.__to)
        print("Subject: " + self.__subject)
        print("Body:" + self.__message.as_string())
        answer = input("Is this correct? (y/n)")
        if answer == 'y':
            return True
        else:
            return False
