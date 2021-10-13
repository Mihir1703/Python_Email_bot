import json
import smtplib
server = smtplib.SMTP('smtp.gmail.com',587)
server.starttls()

def getEmailInfo():
    return json.load(open('./email-config.json'))
def getSenderInfo():
    return json.load(open('./Send/email.json'))
def sendMail():
    info = getEmailInfo()
    sender = getSenderInfo()
    server.login(info['mail'],info['password']) 
    server.sendmail(info['mail'],sender['mail'],sender['message'])

for i in range (20):
    sendMail()