from ProfileInformation import User
class UserDatabase:
    def __init__(self):
        self.users = []
    
    def insert(self,user) :
        i = 0 
        while i < len(self.users):
            if self.users[i].username > user.username:
                break
            i +=1

        self.users.insert(i,user)

    def find(self,username) -> User:
        for user in self.users:
            if user.username == username:
                return user
    
    def update(self,user):
        target = self.find(user.username)
        target.name , target.email = user.name ,user.email
    
    def list_all(self):
        return self.users

