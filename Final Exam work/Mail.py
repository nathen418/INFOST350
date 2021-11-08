import smtplib
import re
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from dotenv import load_dotenv

load_dotenv()

class Mailsend:
    def __init__(self, to, subject, contents):
        self.__to = to
        self.__subject = subject
        self.__contents = contents
        self.__asp = {ASP}
        self.__host = 'smtp.mail.me.com'
        self.__port = 587
        self.__username = "supersecretaddress3"
        self.__from = "supersecretaddress2"
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
            print('Login failed')
            return False
        message = MIMEMultipart()
        message['From'] = self.__from
        message['To'] = self.__to
        message['Subject'] = self.__subject
        textPart = MIMEText(self.__contents, 'plain')
        message.attach(textPart)
        try:
            server.send_message(message)
        except:
            print('Send failed')
            return False
        return True

    def validateEmail(self):
        if len(self.__to) > 7:
            if re.match("^.+\\@(\\[?)[a-zA-Z0-9\\-\\.]+\\.([a-zA-Z]{2,3}|[0-9]{1,3})(\\]?)$", self.__to) != None:
                return True
        return False