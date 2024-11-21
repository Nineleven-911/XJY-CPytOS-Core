from System import System

print("Main Process Start Running.")

# INIT
System.check.IOCheck()
System.check.ConsoleCheck()
System.start()

try:
    while 1:
        if input("User Name:") == "Admin":
            if input("Password:") == "12345678":
                break
            else:
                print("Username or Userpassword error.")
        else:
            print("Username or Userpassword error.")
    print("Welcome,Administrator!")
    while 1:
        try:
            command = input(" >>>")
            System.judgeCommand(command)
        except Exception as err:
            print("Command Run Failed.", err)
except Exception as e:
    print("System Error.OS or \".exe\" file may in a wrong place,or losing important files.\nInformation:", e)
    input("\nPress Enter to exit DOS.")
    exit()
