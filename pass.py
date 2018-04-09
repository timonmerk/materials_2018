def get_credentials():
    username = input('Please type your user name: ')
    password = input('Please type your password: ')
    return username, password

def authenticate(username, password, pwdb):
    status = False
    if username in pwdb:
        if pwdb[username] == password:
            status = True
    else:
        add_user(username, password, pwdb)
        status = True
    return status

def add_user(username, password, pwdb):
    if username not in pwdb:
        pwdb[username] = password
    else:
        print('User already known!')

pwdb = {}

username, password = get_credentials()
if authenticate(username, password, pwdb):
    print('Match!')
else:
    print('No match!')

