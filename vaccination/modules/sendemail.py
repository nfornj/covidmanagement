import time
import smtplib , ssl
from smtplib import SMTP
import datetime


def sendemail(result_data):
    smtp_server = "smtp.gmail.com"
    port = 587  # For starttls
    sender_email = "nfornj@gmail.com"
    password = "aquxsvctyqeepvzc"

    # Create a secure SSL context
    context = ssl.create_default_context()

    server = smtplib.SMTP(smtp_server, port)

    # Try to log in to server and send email
    try:
        server = smtplib.SMTP(smtp_server, port)
        server.ehlo() # Can be omitted
        server.starttls(context=context) # Secure the connection
        server.ehlo() # Can be omitted
        server.login(sender_email, password)

        message = 'Subject: {}\n\n{}'.format("Vaccine Available at Ernakulam "+str(datetime.datetime.now()), result_data)

        server.sendmail(sender_email, ["narayananv1965@gmail.com","nfornj@gmail.com"], message)
        server.quit()
        # TODO: Send email here
    except smtplib.SMTPException as e:
        # Print any error messages to stdout
        print(e)
        pass