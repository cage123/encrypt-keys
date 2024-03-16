How to change script code for using decrypted keys

Import libs (and dont forget to download cryptography lib by command: pip install cryptography):
from cryptography.fernet import Fernet
from getpass import getpass

Put this code upper some code like this -> account = w3.eth.account.from_key(privatekey):
Dkey = getpass('Input key: ')
FFF = Fernet(Dkey)

And change string which create account from key
account = w3.eth.account.from_key(f.decrypt(privatekey.encode()).decode())

.encode() method converts string -> bytes
.decode() method converts bytes -> string

Fernet supports only bytes
so if U want to use any Fernet methods, arguments should be bytes type
and Fernet methods return information in bytes type
