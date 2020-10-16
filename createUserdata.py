import names
import random
import string

def make_user():
    emails = ["gmail.com", "gmx.net", "web.de", "yahoo.com", "hotmail.com", "aol.com", "hotmai.co.uk", "hotmail.fr",
              "msn.com", "yahoo.fr", "wanadoo.fr", "orange.fr", "comcast.net", "yahoo.co.uk", "yahoo.com.br",
              "yahoo.co.in", "live.com", "rediffmail.com", "free.fr"]

    email = names.get_full_name().replace(" ", ".") + "@" + random.choice(emails)
    password = ''.join(random.choice(string.ascii_letters + string.digits) for i in range(random.randint(8, 12)))
    print('Mail: ' + email + '  ' + 'Password: ' + password)

def make_mult_users():
    counter: int = int(input('How many datasets do you need? '))
    count: int = 0
    while int(count) < int(counter):
        print(str(count) + ': ')
        make_user()
        count += 1
