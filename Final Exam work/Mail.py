import smtplib
import re
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import os
from os.path import join, dirname
from dotenv import load_dotenv

class Mail:
    def __init__(self, to_addr, from_addr, subject, templateName, contents):
        self.__to = to_addr
        self.__subject = subject
        self.__contents = contents
        self.__templateName = templateName
        self.__asp = 'asp'
        self.__host = 'smtp.mail.me.com'
        self.__port = 587
        self.__username = "supersecretaddress3"
        self.__from = from_addr

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

    def deliver(self):
        server = smtplib.SMTP(self.__host, self.__port)
        server.starttls()
        try:
            server.login(self.__username, self.__asp)
        except:
            print('Login failed. Please try again later')
            return False
        message = MIMEMultipart()
        message['From'] = self.__from
        message['To'] = self.__to
        message['Subject'] = self.__subject
        textPart = MIMEText(self.__contents, 'plain')
        message.attach(textPart)
        try:
            server.send_message(message)
            return True
        except:
            print('Send failed')
            return False

    def validateEmail(self):
        if len(self.__to) > 7:
            if re.match("^.+\\@(\\[?)[a-zA-Z0-9\\-\\.]+\\.([a-zA-Z]{2,3}|[0-9]{1,3})(\\]?)$", self.__to) != None:
                return True
        return False

    def getTemplateByName(self):
        if self.__templateName == 'friend':
            with open('templates/friend.txt') as f:
                return f.read()
        elif self.__templateName == 'teacher':
            with open('templates/teacher.txt') as f:
                return f.read()
        #! More templates can be added here. These are just some examples