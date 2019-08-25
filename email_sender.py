import smtplib, ssl
from email.mime.text import MIMEText
from datetime import date
import smtplib
import re



def send_email(sender,reciever,password,email_subject,message):
    smtp_server = "smtp.gmail.com"
    smtp_port = 587
    smtp_username = sender
    smtp_password = password

    email_to = [reciever]
    email_from = sender
    date_format = "%d/%m/%Y"
    email_space = ", "

    data = message

    msg = MIMEText(data)
    msg['Subject'] = email_subject + " %s" % (date.today().strftime(date_format))
    msg['To'] = email_space.join(email_to)
    msg['From'] = email_from
    mail = smtplib.SMTP(smtp_server, smtp_port)
    mail.starttls()
    try:
        mail.login(smtp_username, smtp_password)
        mail.sendmail(email_from, email_to, msg.as_string())
        mail.quit()
        return(True)
    except:
        return(False)
