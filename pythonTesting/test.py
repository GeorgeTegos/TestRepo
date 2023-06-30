import re

def emailCheck(email):
    regex = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,7}\b'
    if(re.fullmatch(regex,email)):
        return email
    else:
        while (re.fullmatch(regex,email) != True):
            email = input("Invalid e-mail , try again: ")
            if (re.fullmatch(regex,email)):
                return email


class people:


    def __init__(self, name, age, email, phone, password):
        self.name = name
        self.age = int(age)
        self.email = emailCheck(email)
        self.phone = int(phone)
        self.password = password
    
    def informations(self):
        print(self.name, self.age, self.email, self.phone, self.password)

class user(people):
    
    def __init__(self, name, age, email, phone, password, userID):
        super().__init__(name, age, email, phone, password)
        self.userID = userID
        pass

class employee(people):
    pass

userInfo = user("george",29,"gtultim@asd.com",123123,11111111,19)

employeeInfo = employee("nick",34,"ggg@sss.cas",1234234,222222)

def userInput():
    userX = user(input('Name '),input('age '),input("email "), input("phone "), input("Password "), input("ID "))
    print(userX.name, userX.age, userX.email, userX.phone, userX.password, userX.id)

def peopleInfo():
    userX = people(input('Name '),input('age '),input("email "), input("phone "), input("Password "))
    print(userX.name, userX.age, userX.email, userX.phone, userX.password)


userInput()
peopleInfo()


