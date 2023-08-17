from user import user
class student(user):
    def __init__(self,sid,semester,cgpa,major,user_id,username,password):
        user.__init__(self, user_id, username, password)
        self.sid=sid
        self.semester=semester
        self.cgpa=cgpa
        self.major=major