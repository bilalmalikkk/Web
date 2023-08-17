import pymysql
from user import user
from faculity import faculity
from student import student
class dbHandler:
    def __init__(self,host,user,password,database):
        self.host=host
        self.user=user
        self.password=password
        self.database=database

    def register_user(self,id,username,password):
        try:
            mydb=None
            mydb=pymysql.connect(host=self.host,user=self.user,password=self.password,database=self.database)
            mydbcursor=mydb.cursor()

            sql="insert into user values (%s,%s,%s)"
            args = (id,username,password)
            mydbcursor.execute(sql, args)

        except Exception as e:
            print(str(e))
        finally:
            mydb.commit()
            if mydbcursor !=None:
                mydbcursor.close()
            if mydb !=None:
                mydb.close()

    def register_faculity(self,f):
        try:
            mydb=None
            mydb=pymysql.connect(host=self.host,user=self.user,password=self.password,database=self.database)
            mydbcursor=mydb.cursor()

            sql="insert into faculity values (%s,%s,%s,%s)"
            args = (f.fid,f.designation,f.subject,f.user_id)
            mydbcursor.execute(sql, args)

        except Exception as e:
            print(str(e))
        finally:
            mydb.commit()
            if mydbcursor !=None:
                mydbcursor.close()
            if mydb !=None:
                mydb.close()

    def register_student(self,s):

        mydb=None
        mydbcursor = None
        try:
            mydb=pymysql.connect(host=self.host,user=self.user,password=self.password,database=self.database)
            mydbcursor=mydb.cursor()
            sql="insert into student values (%s,%s,%s,%s, %s)"
            args = (s.sid, s.semester, s.cgpa, s.major, s.user_id)
            mydbcursor.execute(sql, args)

        except Exception as e:
            print(str(e))
        finally:
            mydb.commit()
            if mydbcursor !=None:
                mydbcursor.close()
            if mydb !=None:
                mydb.close()

    def getUserId(self,username,password):
        try:
            mydb=None
            mydb=pymysql.connect(host=self.host,user=self.user,password=self.password,database=self.database)
            mydbcursor=mydb.cursor()

            sql="select username, password from user where id=%s "
            args = (username,password)
            mydbcursor.execute(sql, args)
            mydbcursor.fetchall()

        except Exception as e:
            print(str(e))
        finally:
            mydb.commit()
            if mydbcursor !=None:
                mydbcursor.close()
            if mydb !=None:
                mydb.close()

    def get_faculity(self):
        try:
            mydb=None
            mydb=pymysql.connect(host=self.host,user=self.user,password=self.password,database=self.database)
            mydbcursor=mydb.cursor()
            sql="select * from faculity where user_id =%s "
            args = (self.getUserId())
            mydbcursor.execute(sql, args)
            mydbcursor.fetchall()

        except Exception as e:
            print(str(e))
        finally:
            mydb.commit()
            if mydbcursor !=None:
                mydbcursor.close()
            if mydb !=None:
                mydb.close()
    
    def get_student(self,username,password):
        try:
            mydb=None
            mydb=pymysql.connect(host=self.host,user=self.user,password=self.password,database=self.database)
            mydbcursor=mydb.cursor()

            sql="select id from user where username=%s AND password=%s"
            args = (username,password)
            mydbcursor.execute(sql, args)
            mylist=mydbcursor.fetchone()
            print(mylist)

        except Exception as e:
            print(str(e))
        finally:
            mydb.commit()
            if mydbcursor !=None:
                mydbcursor.close()
            if mydb !=None:
                mydb.close()
    
    def update_faculity(self,fid, newDesignation,newSubject):
        try:
            mydb=None
            mydb=pymysql.connect(host=self.host,user=self.user,password=self.password,database=self.database)
            mydbcursor=mydb.cursor()

            sql='''update faculity set `designation`=%s, `subject`=%s where `id`=%s '''
            args = (newDesignation,newSubject,fid)
            mydbcursor.execute(sql, args)
        
        except Exception as e:
            print(str(e))
        finally:
            mydb.commit()
            if mydbcursor !=None:
                mydbcursor.close()
            if mydb !=None:
                mydb.close()
        

    def update_student(self, sid,newSemester,newCgpa):
        try:
            mydb=None
            mydb=pymysql.connect(host=self.host,user=self.user,password=self.password,database=self.database)
            mydbcursor=mydb.cursor()

            sql="update student set semester=%s AND cgpa=%s where id=%s "
            args = (newSemester,newCgpa,sid)
            mydbcursor.execute(sql, args)

        except Exception as e:
            print(str(e))
        finally:
            mydb.commit()
            if mydbcursor !=None:
                mydbcursor.close()
            if mydb !=None:
                mydb.close()

    def delete_faculity(self, fid):
        try:
            mydb=None
            mydb=pymysql.connect(host=self.host,user=self.user,password=self.password,database=self.database)
            mydbcursor=mydb.cursor()

            sql="delete from faculity where id=%s "
            args = (fid)
            mydbcursor.execute(sql, args)

        except Exception as e:
            print(str(e))
        finally:
            mydb.commit()
            if mydbcursor !=None:
                mydbcursor.close()
            if mydb !=None:
                mydb.close()

    def delete_student(self, sid):
        try:
            mydb=None
            mydb=pymysql.connect(host=self.host,user=self.user,password=self.password,database=self.database)
            mydbcursor=mydb.cursor()

            sql="delete from student where id=%s "
            args = (sid)
            mydbcursor.execute(sql, args)

        except Exception as e:
            print(str(e))
        finally:
            mydb.commit()
            if mydbcursor !=None:
                mydbcursor.close()
            if mydb !=None:
                mydb.close()

    def authenticateUser(self, username, password):
        myDb = None
        myCursor = None
        try:
            myDb = pymysql.connect(host = self.host, user = self.user, password=self.password, database=self.database)
            myCursor = myDb.cursor()
            query = "select * from user where username = %s AND password = %s"
            args = (username, password)        
            myCursor.execute(query, args)
            row = myCursor.fetchall()
            count = 0
            for i in row:
                count = count + 1
                print(i)
            if count != 0:
                return True
            return False
            myDb.commit()
        except Exception as e:
            print(str(e))
        finally:
            if myCursor != None:
                myCursor = None
            if myDb != None:
                myDb = None


# f=faculity(2,"head","chem",3,"malik","123")

# dbh=dbHandler("localhost","root","Bb22092001@#","fcit")
# # s=student(11,3,"5","CS",10,"lal",309)
# dbh.update_faculity("111","111",43)


