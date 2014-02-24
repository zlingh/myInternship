import smtplib,email,os,sys
from email.MIMEBase import MIMEBase
from email.MIMEText import MIMEText
from email.MIMEMultipart import MIMEMultipart
from email import Encoders
from email.header import Header

from optparse import OptionParser

default_sender = 'zhangping@umeng.com'
default_receiver = 'zhangping@umeng.com'
default_password = 'zhang9ping'

parser = OptionParser()
parser.add_option('-s', '--sender', dest='sender', default=default_sender, help=u'sender')
parser.add_option('-p', '--password', dest='password', default=default_password, help=u'senderp')
parser.add_option('-r', '--receiver', dest='receiver', default=default_receiver, help=u'reciver')
parser.add_option('-t', '--title', dest='title', help=u'head')
parser.add_option('-m', '--message', dest='message', default='hello world', help=u'head')
parser.add_option('-a', '--attachment', dest='attachment', help=u'attch')
(options, args) = parser.parse_args()    

mail_server = 'smtp.gmail.com'
mail_server_port = 587

from_addr = options.sender
password = options.password
to_addr = options.receiver
title = options.title
message = options.message
attachment = None
if options.attachment:
    attachment = options.attachment

msg = MIMEMultipart()

msg['From'] = from_addr
msg['To'] = str(to_addr)
msg['Subject'] = Header(title, 'utf8')
msg['Reply-To'] = from_addr
print msg.as_string()

email_message = message

msg.attach(MIMEText(email_message))

if attachment:
     
    fp = open(attachment, 'rb')
    part = MIMEBase('application', "octet-stream")
    part.set_payload(fp.read())
    fp.close()
    Encoders.encode_base64(part)
    part.add_header('Content-Disposition', 'attachment; filename="%s"' % attachment)
    msg.attach(part)

s = smtplib.SMTP(mail_server, mail_server_port)
#s.set_debuglevel(1)
s.ehlo()
s.starttls()
s.login(from_addr, password)
s.sendmail(from_addr, to_addr, msg.as_string())
s.quit()
