#mail
from flask_mail import Mail, Message

#app
from app import app

#other imports
from os import getenv

#basic mail + config for mail app
mailSender="schoologycalendar@gmail.com"
mail = Mail(app)

class eMail:
    #A simple mail class application
    def __init__(self):
        self.msg = Message("", sender=mailSender,recipients=[])
        
        #recipients
        self.recipients=[]
        #header
        self.head=""
        #body
        self.body=""
    
    #attaching stuff to email
    def attach(self,name,fType,fPath):
        with app.open_resource(fPath) as fp:
            msg.attach(name, fType, fp.read())
            
    #sending mail
    def send(self):
        self.msg.head=self.head
        self.msg.body=self.body
        self.msg.recipients=self.recipients
        mail.send(self.msg)