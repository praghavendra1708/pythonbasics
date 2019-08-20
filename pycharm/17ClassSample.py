class User:
    pass

user1 = User()
user1.name = "Unknown"
user1.birthday = "19700101"

from datetime import datetime


class UserDetails:
    """ This is class that stores user details"""

    def __init__(self, name, dob):
        self.name = name
        self.dob = datetime.strptime(dob, '%d/%m/%Y')

    def age(self):
        today = datetime.today()
        return int((today - self.dob).days / 365)


usrDetails = UserDetails('Unknown', '01/01/1970')
print(usrDetails.name, usrDetails.dob, " and today his age is", usrDetails.age())
