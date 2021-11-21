import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import json

class Mail:
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
        message = MIMEMultipart()
        message['From'] = self.__from
        message['To'] = self.__to
        message['Subject'] = self.__subject
        textPart = MIMEText(self.__contents, 'plain')
        message.attach(textPart)
        self.__message = message

    def send(self):
        server = smtplib.SMTP(self.__host, self.__port)
        server.starttls()
        try:
            server.login(self.__username, self.__asp)
        except:
            print('Login failed. Please try again later')
            return False
        try:
            server.send_message(self.__message)
        except:
            print('Message failed to send. Please try again later')
            return False
        server.quit()