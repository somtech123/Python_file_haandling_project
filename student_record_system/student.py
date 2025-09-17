

class Student:
    file_path = 'student_record_system/student_record.txt'

    def __add_student():
        with open(Student.file_path, 'a', encoding='utf-8') as f:
         while True:
            name = input('Enter Student Name (q for quit) \n')
            if name.lower() == 'q':
                break
            student_id = input('Enter student Id\n')
            age = input('Enter student Age\n')
            grade = input('Enter student grade\n')
            f.write(f'{student_id}, {name}, {age}, {grade}\n--------\n')



    def __search_student():
        keyword = input('Enter Student Id to search: ').lower()
        found = False
        try:
           with open(Student.file_path, 'r', encoding='utf-8') as f:
              for entry in f:
                 if entry.startswith(keyword + ","):
                    print('Found:', entry.strip())
                    found = True
                 if not found:
                    print('\n No Student found')
        except FileExistsError:
           print('File not found\n')

    def __view_student():
       try:
          with open(Student.file_path, 'r', encoding='utf-8') as f:
             print('\n Student Records:')
             for line in f:
                print(line.strip())
       except FileNotFoundError:
          print('File not found\n')

    
    def __update_student():
       student_id = input('Enter Student ID to update: ')
       updated = False
       record = []

       with open(Student.file_path, 'r', encoding='utf-8') as f:
          record = f.readlines()
        
       with open(Student.file_path, 'w', encoding='utf-8') as f:
          for line in record:
             if line.startswith(student_id + ','):
                print('Current Record: ', line.strip())
                name = input('Enter new name: ')
                age = input('Enter new Age: ')
                grade = input('Enter new Grade: ')
                f.write(f'{student_id}, {name}, {age}, {grade}\n')
                updated = True
             else:
                f.write(line)
       if updated:
          print('Student updated successfully')
       else: print('Student not founf')

    
    def __delete_student():
       student_id = input('Enter Student ID to delete: ')
       updated = False
       record = []

       with open(Student.file_path, 'r', encoding='utf-8') as f:
          record = f.readlines()
        
       with open(Student.file_path, 'w', encoding='utf-8') as f:
          for line in record:
             if line.startswith(student_id + ','):
                updated = True
                continue
             f.write(line)
       if updated:
          print('Student deleted successfully')
       else: print('Student not founf')


    def run(self):
       
        while True:
            print('\n Student Record System')
            print('1. Add Student')
            print('2. View All Student')
            print('3. Search Student by Id')
            print('4. Update Student by ID')
            print('5. Delete student by ID')
            print('6. Exit')

            choice = input('Choose an option: ')

            if choice == '1': Student.__add_student()
            elif choice == '2' : Student.__view_student()
            elif choice == '3': Student.__search_student()
            elif choice == '4': Student.__update_student()
            elif choice == '5': Student.__delete_student()
            elif choice == '6':
                print('Goodbye!')
                break
            else: print('Invali choice, try again')
                 
       


