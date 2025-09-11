from datetime import datetime

from auth import Auth

class DiaryApp:
    file_path = 'simple_diary_app/diary.txt'

    auth = Auth()

    def __init__(self):
        pass

    def __add_entry():
        entry = input('Write your diary entry\n ')
        timestamp = datetime.now().strftime("%y-%m-%d %H:%M")
    
        with open(DiaryApp.file_path, 'a', encoding='utf-8') as f:
            f.write(f'{timestamp}\n{entry}\n---\n')
        print('Entry saved successfully!\n')

    def __view_entry():
        try:
            with open(DiaryApp.file_path, 'r', encoding='utf-8') as f:
                content = f.read()
                if content.strip() == "":
                    print('Diary is empty.\n')
                else:
                    print('\n Your diary:\n')
                    print(content)

        except FileNotFoundError:
            print('no diary file found, start by adding an entry\n')

    
    def __search_entries():
        keyword = input('Enter a keyword or date (YYYY-MM-DD): ').lower()

        try:
            with open(DiaryApp.file_path, 'r', encoding='utf-8') as f:
                entries = f.read().split('---\n')
                found = False
                for entry in entries:
                    if keyword in entry.lower():
                        print('\nFound Entry\n')
                        print(entry.strip())
                        found = True
                if not found:
                    print('No matching entry found.\n')

        except FileNotFoundError:
            print('No Diary file found.\n')


    def run(self):
        DiaryApp.auth.check_password()

        
        while True:
            print('\n Simple Diary app')
            print('1. Add Entry')
            print('2. View Entries')
            print('3. Search Entries')
            print('4. Exit')

            choice = input('Choose an option: ')

            if choice == '1': DiaryApp.__add_entry()
            elif choice == '2' : DiaryApp.__view_entry()
            elif choice == '3': DiaryApp.__search_entries()
            elif choice == '4':
                print('Goodbye!')
                break
            else: print('Invali choice, try again')

        