from email.mime.text import MIMEText
import smtplib


def send_email(email, height, average_height, count):
    from_email = "wrobellkatarzyna@gmail.com"
    from_password = "1!WRObelek"
    to_email = email

    subject = "Height data"
    message = "Ciao, your height is <strong>%s</strong> while average height is <strong>%s</strong> calculated out of <strong>%s</strong> people." % (
    height, average_height, count)

    msg = MIMEText(message, 'html')
    msg['Subject'] = subject
    msg['To'] = to_email
    msg['From'] = from_email

    gmail = smtplib.SMTP('smtp.gmail.com', 587)
    gmail.ehlo()
    gmail.starttls()
    gmail.login(from_email, from_password)
    gmail.send_message(msg)
