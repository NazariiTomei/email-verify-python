# See https://pypi.org/project/email-validator/
from email_validator import validate_email, EmailNotValidError

email = input('Input email: ')

# Step 1
# Email Syntax & domain availability test

try:

  emailinfo = validate_email(email) # check_deliverability=False
  email = emailinfo.normalized

except EmailNotValidError as e:

  print(str(e))

# Step 2
# Use email verification apis

# 1) CaptainVerify
# See https://dashboard.captainverify.com/api-v2.html
