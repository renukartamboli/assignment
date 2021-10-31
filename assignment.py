from cryptography.fernet import Fernet
class Switcher(object):
    users = {}
    weatherInformation= {"goa":{"humidity":5,"Pressure":6,"Average Temperature":30,"Wind Speed":5,"Wind Degree":9,"UI index":12},"jaipur":{"humidity":5,"Pressure":6,"Average Temperature":30,"Wind Speed":5,"Wind Degree":9,"UI index":12},"banglore":{"humidity":5,"Pressure":6,"Average Temperature":30,"Wind Speed":5,"Wind Degree":9,"UI index":12},"-90/+90":{"humidity":5,"Pressure":6,"Average Temperature":30,"Wind Speed":5,"Wind Degree":9,"UI index":12}}
    key = Fernet.generate_key()
    cipherSuite = Fernet(key)
    def __init__(self):
        Switcher.users = {'testUser':Switcher.cipherSuite.encrypt('123'.encode())}
    def Operation(self,method_name):
        method=getattr(self,method_name,lambda :'Invalid')
        return method()
    
    def create(self):
        print("enter user name:")
        user = input()
        print("enter password:")
        password = input()
        Switcher.users[user]=Switcher.cipherSuite.encrypt(password.encode())
        print("User created Successfully!!")
    
    def update(self):
        print("Enter your userName to update")
        user = input()
        password = Switcher.users[user]
        print("Do you want to update username? y/n")
        ans = input()
        if(ans == "y"):
            print("Enter new userName")
            enteredUser = input()
            print("Enter your password")
            i =3
            p=0
            while(i!=0):
                enteredPass = input()
                if(Switcher.cipherSuite.decrypt(password).decode()==enteredPass):
                    del Switcher.users[user]
                    Switcher.users[enteredUser] = password
                    print("Username updated successfully")
                    p=1
                    break
                else:
                    print("incorrect password")
                i-=1
            if(p!=1):
                print("Incorrect password attemp 3 times.Please try again later.")
        print("Do you want to update password? y/n")
        ans = input()
        if(ans=="y"):
            print("Enter old password")
            i=3
            while(i!=0):
                enteredPass = input()
                if(Switcher.cipherSuite.decrypt(password).decode()==enteredPass):
                    print("enter new password")
                    newPass = input()
                    Switcher.users[user]=Switcher.cipherSuite.encrypt(password)
                    p=1
                    print("Password updated Successfully!!")
                    break
                else:
                    print("incorrect password")
                i-=1
            if(p!=1):
                print("Incorrect password attemp 3 times.Please try again later.")
    
    
    
    def delete(self):
        print("Enter user name to delete")
        user = input()
        del Switcher.users[user]
        print("User deleted Successfully")

    def readAll(self):
        print("User Entries:")
        for key,value in Switcher.users.items():
            print(key,end="\t")
        print("\n")

    def weatherInfo(self):
        print("Enter City Name or Longitude and Latitude in following manner: Longitude/Latitude")
        location = input()
        if(location not in Switcher.weatherInformation.keys()):
            print("no weather info for this location")
            return
        for info in Switcher.weatherInformation[location]:
            print(info,':',Switcher.weatherInformation[location][info])

    def helpCmd(self):
        return "Press 1 for creating new user \n Press 2 to update user \n Press 3 to delete user \n Press 4 to print all users \n Press 5 for weather information \n --help for help command"
    
if __name__ == "__main__":
    s=Switcher()
    Choice = 0
    while(Choice!="exit"):
        print("\n")
        print("Enter your Choice:")
        print("1 - creating new user")
        print("2 - update user")
        print("3 - delete user")
        print("4 - print all users")
        print("5 - weather information")
        print("--help for help command")
        print("Type exit to quit")
        print("\n")
        Choice = input()
        if(Choice=="--help"):
            print(s.Operation('helpCmd'))
        if(Choice=='1'):
            s.Operation('create')
        if(Choice=='2'):
            s.Operation('update')
        if(Choice=='3'):
            s.Operation('delete')
        if(Choice=='4'):
            s.Operation('readAll')
        if(Choice=='5'):
            s.Operation('weatherInfo')