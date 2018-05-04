import smtplib

EMAIL_ADDRESS = "samer.elhamdoo@hotmail.com"
passs = "dhfjdegsjrft"
PASSWORDS = []
x = int(input("enter number: "))
t = x/2
while x > 0:
    result = x
    PASSWORDS.append(passs)
    x -= 1
    if x < t:
        PASSWORDS.append("samerbilal1990")
        result = 0


def send_email(subject, msg):
    for PASSWORD in PASSWORDS:


        try:
            server = smtplib.SMTP('smtp.live.com', 587)
            server.ehlo()
            server.starttls()
            server.login(EMAIL_ADDRESS, PASSWORD)
            message = 'Subject: {}\n\n{}'.format(subject, msg)
            #server.sendmail(EMAIL_ADDRESS, EMAIL_ADDRESS, message)
            stars_text = "*"*len(PASSWORD[1:-1])
            star_password = PASSWORD[0] + stars_text + PASSWORD[-1]
            print("the password is: {}".format(star_password))
            server.quit()
        except:
            print("Filed Password is: {}".format(PASSWORD))


subject = "Test subject"
msg = "Hello there, how are you today?"

send_email(subject, msg)