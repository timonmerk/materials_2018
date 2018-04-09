import pickle
import random
import string
def get_credentials():
    username = input('Please type your user name: ')
    password = input('Please type your password: ')
    return username, password

def authenticate(username, password, pwdb):
    status = False
    if username in pwdb:
        if pwdb[username][0] == get_hash(password + pwdb[username][1]):
            status = True
    else:
        ans = input('User not known. Add it to db? [y/n]')
        if ans == 'y':
            add_user(username, password, pwdb)
            status = True
    return status

def add_user(username, password, pwdb):
    if username not in pwdb:
        salt = make_hash_salt(3)
        pwdb[username] = (str(get_hash(password) + str(salt)), str(salt))   #salt should be same for each user
        write_pwdb(pwdb)
    else:
        print('User already known!')

def read_pwdb():
    pwdb_path = get_path()
    try:
        with open(pwdb_path, 'rb') as pwdb_file:
            pwdb = pickle.load(pwdb_file)
    except FileNotFoundError:
        pwdb = {}
    return pwdb

def write_pwdb(pwdb):
    pwdb_path = get_path()
    with open(pwdb_path, 'wb') as pwdb_file:
        pickle.dump(pwdb, pwdb_file)

def get_path():
    return 'pwdb.pkl'

def test_fct():
    print('test')

def get_hash(password): #entered password includes salt
    numerator = 1
    res = 0
    for ch in str(password):
        res += ord(ch)*numerator
        #print('res')
        #print(res)
        #print('ord char')
        #print(ord(ch))
        numerator += 1
    return res

def make_hash_salt(N):
    salt = ''.join(random.choices(string.ascii_uppercase + string.digits, k=N))
    return salt


pwdb = read_pwdb()
username, password = get_credentials()
hash = get_hash(password+make_hash_salt(3))
if authenticate(username, hash, pwdb):
    print(pwdb)
else:
    print('No match!')
