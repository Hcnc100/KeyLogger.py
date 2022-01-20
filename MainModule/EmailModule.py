import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

FROM = "From"
TO = "To"
SUBJECT = "Subject"
SERVER_GMAIL = "smtp.gmail.com:587"


def send_content_file(file_name, email, passwd, subject):
    msg = MIMEMultipart()
    msg[FROM] = email
    msg[TO] = email
    msg[SUBJECT] = subject
    read_file(file_name)
    msg.attach(MIMEText(read_file(file_name)))
    server = smtplib.SMTP(SERVER_GMAIL)
    server.starttls()
    server.login(email, passwd)
    server.sendmail(msg[FROM], msg[TO], msg.as_string())


def read_file(file_name):
    file = open(file_name, "r")
    content = file.read()
    file.close()
    return content
