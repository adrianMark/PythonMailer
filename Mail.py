import sys, smtplib, os
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email.mime.text import MIMEText
from email.utils import formatdate
from email.encoders import *


class SendMail(object):
  mailadress = 'myaddress' #EDIT
  smtpserver = 'smtp.web.de'
  username = 'uname'#EDIT
  password = 'pw' #EDIT

  def send(self, files):
    to = "address" #EDIT
    From = self.mailadress
    subject = 'Bewegung aufgezeichnet!' 
    msg = self.prepareMail(From, to, subject, files)

    #Connect to server and send mail
    server = smtplib.SMTP(self.smtpserver)
    server.ehlo() 
    server.starttls() 
    server.ehlo() 
    server.login(self.username, self.password)
    failed = server.sendmail(From, to, msg.as_string())
    server.quit()

  def prepareMail(self, From, to, subject, attachments):
    msg = MIMEMultipart()
    msg['From'] = From
    msg['To'] = to
    msg['Date'] = formatdate(localtime=True)
    msg['Subject'] = subject

    msg.attach( MIMEText("Die Alarmanlage hat eine Bewegung aufgezeichnet: \n"))

    for file in attachments:
      part = MIMEBase('application', "octet-stream")
      part.set_payload( open(file,"rb").read() )
      encode_base64(part)
      part.add_header('Content-Disposition', 'attachment; filename="%s"' % os.path.basename(file))
      msg.attach(part)
    return msg

if __name__ == '__main__':
    mail = SendMail()
    mail.send(["file1"]) #EDIT
