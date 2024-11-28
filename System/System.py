import os, shutil

"""Defined Function Program Version 0.01.0"""
"""Public:Variables & Consts"""
const_SystemRootDirectory = os.getcwd()
const_LoginUserDirectory = os.getcwd()
const_loginUser = ""


#def setColor(color):
#    return ctypes.windll.kernel32.SetConsoleTextAttribute(ctypes.windll.kernel32.GetStdHandle(-11), color)

def version():
    print(
        """XJY-DOS-Base Disk Operating System(Console Version)
Copyright (C)2023-2024 JinY Corporation.All rights reserved.\nVersions:DOS Alpha 0.01.1.24001 | Visual C++ 2024 | Python CPython 3.12.5 x64
! Internal Test Version !""")


def judgeCommand(inputcommand: str):
    """Class Def Variables"""
    fileCmd = file()
    userCmd = user()
    """-----Class End-----"""
    command = ""
    counter = 0
    parameter = []
    parameterWithMark = []
    for _ in inputcommand:
        if _ == "(":
            command = inputcommand[:counter]
            parameterWithMark = list(map(str, inputcommand[counter + 1:-1].split(",")))
            break
        counter += 1
    for _ in parameterWithMark:
        parameter.append(_[1:-1])
    if command[:6] == "check.":
        classway = command[6:]
        if classway == "IOCheck":
            check.IOCheck()
        elif classway == "ConsoleCheck":
            check.ConsoleCheck()
        else:
            raise NameError("There's no Function called \"" + inputcommand + "\".")
    elif command[:5] == "file.":
        classway = command[5:]
        if classway == "recoverDefaultDir":
            file.recoverDefaultDir()
        elif classway == "createFolder":
            file.createFolder(fileCmd, parameter[0], parameter[1])
        elif classway == "deleteFolder":
            file.deleteFolder(fileCmd, parameter[0], parameter[1])
        elif classway == "createFile":
            file.createFile(fileCmd, parameter[0], parameter[1])
        elif classway == "deleteFile":
            file.deleteFile(fileCmd, parameter[0], parameter[1])
        elif classway == "writeFileText":
            file.writeFileText(fileCmd, parameter[0], parameter[1], parameter[2])
        else:
            raise NameError("There's no Function called \"" + inputcommand + "\".")
    elif command[:5] == "user.":
        classway = command[5:]
        if classway == "addUser":
            user.addUser(userCmd, parameter[0], parameter[1])
    elif command == "version":
        version()
    else:
        raise NameError("There's no Function called \"" + inputcommand + "\".")


# 这个函数只对未编译的Python源文件使用。
"""def delCache():
    shutil.rmtree(os.getcwd()+"\\System\\__pycache__")
    print("Clean cache successful.")"""


def _writeUnicodeString(string):
    outstr = ""
    tmp = 0
    for _ in string:
        if tmp == len(string) - 1:
            outstr += str(ord(_))
        else:
            outstr += str(ord(_)) + " "
        tmp += 1
    return outstr


def _readUnicodeString(unicodestring):
    outstr = ""
    string = list(map(int, unicodestring.split(" ")))
    for _ in string:
        outstr += str(chr(_))
    return outstr


def _start():
    a = ""
    print("[POS]Starting System...")
    with open(const_SystemRootDirectory + "\\System\\SAM", "r+") as f:
        f.seek(0)
        a = f.read()
    return _userJudge(a)


def _userJudge(st):
    statements = list(_readUnicodeString(st).split(" "))
    userDat = {}
    tmp = 0;
    usernum = 0
    for i in statements:
        # Judge Username and Userpwd
        if "MainUser:" == i[:9]:
            # Main User is equal to User0
            userDat[i[9:]] = statements[tmp + 1]
            usernum += 1
        if i[:5] == "User:":
            userDat[i[5:]] = statements[tmp + 1]
        tmp += 1
    return userDat


def _analysisPaths(path):
    """C:==System\\"""
    outstr = const_LoginUserDirectory + path[3:]
    return outstr


def _nowDirectory():
    return const_LoginUserDirectory


class check:
    @staticmethod
    def IOCheck():
        os.mkdir("checkFolder")
        f = open("checkFolder\\checkUACFile.log", "w+")
        a = _writeUnicodeString("checking...AaBbCcDdEeFfGgHhIiGjKk--UTF-8!@#$%^&*\\\"\'")
        f.write(a)
        f.seek(0)
        checkText = f.read()
        f.close()
        os.remove("checkFolder\\checkUACFile.log")
        os.rmdir("checkFolder")
        if _readUnicodeString(checkText) == "checking...AaBbCcDdEeFfGgHhIiGjKk--UTF-8!@#$%^&*\\\"\'":
            print("[System]<check>IOcheck:IOcheck Success.")
            return True
        else:
            print("[System]<check>IOcheck:IOcheck Failed!")
            return False

    def ConsoleCheck():
        print(
            "ABCDEFGHIGKLMNOPQRSTUVWXYZabcdefghijklmnoptrstuvwxyz-Backspace\" \"-~!@#$%^&*()`_+-=1234567890[]\\;\',./{}|:\"<>?\'")
        print("[System]<check>Consolecheck:ConsoleCheck Run Successful.")


class file:
    def recoverDefaultDir():
        os.chdir(const_SystemRootDirectory)

    def createFolder(self, path, foldername):
        os.chdir(_analysisPaths(path))
        os.mkdir(foldername)
        file.recoverDefaultDir()
        print("[FileSystem]Folder Created.")

    def deleteFolder(self, path, foldername):
        os.chdir(_analysisPaths(path))
        if len(os.listdir(os.getcwd() + "\\" + foldername)) != 0:
            if input(
                    "[FileSystem]This Directory is not empty.Do you want to delete the sub-files(\"Y\"or\"N\")?") == "Y":
                shutil.rmtree(foldername)
            else:
                print("[FileSystem]Folder Deleted.")
                return False
        else:
            os.rmdir(foldername)
        file.recoverDefaultDir()
        print("[FileSystem]Folder Deleted.")

    def createFile(self, path, filename):
        f = open(_analysisPaths(path) + "\\" + filename, "w+")
        f.close()
        print("[FileSystem]File created.")

    def deleteFile(self, path, filename):
        os.remove(path + filename)
        file.recoverDefaultDir()
        print("[FileSystem]File Deleted.")

    def writeFileText(self, path, text, mode):
        path = _analysisPaths(path)
        if mode == "add":
            with open(path, "a") as f:
                f.write(text)
        elif mode == "fill":
            with open(path, "w") as f:
                f.write(text)
        print("[FileSystem]File text wrote.")



class user:
    def addUser(self, username, password=""):
        with open(const_SystemRootDirectory + "\\System\\SAM", "a") as f:
            f.write(" " + _writeUnicodeString("User:" + username + " " + password))

    def deleteUser(self, username):
        with open(const_SystemRootDirectory + "\\System\\SAM", "w") as f:
            pass
