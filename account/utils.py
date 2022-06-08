from django.core.mail import EmailMessage
import os

class Util:
  @staticmethod
  def send_email(data):
    email = EmailMessage(
      subject=data['subject'],
      body=data['body'],
      from_email='suar12358@outlook.com',
      to=[data['to_email']]
    )
    email.send()