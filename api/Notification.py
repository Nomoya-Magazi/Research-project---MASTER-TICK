from sendgrid import SendGrid
import os
from sendgrid import SendGridAPIClient
from sendgrid.helpers.mail import Mail

sg_api_key = os.environ.get('SENDGRID_API_KEY')
sg_client = SendGridAPIClient(sg_api_key)

from_email = "mastertick.com"
to_email = "naruto.uzumaki@gmail.com"
subject = "Task reminder"
message = "Hello your task is due!"

email_message = Mail(
    from_email=from_email,
    to_emails=to_email,
    subject=subject,
    html_content=message)

response = sg_client.send(email_message)
