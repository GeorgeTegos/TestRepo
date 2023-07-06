import re
import csv
    
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

        what_is_it = int(input("\nFor new user Press 1\nFor new employee press 2\nFor new Admind press 9\n"))

        newUserInput = {
            "Name": userX.name,
            "Age": int(userX.age),
            "E-mail": userX.email,
            "Phone": userX.phone,
            "Password": userX.password,
        }
        
        if what_is_it == 1:
            give_user_id = int(input("Give user ID"))
            newUserInput['ID'] = give_user_id
            userDB.append(newUserInput)
        elif what_is_it == 2:
            give_user_id = int(input("Give user ID"))
            newUserInput['ID'] = give_user_id
            employeeDB.append(newUserInput)
        else:
            print("wrong input")
        



        newInput()

class user(people):
    
    def __init__(self, name, age, email, phone, password, userID):
        super().__init__(name, age, email, phone, password)
        self.userID = userID
        
    def userInput():
        userX = user(input('Name '),input('age '),input("email "), input("phone "), input("Password "), input("ID "))
        print(f"\nName: ",userX.name,"\nAge: ", userX.age, "\nEmail: ", userX.email,"\nPhone: ", userX.phone,"\nPassword: ", userX.password,"\nYour ID: ", userX.userID)
        
        # newUserInput = [userX.name,int(userX.age),userX.email,int(userX.phone),userX.password]
        newUserInput = {
            "Name": userX.name,
            "Age": int(userX.age),
            "E-mail": userX.email,
            "Phone": userX.phone,
            "Password": userX.password,
            "ID": userX.userID
        }
        userDB.append(newUserInput)
        
        newInput()

class employee(people):
    def __init__(self, name, age, email, phone, password, employeeID):
        super().__init__(name, age, email, phone, password)
        self.employeeID = employeeID
    def employeeInput():
        userX = employee(input('Name '),input('age '),input("email "), input("phone "), input("Password "), input("ID "))
        print(f"Name: ",userX.name,"\nAge: ", userX.age, "\nEmail: ", userX.email,"\nPhone: ", userX.phone,"\nPassword: ", userX.password, "\nYour ID: ", userX.employeeID)

        newEmployeeInput = {
            "Name": userX.name,
            "Age": int(userX.age),
            "E-mail": userX.email,
            "Phone": userX.phone,
            "Password": userX.password,
            "ID": userX.employeeID
        }

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
    option = input("\n1) Users Database \n2) Employees Database\n3) Admins Database\nPress anything else to exit\n")
    if option == "1":
        print(userDB)
        newInput()        
    elif option == "2":
        print(employeeDB)
        newInput()
    elif option == "3":
        print("Admins are not ready yet")
        MainMenu()
    else:
        return None

def MainMenu():
    test_list = ["0","1","2","3","4","5","6","7","8","9"]
    option = input("\nWelcome to my personal DB\nChoose one of the below\n1) Login (not working)\n2) New Inputs\n3) Check Database\n9) Data to CSV\n4) Exit\n")
    #Force INT option input !!!!
    
    if option in test_list:
        if (int(option) == 1):
            pass
        elif (int(option) == 2):
            whoIsIt()
        elif (int(option) == 3):
            checkDataBase()
        elif (int(option) == 4):
            exit()
        elif (int(option) == 9):
            dataIntoCSV(userDB)
        else:
            print("wrong input, try again")
            exit()
    else:
        print("Try again !")
    
def dataIntoCSV(database):

    # for key in database:
    #     local_key_save = key.keys()
    #     data_to_save.append(local_key_save)

    data_to_save = ["Name","Age","E-mail","Phone","Password","ID"]
    with open('mycsvfile.csv',"w") as csvfile:
        writer = csv.DictWriter(csvfile,data_to_save)
        writer.writeheader()
        writer.writerows(database)
    
    
MainMenu()
# 1) ask for peopleDB to user or employee ++
# 2) safe inputs to CSV
# 3) read CSV inputs and update them
# 4) -- Safe them in local DB --
# 5) -- Make function Login with privillages --
