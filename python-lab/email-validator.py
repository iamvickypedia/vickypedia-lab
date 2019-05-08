def check_email(s):
    try:
        username,url = s.split('@')
        website,ext = url.split('.')
    except ValueError:
        return False

    if not username.replace('-','').replace('_','').isalnum():
        return False
    if not website.isalnum():
        return False
    if len(ext) < 1 or len(ext) > 3:
        return False
    return True

print('This program checks the string to validate whether it is a valid email or not')
em = input('Enter email address to check validity\n')

if check_email(em):
    print('{} is a valid email address'.format(em))
else:
    print('{} is not a valid email address'.format(em))

