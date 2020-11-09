from interfaces.interface import SendEmail
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from confidential import SUPPORT_MAIL, SUPPORT_MAIL_PASS
from utils import common_constants


class NotificationUtils(SendEmail):

    def send_mail(self):
        print("=== === Preparing to send mail === === ")
        message_list = self.custom_message
        mail_content = "| |".join(message_list)
        message = MIMEMultipart()
        message['From'] = SUPPORT_MAIL
        message['To'] = self.user_email
        message['Subject'] = "YOUR STOCK ALERTS !! "
        # The body and the attachments for the mail
        message.attach(MIMEText(mail_content, 'plain'))
        # Create SMTP session for sending the mail
        session = smtplib.SMTP('smtp.gmail.com', 587)  # use gmail with port
        session.starttls()  # enable security
        session.login(SUPPORT_MAIL, SUPPORT_MAIL_PASS)  # login with mail_id and password
        text = message.as_string()
        session.sendmail(SUPPORT_MAIL, self.user_email, text)
        session.quit()
        print(f"Mail Sent to {self.user_email}")
