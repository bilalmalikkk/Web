from contact import Contact
from db import dbHandler

db = dbHandler("localhost", "root", "Bb22092001@#", "fcit")


def add_Contact(contact):
    db.insertContact(contact)


def show_contacts():
    return db.showAllContacts()


def show_contact_name(name):
    return db.showContactbyName(name)


def isValidate(c):
    flag = False
    num = c.MobileNo
    if (num.isnumeric()):
        for i in num:
            if (i == '+' or i <= '9'):
                flag = True
            else:
                return False
    else:
        return False

    return flag
