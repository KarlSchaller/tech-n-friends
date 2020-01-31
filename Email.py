
import smtplib

# =============================================================================
# SET EMAIL LOGIN REQUIREMENTS
# =============================================================================
gmail_user = 'hackingtemplecanvas@gmail.com'
gmail_app_password = '123Password'

# =============================================================================
# SET THE INFO ABOUT THE SAID EMAIL
# =============================================================================
sent_from = gmail_user
sent_to = ['tuf08803@temple.edu']
sent_subject = "Where are all my Robot Women at?"
sent_body = ("Hey, what's up? friend!\n\n"
             "I hope you have been well!\n"
             "\n"
             "Here is our slack please join!!"
            "https://hackingtemplecanvas.slack.com/"
              "\n"
             "Cheers,\n"
             "Jay\n")

email_text = """\
From: %s
To: %s
Subject: %s

%s
""" % (sent_from, ", ".join(sent_to), sent_subject, sent_body)

# =============================================================================
# SEND EMAIL OR DIE TRYING!!!
# Details: http://www.samlogic.net/articles/smtp-commands-reference.htm
# =============================================================================

try:
    server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
    server.ehlo()
    server.login(gmail_user, gmail_app_password)
    server.sendmail(sent_from, sent_to, email_text)
    server.close()

    print('Email sent!')
except Exception as exception:
    print("Error: %s!\n\n" % exception)