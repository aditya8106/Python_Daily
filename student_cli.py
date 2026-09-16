students = [
    {"id": 1, "name": "Aditya", "marks": 85},
    {"id": 2, "name": "Rahul", "marks": 72},
    {"id": 3, "name": "Priya", "marks": 91},
    {"id": 4, "name": "Kiran", "marks": 68},
    {"id": 5, "name": "Kiran", "marks": 68}

     
]
def View_stds():
  for std in students:
    print('list of the studeents')
    print('ID:',std['id'], '| Name:',std['name'],'| marks :',std['marks'])

def Search_stds():
  try:
    search = int(input('enter Id for Search'));
    for std in students:
      if std['id'] == search:
        print('\n Student Founded')
        print('ID:',std['id'], '| Name:',std['name'],'| marks :',std['marks'])
        return
    print('stdent not found');
  except ValueError:
    print('enter valid ID')

def Insert_student():
  try:
    Id = int(input('Enter  ID'))
    name = input('enter name of student')
    marks = int(input('enter Student marks'))
    New_std =  {
       'id':Id,
       'name':name,
       'marks':marks
     }
    students.append(New_std);
    print(students)
    print('studnet inserted successfuly')
  except ValueError:
    print('enter a valid Input')
def delete_std():
  try:
    Id = int(input('enter Id to  delete'))
    for std in students:
      if std['id'] == Id:
        students.remove(std)
        print(students)
        print('student removed successfully !')
  except ValueError:
    print('enter valid Id type')
def Update_std():
  try:
    id  = int(input('enter id to uodate'))
    for std in students:
      if std['id'] == id:
        new_name = input('enter name to update')
        new_Marks = int(input('enter marks to update'))
        std['name'] = new_name
        std['marks'] = new_Marks
        print(students)
        print('student updated')
    print('not fount')
  except ValueError:
    print('enter valid input')
while True:
    print("\n===== Student Management System =====")
    print("1. View students")
    print("2. Search student")
    print("3. Add student")
    print("4. Delete student")
    print("5. Update student")
    print("6. Exit")

    choice = input('enter your choice')
    if choice == '1':
      View_stds()
    elif choice == '2':
      Search_stds()
    elif choice == '3':
      Insert_student()
    elif choice == '4':
      delete_std()
    elif choice == '5':
      Update_std()
    elif choice == '6':
      break