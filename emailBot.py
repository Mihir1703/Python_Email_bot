import json
import smtplib

def getEmailInfo():
    return json.load(open('email-config.json'))
def getSenderInfo():
    return json.load(open('./Send/email.json'))

server = smtplib.SMTP('smtp.gmail.com',587)
server.starttls()
info = getEmailInfo()
sender = getSenderInfo()
server.login(info['mail'],info['password']) 
server.sendmail(info['mail'],sender['mail'],sender['message'])