from controller import Controller

print("Welcome To Main Menu!")
flag = True
while flag:
    print('''\n
    1. Register faculity
    2. Register student
    3. Choose something else''')
    mark = input("Select the number of service which you want to perform ")
    if int(mark) == 1:
        Controller().registerFaculity()
    elif int(mark) == 2:
        print("\n")
        Controller().registerStudent()
    elif int(mark) == 3:
        flag = Controller().Login()
        if flag == True:
            print('''others:
                1.Update faculity
                2.Update student
                3.delete faculity
                4.delete student''')
            choose = input("Enter your choice ")
            if int(choose) == 1:
                print("\n")
                Controller().updateFaculity()
            elif int(choose) == 2:
                print("\n")
                Controller().updateStudent()
            elif int(choose) == 3:
                print("\n")
                Controller().deleteFaculity()
            elif int(choose) == 4:
                print("\n")
                Controller().deleteStudent()
            
        else:
            print("Account does not exist!")
            break
    else:
        print("\nNo such operations are allowed ")
        break