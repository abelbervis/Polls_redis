import time
from celery import shared_task
import smtplib, ssl
from socket import gaierror

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
    message_status = ''
    try:
        context = ssl.create_default_context()
        with smtplib.SMTP_SSL(smtp_server, port, context=context) as server:
            server.login(sender_email, password)
            server.sendmail(sender_email, receiver_email, message)
        message_status = 'Sent'
    except (gaierror, ConnectionRefusedError):
            message_status = 'Failed to connect to the server. Bad connection settings?'
    except smtplib.SMTPServerDisconnected:
        message_status = 'Failed to connect to the server. Wrong user/password?'
    except smtplib.SMTPException as e:
        message_status = 'SMTP error occurred: ' + str(e)
    
    return message_status
