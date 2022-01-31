import time
from celery import shared_task
import smtplib, ssl

port = 465  # For SSL
smtp_server = "smtp.gmail.com"
#sender_email = "abel.kyojin2@gmail.com"  # Enter your address
#receiver_email = "abel.bervis.quintero@gmail.com"  # Enter receiver address
#password = "mipassword"
sending_message = False
#message = """\
#Subject: Hi there
#
#This message is sent from Python."""

@shared_task
def task_send_mail(sender_email,password,receiver_email,message):
    print('waiting 10 seconds...')
    time.sleep(10)
    try:
        context = ssl.create_default_context()
        with smtplib.SMTP_SSL(smtp_server, port, context=context) as server:
            server.login(sender_email, password)
            server.sendmail(sender_email, receiver_email, message)
        sending_message = True
        print('message sent')
    except Exception as e:
        print(e)
        sending_message = False
        print('message not sent')
    return sending_message