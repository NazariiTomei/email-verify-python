# See https://pypi.org/project/email-validator/
from email_validator import validate_email, EmailNotValidError

# Email Syntax & domain availability test
def checkEmailSyntax(email):
  try:
    validate_email(email) # check_deliverability=False
    return True
  except EmailNotValidError as e:
    return (False, str(e))
