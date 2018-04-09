def get_credentials():
    username = input('Please type your user name: ')
    password = input('Please type your password: ')
    return username, password

def authenticate(username, password, pwdb):
    if username in pwdb:
        if pwdb[username] == password:
            return True
    return False

pwdb = {'tiziano': 'right_password'}
username, password = get_credentials()
if authenticate(username, password, pwdb):
    print('Match!')
else:
    print('No match!')

