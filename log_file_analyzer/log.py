class Log:
    file_path = 'log_file_analyzer\log.txt'

    def run(self):
        """Main menu system"""
        while True:
            print("\n📊 Log File Analyzer")
            print("1. View all logs")
            print("2. Count errors")
            print("3. Count logins")
            print("4. Search by keyword")
            print("5. Exit")

            choice = input("Choose an option: ")

            if choice == "1": Log.__view_log()
            elif choice == "2":  Log.__count_error()
         
            elif choice == "3":Log.__count_login()
            
            elif choice == "4": Log.__search_keyword()
            
            elif choice == "5": 
                print("Goodbye!")
                break
            else:
              print("Invalid choice, try again.")



    def __view_log():
        """Display all logs"""
        try:
            with open(Log.file_path, 'r', encoding='utf-8') as f:
                print('\n Log File Content')
                for line in f:
                    print(line.strip())
        except FileNotFoundError:
            print('No log file found')

    
    def __count_login():
         """Count all login events and group by user"""
         users, login_count ={}, 0

         with open(Log.file_path, 'r', encoding='utf-8') as f:
             for line in f:
                 if "logged in" in line:
                     login_count += 1
                     user = line.split()[-2] #extract username
                     users[user] = users.get(user, 0) + 1

         print(f"\n👥 Total Logins: {login_count}")
         print("Login Count by User:", users)

    def __count_error():
        """Count all ERROR entries"""
        error_count =0

        with open(Log.file_path, 'r', encoding='utf-8') as f:
             for line in f:
                 if "ERROR" in line:
                     error_count += 1
        print(f"\n Total Errors: {error_count}")
                     
   
    def __search_keyword():
        keyword = input('Enter Keyword to search')
        found = False
        with open(Log.file_path, 'r', encoding='utf-8') as f:
            for line in f:
               if keyword.lower() in line.lower():
                  print("👉", line.strip())
                  found = True
        if not found:
            print("No matches found.")

        





    