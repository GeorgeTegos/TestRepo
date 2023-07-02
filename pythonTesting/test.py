import re
peopleDB= []



def emailCheck(email):
    regex = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,7}\b'
    if(re.fullmatch(regex,email)):
        return email
    else:
        while (re.fullmatch(regex,email) != True):
            email = input("Invalid e-mail , try again: ")
            if (re.fullmatch(regex,email)):
                return email

def phoneCheck(phone):
    regex = r'\d{10}'
    if(re.fullmatch(regex,phone)):
        return phone
    else:
        while (re.fullmatch(regex,phone) != True):
            phone = input("Invalid phone, try again: ")
            if (re.fullmatch(regex,phone)):
                return phone

def ageCheck(age):
    regex = r'\d{2,3}'
    if(re.fullmatch(regex,age)):
        return age
    else:
        while (re.fullmatch(regex,age) != True):
            age = input("Invalid age, try again: ")
            if (re.fullmatch(regex,age)):
                return age

class people:


    def __init__(self, name, age, email, phone, password):
        self.name = name.lower().capitalize()
        self.age = ageCheck(age)
        self.email = emailCheck(email)
        self.phone = phoneCheck(phone)
        self.password = password
    
    def informations(self):
        print(self.name, self.age, self.email, self.phone, self.password)

    def peopleInfo():
        userX = people(input('Name '),input('age '),input("email "), input("phone "), input("Password "))
        print(f"Name: ",userX.name,"\nAge: ", userX.age, "\nEmail: ", userX.email,"\nPhone: ", userX.phone,"\nPassword: ", userX.password)

        NEWpeopleDB = [userX.name,int(userX.age),userX.email,int(userX.phone),userX.password]
        peopleDB.append(NEWpeopleDB)


        if (input("New input ? Y/N\n") == "Y"):
            whoIsIt()
        elif (input("Check people Database? Y/N\n") == "Y"):
            #checkPeopleDB()
            print(peopleDB)
        else:
            pass

class user(people):
    
    def __init__(self, name, age, email, phone, password, userID):
        super().__init__(name, age, email, phone, password)
        self.userID = userID
        
    def userInput():
        userX = user(input('Name '),input('age '),input("email "), input("phone "), input("Password "), input("ID "))
        print(f"\nName: ",userX.name,"\nAge: ", userX.age, "\nEmail: ", userX.email,"\nPhone: ", userX.phone,"\nPassword: ", userX.password,"\nYour ID: ", userX.userID)

class employee(people):
    def __init__(self, name, age, email, phone, password, employeeID):
        super().__init__(name, age, email, phone, password)
        self.employeeID = employeeID
    def employeeInput():
        userX = employee(input('Name '),input('age '),input("email "), input("phone "), input("Password "), input("ID "))
        print(f"Name: ",userX.name,"\nAge: ", userX.age, "\nEmail: ", userX.email,"\nPhone: ", userX.phone,"\nPassword: ", userX.password, "\nYour ID: ", userX.employeeID)

def peopleDatabase(number):
    peopleDB[number].update()
    return peopleDB

def whoIsIt():
    whoIsIt = input("\nWho are you ? \n1) New \n2) Already User \n3) Employee\n4) Quit\n")
    whoIsIt = int(whoIsIt)

    if whoIsIt == 1:
        people.peopleInfo()
    elif whoIsIt == 2:
        user.userInput()
    elif whoIsIt == 3:
        employee.employeeInput()
    else:
        print("Wrong input")
    
def checkPeopleDB():
    print("------------")
    #for key in peopleDB:
    #    print(key," = ",peopleDB[key])
    print(peopleDB)
    print("----------")

whoIsIt()
