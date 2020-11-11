from interfaces.interface import SendEmail
import smtplib
from email.mime.text import MIMEText
from confidential import SUPPORT_MAIL, SUPPORT_MAIL_PASS
import datetime
from utils import common_constants


class NotificationUtils(SendEmail):

    def send_mail(self):
        print(f"=== === Preparing to send mail === === to: {self.user_email} ")
        message_list = self.custom_message
        mail_content = "| |".join(message_list)
        body = """\
<html>
  <head></head>
  <body>
    <p>Hi!<br>
       Here is your Alert !<br>
      """ + mail_content + """
    </p>
  </body>
</html>
"""
        try:
            s = smtplib.SMTP('smtp.gmail.com', 587)
            msg = MIMEText(body, 'html')
            msg['Subject'] = "STOCK--ALERT !!"
            msg['From'] = SUPPORT_MAIL
            msg['To'] = self.user_email
            s.starttls()
            s.login(SUPPORT_MAIL, SUPPORT_MAIL_PASS)
            s.sendmail(SUPPORT_MAIL, self.user_email, msg.as_string())
            s.quit()
            print(f"Notified successfully at: {datetime.datetime.now()} ")
        except ConnectionError:
            print("error in connecting to SMTP server")
            pass
