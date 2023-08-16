import pymysql
from contact import Contact


class dbHandler:
    def __init__(self, host, user, passd, database):
        self.host = host
        self.user = user
        self.passwd = passd
        self.db = database

    def insertContact(self, contactObj):
        dbConnect = None
        curObj = None
        try:
            dbConnect = pymysql.connect(host=self.host, user=self.user, passwd=self.passwd, db=self.db)
            curObj = dbConnect.cursor()
            sqlQuery = "Insert into contacts(name,mobileno,city,profession) values(%s,%s,%s,%s)"
            agrc = (contactObj.name, contactObj.mobileNo, contactObj.city, contactObj.profession)
            curObj.execute(sqlQuery, agrc)
            dbConnect.commit()
        except Exception as e:
            print(e)
        finally:
            if dbConnect != None:
                dbConnect.close()

    def showAllContacts(self):
        dbConnect = None
        curObj = None

        try:
            dbConnect = pymysql.connect(host=self.host, user=self.user, passwd=self.passwd, db=self.db)
            curObj = dbConnect.cursor()
            sqlQuery = """Select * from contacts"""
            curObj.execute(sqlQuery)
            result = curObj.fetchall()
        except Exception as e:
            print(e)
        finally:
            if dbConnect != None:
                dbConnect.close()
        return result

    def showContactbyName(self, name):
        dbConnect = None
        curObj = None
        try:
            dbConnect = pymysql.connect(host=self.host, user=self.user, passwd=self.passwd, db=self.db)
            curObj = dbConnect.cursor()
            sqlQuery = """Select * from contacts
            where name = %s"""
            argc = (name)
            curObj.execute(sqlQuery, argc)
            result = curObj.fetchall()
        except Exception as e:
            print(e)
        finally:
            if dbConnect != None:
                dbConnect.close()
        return result

