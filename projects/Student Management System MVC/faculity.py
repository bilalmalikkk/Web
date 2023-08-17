from user import user
class faculity(user):
    def __init__(self,fid,designation,subject,user_id, username, password):
        user.__init__(self, user_id, username, password)
        self.fid=fid
        self.designation=designation
        self.subject=subject
        