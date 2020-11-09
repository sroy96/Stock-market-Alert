from interfaces.interface import SendEmail
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders
from confidential import SUPPORT_MAIL, SUPPORT_MAIL_PASS
from utils import common_constants


class NotificationUtils(SendEmail):

    def send_mail(self):
        print(f"=== === Preparing to send mail === === to: {self.user_email} ")
        message_list = self.custom_message
        mail_content = "| |".join(message_list)
        try:
            s = smtplib.SMTP('smtp.gmail.com', 587)
            s.starttls()
            s.login(SUPPORT_MAIL, SUPPORT_MAIL_PASS)
            s.sendmail(SUPPORT_MAIL, self.user_email, mail_content)
            s.quit()
            print("mail sent")
        except ConnectionError:
            print("error in connecting to SMTP server")


        # message = MIMEMultipart()
        # message['From'] = SUPPORT_MAIL
        # message['To'] = self.user_email
        # message['Subject'] = "YOUR STOCK ALERTS !! "
        # # The body and the attachments for the mail
        # message.attach(MIMEText(mail_content, 'plain'))
        # # Create SMTP session for sending the mail
        # session = smtplib.SMTP('smtp.gmail.com', 587)  # use gmail with port
        # session.starttls()  # enable security
        # session.login(SUPPORT_MAIL, SUPPORT_MAIL_PASS)  # login with mail_id and password
        # text = message[0].as_string()
        # session.sendmail(SUPPORT_MAIL, self.user_email, text)
        # session.quit()
        # print(f"Mail Sent to {self.user_email}")
