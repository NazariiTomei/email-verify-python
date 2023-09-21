import requests
from email_syntax_domain_availability import checkEmailSyntax

GOOD = 'Good' # valid
WRONGFORMAT = 'Wrong format' # basic format check of an email account
DISABLE = 'Disable' # this mail is disabled during login
VERIFY = 'Verify' # this mail is asking for phone number during login
NOTEXIST = 'Not exist' # user is already deleted from the mail server or not register yet

def validate(email):
  systaxResult = checkEmailSyntax(email);
  if systaxResult != True:
    return WRONGFORMAT
