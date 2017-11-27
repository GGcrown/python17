# Auhtor:Crown
import getpass #引入模块

_username="Crown"
_password="123"



username = input("username:")
#password = getpass.getpass("password");
password  = input("password:")

if _username==username and _password==password:
    print('Welcome user {name} login'.format(name=username))
else:
    print('Invalid username or password')


''''''