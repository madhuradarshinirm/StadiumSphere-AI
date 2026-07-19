import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText


# YOUR GMAIL
EMAIL = "YOUR_GMAIL@gmail.com"

# Gmail App Password (16 characters)
PASSWORD = "YOUR_APP_PASSWORD"


def send_ticket_email(receiver, ticket):

    subject = "🎟 StadiumSphere AI - Ticket Confirmation"

    body = f"""
Hello {ticket['Name']},

Thank you for booking with StadiumSphere AI!

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

🎟 Ticket ID : {ticket['Ticket ID']}

⚽ Match : {ticket['Match']}

🏟 Stadium : {ticket['Stadium']}

📅 Date : {ticket['Date']}

⏰ Time : {ticket['Time']}

💺 Category : {ticket['Category']}

👥 Tickets : {ticket['Tickets']}

💰 Amount : ₹{ticket['Amount']}

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

Please arrive 60 minutes before kickoff.

Carry your ID proof.

Show your QR Ticket at the stadium entrance.

Enjoy the FIFA World Cup!

Team StadiumSphere AI ❤️
"""

    message = MIMEMultipart()

    message["From"] = EMAIL
    message["To"] = receiver
    message["Subject"] = subject

    message.attach(MIMEText(body, "plain"))

    server = smtplib.SMTP("smtp.gmail.com", 587)

    server.starttls()

    server.login(EMAIL, PASSWORD)

    server.sendmail(
        EMAIL,
        receiver,
        message.as_string()
    )

    server.quit()