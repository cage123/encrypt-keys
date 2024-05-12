from cryptography.fernet import Fernet
from web3 import Web3
from getpass import getpass

# How to change script code for using decrypted keys

# Import libs (and dont forget to download cryptography lib by command: pip install cryptography):
# from cryptography.fernet import Fernet
# from getpass import getpass

# Put this code upper some code like this -> account = w3.eth.account.from_key(privatekey):
# Dkey = getpass('Input key: ')
# FFF = Fernet(Dkey)

# And change string which create account from key
# account = w3.eth.account.from_key(f.decrypt(privatekey.encode()).decode())



# .encode() method converts string -> bytes
# .decode() method converts bytes -> string

# Fernet supports only bytes
# so if U want to use any Fernet methods, arguments should be bytes type
# and Fernet methods return information in bytes type


if __name__ == '__main__':
    mode = input('Input mode (1 - generate, 2 - get addresses, 3 - get keys): ')
    if mode == '1':
        key = Fernet.generate_key()
        f = Fernet(key)
        print(f'Generated key: {key.decode()}')
        with open('key.txt', 'w') as file_key:
            file_key.write(key.decode())
            file_key.close()
        
        with open('privatekeys.txt', 'r') as file_keys:
            data = file_keys.read().splitlines()
            file_keys.close()
        
        # To clear contents of file
        with open('encrypted_keys.txt', 'w') as file_result:
            file_result.close()
        
        for privatekey in data:
            privatekey = f.encrypt(privatekey.encode())
            with open('encrypted_keys.txt', 'a') as file_result:
                file_result.write(f'{privatekey.decode()}\n')
                file_result.close()
        
        print(f'\n{len(data)} wallets successfully encrypted\nEncrypted privatekeys in encrypted_keys.txt\nDecrypt key in key.txt')
    elif mode == '2':
        w3 = Web3()
        key = getpass('Input key: ')
        f = Fernet(key.encode())
        
        with open('encrypted_keys.txt', 'r') as file:
            data = file.read().splitlines()
            file.close()
        
        print('\nAddresses encrypted wallets:')
        for privatekey in data:
            account = w3.eth.account.from_key(f.decrypt(privatekey.encode()).decode())
            print(account.address)
    elif mode == '3':
        key = getpass('Input key: ')
        f = Fernet(key.encode())
        
        with open('encrypted_keys.txt', 'r') as file:
            data = file.read().splitlines()
            file.close()
        
        print('\nPrivate keys:')
        for privatekey in data:
            print(f.decrypt(privatekey.encode()).decode())
    
    input()