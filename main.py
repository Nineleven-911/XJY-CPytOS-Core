# -*- coding: utf-8 -*-

import os
import shutil
import colorama
import random

from datetime import datetime

# import tqdm
# import pwinput

import system
import functions as func

# Init 初始化部分
system.write_log(None, is_new=True)

# Variables
root_loc = os.getcwd()
is_login = False

# Variables Defining Ends

# Initiation for Nuitka (为Nuitka的初始化，因为Nuitka的处理逻辑是: 不用到，不打包)
colorama.init()
os.system("cls" if os.name == "nt" else "clear")
usr = system.read_users()
print(
    fr"""XJY-DOS <Alpha 0.02.0 Remake>
[Development Version]: Build in XJY-CPython Operating System Core Version <0.01.0>
{system.consts.OS_ICON}
""")

# Initiation ends

# Login 登录账户部分
account_logged_in = func.user.login(usr)

# Main Loop 主循环
command_case = ""
command_args = []
while 1:
    try:  # 循环主体
        command = input(" >>>")
        # Split command
        command_case = "NaS"
        command_args = []
        if "(" not in command and ")" not in command:
            command_case = command
        else:
            command_case = command[:command.find("(")]
            command_args: list = command[command.find("(") + 1:command.rfind(")")].split(",")
        if command_case == "":
            continue

        # Judge 判断指令

        """ # Prefix Commands 前缀命令
        # It will be executed if there's a prefix in command. 当命令有前缀时, 激活此处判断语句 
        if "." in command_case:
            command_without_prefix = command_case[command.find(".") + 1:]
            if command[:command.find(".")] == "os":
                match command_without_prefix:
                    case "version":
                        pass

            """

        # Test Commands 测试命令
        # print(system.write_user_log("Admin1", "123456", "admin", usr))

        match command_case:
            # OS Basic Commands 基础命令(操作系统底层命令)
            case "version":
                system.info.normal_info("System info: \
XJY-CPython Operating System Core <0.01.0> \nOS Version: Alpha Build 00101.03067.19377.11001")
            case "exit":
                system.info.normal_info("You can close the Operating-System now.")
                break
            case "tips":
                system.info.normal_info(random.choice(system.consts.TIPS))

            case "cls":
                os.system("cls" if os.name == "nt" else "clear")

            case "debugger":  # 调试器
                if usr[account_logged_in][1] != "admin":
                    raise PermissionError("Have no enough permissions")
                os.system("cls" if os.name == "nt" else "clear")
                print(system.consts.OS_ICON + "\n" +
                      system.consts.OS_DEBUGGER_ICON
                      )
                login_success: bool = False
                scope = system.CommandScope()
                user_pwd = ""
                while not login_success:  # 终端用户验证
                    user_pwd = input("PWD >>>")
                    if user_pwd == "1111":
                        login_success = True
                        break
                    if user_pwd == "":
                        break
                else:
                    while 1:
                        scope.command = input(" -").lower()
                        scope.command_case = scope.command.split(" ")[0]
                        scope.args = [value for value in scope.command.split(" ")[1:] if value != ""]
                        # Debug
                        # print(scope.command, " | ", scope.command_case, " | ", scope.args)
                        try:
                            match scope.command_case.lower():
                                case "exit":
                                    break
                                case "":
                                    continue
                                case "cls":
                                    os.system("cls" if os.name == "nt" else "clear")
                                case "db":
                                    if len(scope.args) == 0:
                                        print("No arguments.")
                                        continue
                                    if (scope.args[0] == "--check" and not system.chars_in(
                                                scope.args[1], ["(", ")", ",", ".", "|", "?", "!", "~"]
                                            )):
                                        print(eval(scope.args[1]))
                                    else:
                                        print("Invalid argument.")
                                case _:
                                    print("Invalid command.")
                        except EOFError:
                            print("EOF Exited.")
                            break
                        except Exception as err:
                            system.info.error_info(str(err))
                os.system("cls" if os.name == "nt" else "clear")
                print(system.consts.OS_ICON)

            # User Commands 用户命令
            case "relogin":
                system.write_log("Login status be turned to: non_login")
                account_logged_in = func.user.login(usr)

            case "logining":
                system.info.normal_info(
                    "User name: " + account_logged_in)

            case "adduser":
                system.require_args(3, command_args)
                if usr[account_logged_in][1] != "admin":
                    raise PermissionError("Have no enough permissions")
                system.write_users(
                    system.encrypt(system.write_user_log(command_args[0], command_args[1], command_args[2], usr))
                )
                system.write_log(f"Use command: \"{command_case}\", args are not viewable.")
                continue

            case "deluser":
                system.require_args(1, command_args)
                if usr[account_logged_in][1] != "admin":
                    raise PermissionError("Have no enough permissions")
                result = ""
                for key, value in usr.items():
                    if key != command_args[0]:
                        result += f"{key}:{value[0]}?{value[1]},"
                system.write_users(
                    system.encrypt(result[:-1])
                )
                system.write_log(f"Use command: \"{command_case}\", args are not viewable.")
                continue

            case "chgpwd":
                system.require_args(2, command_args)
                if usr[account_logged_in][1] != "admin":
                    raise PermissionError("Have no enough permissions")
                result = ""
                found = False
                for key, value in usr.items():
                    if key != command_args[0]:
                        result += f"{key}:{value[0]}?{value[1]},"
                    else:
                        result += f"{key}:{command_args[1]}?{value[1]},"
                        found = True
                if not found:
                    system.info.normal_info(f"There is no user called \"{command_args[0]}\"")
                system.write_users(
                    system.encrypt(result[:-1])
                )
                system.write_log(f"Use command: \"{command_case}\", args are not viewable.")
                continue

            # Applications Commands 软件命令
            case "apps":
                print(f"----------Directory of \"{os.getcwd() + "\\Program Files (p3.12)"}\"----------")
                for file_name in os.listdir(os.getcwd() + "\\Program Files (p3.12)"):
                    file_loc = root_loc + "\\Program Files (p3.12)\\" + file_name
                    file_last_write_date = datetime.fromtimestamp(os.stat(file_loc).st_mtime)
                    print(f"<{file_last_write_date}> {file_name} <xOS Application>")

            case "run":
                system.require_args(1, command_args)
                app_name = command_args[0]
                if app_name not in os.listdir(os.getcwd() + "\\Program Files (p3.12)\\"):
                    raise FileNotFoundError(f"Can't find an application called \"{app_name}\"")
                elif usr[account_logged_in][1] == "guest":
                    raise PermissionError("Have no enough permissions")
                os.system(f"python \"{os.getcwd() + "\\Program Files (p3.12)\\" + app_name}\"")

            # IO Commands I/O 命令
            case "type":
                system.require_args(1, command_args)
                file_loc = os.getcwd() + "\\" + command_args[0]
                with open(file_loc, encoding="UTF-8") as f:
                    system.info.normal_info(f.read())

            case "dir":
                print(f"----------Directory of \"{os.getcwd()}\"----------")
                for file_name in os.listdir(os.getcwd()):
                    file_loc = os.getcwd() + "\\" + file_name
                    file_last_write_date = datetime.fromtimestamp(os.stat(file_loc).st_mtime)
                    print(f"<{file_last_write_date}> {file_name} <File>")

            case "cd":
                system.require_args(1, command_args)
                os.chdir(command_args[0])

            case "mkdir":
                system.require_args(1, command_args)
                os.makedirs(os.getcwd() + "\\" + command_args[0])

            case "rmdir":
                system.require_args(1, command_args)
                if len(os.listdir(os.getcwd() + "\\" + command_args[0])):
                    shutil.rmtree(command_args[0])
                else:
                    os.rmdir(command_args[0])

            case "makefile":
                system.require_args(1, command_args)
                with open(os.getcwd() + "\\" + command_args[0], "a+", encoding="UTF-8") as f:
                    while 1:
                        text = input(" ...")
                        if text == "":
                            break
                        f.write(text + "\n")
                        system.write_log("Go on command. Input texts: " + text)

            case "rm":
                system.require_args(1, command_args)
                os.remove(os.getcwd() + "\\" + command_args[0])

            # Special Commands 特殊命令
            case "is_admin":
                if usr[account_logged_in][1] == "guest":
                    raise PermissionError("Have no enough permissions")
                system.info.normal_info("You are administrator!")

            case "HELLO_WORLD":
                system.info.error_info(system.consts.COMMAND_HELLO_WORLD_STRINGS)

            case _:
                raise system.MethodError(f"There's no method called \"{command_case if command_case != "" else "'NaS(\
Not a Statement)'"}\"")

        system.write_log(f"Use command: \"{command_case}\", args: {command_args}")

    except EOFError:
        print("EOF Exited.")
    except Exception as error:
        system.write_log(f"Use command failed: \"{command_case}\", args: {command_args}, cause \
by \"{str(error)}\"")
        system.info.error_info("Catch Runtime Error:", str(error))
