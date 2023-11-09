import smtplib


To = input("Enter the Email Address of Recipent---> ")
Content = input("Enter the body for Mail---> \n")

def sendMail(To,Content):

    server = smtplib.SMTP('smtp.gmail.com',587)
    server.ehlo()
    server.starttls()
    server.login('SenderEmail','Pass')
    server.sendmail('SenderEmail',To,Content)
    server.close()

sendMail(To,Content)

