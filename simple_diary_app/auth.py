
import hashlib
import os

class Auth:

    password_path = 'simple_diary_app/auth.txt'

    def __hashPassword(password: str)-> str:
        return hashlib.sha256(password.encode()).hexdigest()
    
    def __set_password():
        password = input('Set a new password\n')

        hashed = Auth.__hashPassword(password)

        with open(Auth.password_path, 'w', encoding='utf-8') as f:
            f.write(hashed)
        print('Password set successfully\n')

    def check_password(self):
        if not os.path.exists(Auth.password_path):
            Auth.__set_password()

        with open(Auth.password_path, 'r', encoding='utf-8') as f:
            saved_hashed = f.read().strip()

        entered = input('Enter your diary password\n')

        entered_hashed = Auth.__hashPassword(entered)

        if entered_hashed != saved_hashed:
            print('Wrong password access denied')
            exit()
        else:
            print('Access granted')

