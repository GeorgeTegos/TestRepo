import re
peopleDB= []
userDB = []
employeeDB = []

def newInput():
    option = input("~~~~~~~~\nNew input ? Y/N\n~~~~~~~~\n")
    option = option.lower()
    if (option == "y"):
        whoIsIt()
    else:
        MainMenu()

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

        newPeopleInput = [userX.name,int(userX.age),userX.email,int(userX.phone),userX.password]
        peopleDB.append(newPeopleInput)

        newInput()

class user(people):
    
    def __init__(self, name, age, email, phone, password, userID):
        super().__init__(name, age, email, phone, password)
        self.userID = userID
        
    def userInput():
        userX = user(input('Name '),input('age '),input("email "), input("phone "), input("Password "), input("ID "))
        print(f"\nName: ",userX.name,"\nAge: ", userX.age, "\nEmail: ", userX.email,"\nPhone: ", userX.phone,"\nPassword: ", userX.password,"\nYour ID: ", userX.userID)
        
        newUserInput = [userX.name,int(userX.age),userX.email,int(userX.phone),userX.password]
        userDB.append(newUserInput)
        
        newInput()

class employee(people):
    def __init__(self, name, age, email, phone, password, employeeID):
        super().__init__(name, age, email, phone, password)
        self.employeeID = employeeID
    def employeeInput():
        userX = employee(input('Name '),input('age '),input("email "), input("phone "), input("Password "), input("ID "))
        print(f"Name: ",userX.name,"\nAge: ", userX.age, "\nEmail: ", userX.email,"\nPhone: ", userX.phone,"\nPassword: ", userX.password, "\nYour ID: ", userX.employeeID)

        newEmployeeInput = [userX.name,int(userX.age),userX.email,int(userX.phone),userX.password]
        employeeDB.append(newEmployeeInput)

        newInput()

def whoIsIt():
    whoIsIt = input("\nWho are you ? \n1) New \n2) Already User \n3) Employee\n4) Make new inputs \n5) Exit\n")
    whoIsIt = int(whoIsIt)

    if whoIsIt == 1:
        people.peopleInfo()
    elif whoIsIt == 2:
        user.userInput()
    elif whoIsIt == 3:
        employee.employeeInput()
    elif whoIsIt == 4:
        whoIsIt()
    elif whoIsIt == 5:
        pass
    else:
        print("Wrong input")

def checkDataBase():
    option = input("\n1) Visitors Database \n2) Users Database \n3) Employees Database\nPress anything else to exit\n")
    if option == "1":
        print(peopleDB)
        newInput()
    elif option == "2":
        print(userDB)
        newInput()
    elif option == "3":
        print(employeeDB)
        newInput()
    else:
        return None

def MainMenu():
    option = input("\nWelcome to my personal DB\nChoose one of the below\n1) Login (not working)\n2) New Inputs\n3) Check Database\n4) Exit\n")
    option = int(option)

    if(option == 1):
        pass
    elif (option == 2):
        whoIsIt()
    elif (option == 3):
        checkDataBase()
    elif (option == 4):
        exit()
    else:
        print("\nWrong Input\n")

MainMenu()

# 1) ask for peopleDB to user or employee
# 2) safe inputs to CSV
# 3) read CSV inputs and update them
# 4) -- Safe them in local DB --
# 5) -- Make function Login with privillages --
