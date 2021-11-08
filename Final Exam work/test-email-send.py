import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

# Connection with the server
server = smtplib.SMTP(host='smtp.mail.me.com', port=587)
server.starttls()
res = server.login('supersecretaddress1', 'supersecret token here')
message = MIMEMultipart()
message['From'] = 'supersecretaddress3'
message['To'] = 'supersecretaddress2'
message['Subject'] = "Automated Email"

textPart = MIMEText("This is an automated email sent using python", 'plain')
message.attach(textPart)
server.send_message(message)