from user import user
from faculity import faculity
from student import student
from model import dbHandler
import model
class invalidPassword(Exception):
    pass

dbh = dbHandler("localhost", "root", "Bb22092001@#", "fcit")

class Controller:
    def passwordcheck(self, password):
        flag = True
        try:
            if len(password) < 4:
                raise invalidPassword("Password must contain atleast 4 digits")
        except invalidPassword as e:
            print(str(e))
            flag = False
        return flag

    def Login(self):
        username = input("Enter username ")
        password = input("Password ")
        flag = dbh.authenticateUser(username, password)
        return flag

    def registerFaculity(self):
        username = input("Enter username ")
        password = input("Enter your password ")
        flag = self.passwordcheck(password)
        while flag == False:
            password = input('''
            Invalid password!
            Enter password again''')
            flag = self.passwordcheck(password)
        fid=input("Enter faculity_id")
        user_id=input("Enter user_id")
        designation = input("At what designation you are working ")
        subject = input("Enter your subject ")
        f = faculity(fid,designation, subject,user_id, username, password)
        dbh.register_faculity(f)

    def registerStudent(self):
        username = input("Enter username ")
        password = input("Enter your password ")
        flag = self.passwordcheck(password)
        while flag == False:
            password = input('''
            Invalid password!
            Enter password again''')
            flag = self.passwordcheck(password)
        sid = input("Enter your student_id")
        semester = input("Enter your current semester ")
        cgpa = input("Enter your cgpa ")
        major = input("Enter your majors ")
        user_id=input("Enter user_id")
        s = student(sid,semester, cgpa, major,user_id, username, password)
        dbh.register_student(s)

    def updateFaculity(self):
        newDesignation = input("Enter the new designation ")
        newSubject = input("Enter the new subject ")
        fid = int(input("Enter the id of faculity "))
        dbh.update_faculity(fid, newSubject, newDesignation)

    def updateStudent(self):
        newSemester = input("\nEnter the new semester ")
        newCgpa = input("Enter the new cgpa ")
        sid = input("Enter the id of student ")
        dbh.update_student(sid, newSemester, newCgpa)

    def deleteStudent(self):
        sid = input("Enter the id of student you want to delete ")
        dbh.delete_student(sid)

    def deleteFaculity(self):
        fid = input("Enter the id of faculty you want to delete ")
        dbh.delete_faculity(fid)

    