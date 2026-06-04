from abc import ABC,abstractmethod

class Person(ABC):

    def __init__(self):
        pass

    @abstractmethod
    def Display_Data(self):
        pass   

    
    def __del__(self):
        pass
               

class Employee(Person):

    company_name = "ABC_Infotech.in"

    def __init__(self, id1, name, age):
        super().__init__()
        self.id = id1
        self.name = name
        self.age = age
    
    def Display_Data(self):
        print("-----------------------------")
        print("Employee Id     :",self.id)
        print("Employee Name   :",self.name)
        print("Employee Age    :",self.age)

    @classmethod
    def info(cls):
        print(cls.company_name)    

        


class Manager(Employee):
    def __init__(self, id1, name, age,Salary,dep):
        super().__init__(id1, name, age)
        self.__salary = Salary
        self.dep = dep

    def Display_Data(self):
        print("-----------------------------")
        print(" Manager Id         :",self.id)
        print(" Manager Name       :",self.name)
        print(" Manager Age        :",self.age)  
        print(" Manager Department :",self.dep)
        print(" Manager Salary     :",self.__salary)

        
    
class Devloper(Employee):
    def __init__(self, id1, name, age,Salary,lan):
        super().__init__(id1, name, age)
        self.__salary = Salary
        self.lan = lan

    def Display_Data(self):
        print("-----------------------------")
        print(" Devloper Id     :",self.id)
        print(" Devloper Name   :",self.name)
        print(" Devloper Age    :",self.age)  
        print(" Devloper Salary :",self.__salary) 
        print(" Devloper Programming Languages :",self.lan) 

    def __del__(self):
       super().__del__()
            
while True:
    
    print("----- EMPLOYEE MANAGEMENT SYSTEM ----- ")
    print("1) Create An Employee")
    print("2) Create  A Manager")
    print("3) Create  A Devloper")
    print("4) Show Details")
    print("5) Exit")

    ch = int(input("Enter Your Choice"))

    match ch : 

        case 1 :
            print("Create An Employee")
            print("-------------------------")
            id1 = int(input("Enter  Id"))
            name = input("Enter Name")
            age = int(input("Enter Age"))
            print(" ")

            e = Employee(id1,name,age)

            print("Employee Class Are Create.....") 

            while True:
                print("Menu")
                print("1) Show Class Info")
                print("2) Show Employee Data")
                print("3) Exit")

                ch1 = int(input("Enter Your Choice"))

                match ch1:

                    case 1:
                        print("----Class Info----")
                        print()
                        Employee.info()
                        print("Employee Is Subclass   : ",issubclass(Employee,Manager))
                        print("Employee Is Isinstance : ",isinstance(e,Employee))
                    case 2 :
                        print("----Employee Data----")    
                        print()
                        e.Display_Data()
                    case 3 :
                        print()
                        break    
            
        case 2:
            print("Create  A Manager")
            print("-------------------------")

            id1 = int(input("Enter  Id"))
            name = input("Enter Name")
            age = int(input("Enter Age"))
            salary = int(input("Enter Salary"))
            dep = input("Enter Department")
            print(" ")
            m = Manager(id1,name,age,salary,dep)
            
            print("Manager Class Are Create.....")

            while True:
                print("Menu")
                print("1) Show Class Info")
                print("2) Show Manager Data")
                print("3) Exit")

                ch1 = int(input("Enter Your Choice"))

                match ch1:

                    case 1:
                        print("----Class Info----")
                        print()
                        Manager.info()
                        print("Manager Is Subclass   : ",issubclass(Manager,Employee))
                        print("Manager Is Isinstance : ",isinstance(m,Manager))
                    case 2 :
                        print("----Manager Data----")    
                        print()
                        m.Display_Data()
                    case 3 :
                        print()
                        break   

        case 3:
            print("Create  A Devloper")
            print("-------------------------")
            
            id1 = int(input("Enter  Id"))
            name = input("Enter Name")
            age = int(input("Enter Age"))
            salary = int(input("Enter Salary"))
            lan = input("which Languages Devloper ?  ")
            print(" ")
            d = Devloper(id1,name,age,salary,lan)
            
            print("Devloper Class Are Create.....")
         
            while True:
                print("Menu")
                print("1) Show Class Info")
                print("2) Show Devloper Data")
                print("3) Exit")

                ch1 = int(input("Enter Your Choice"))

                match ch1:

                    case 1:
                        print("----Class Info----")
                        print()
                        Devloper.info()
                        print("Devloper Is Subclass   : ",issubclass(Devloper,Employee))
                        print("Devloper Is Isinstance : ",isinstance(d,Devloper))
                    case 2 :
                        print("----Devloper Data----")    
                        print()
                        d.Display_Data()
                    case 3 :
                        print()
                        break   


        case 4:
            print(" All Show Details")
            while True:
                print("----Menu------")
                print("1) Employee Details")
                print("2) Manager Details")
                print("3) Devloper Details")
                print("4) Exit")

                ch2 = int(input("Enter Your Choice"))

                match ch2 :
                    case 1:
                        print("Employee Details")
                        e.Display_Data()
                    case 2 :
                        print("Manager Details")
                        m.Display_Data()
                    case 3:
                        print("Devloper Details")
                        d.Display_Data()
                    case 4:
                        break   
        
        case 5:
            
            print("Exiting The System . All Resources Have Been Freed")
            print("Goodbye..")
            exit()
           

