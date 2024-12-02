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
usr = system.read_config()
print(
    fr"""XJY-DOS <Alpha 0.02.0 Remake>
[Development Version]: Build in XJY-CPython Operating System Core Version <0.01.0>
{system.consts.OS_ICON}
""")
system.info.normal_info("[OS]: Need login(Catch exception) - [xjy.os.status.exception.NeedLoginException]")

# Initiation ends

# Login 登录账户部分

account_logged_in = func.user.login(usr)

# Main Loop 主循环
command_case = ""
command_args = []
while 1:
    try:
        command = input(" >>>")
        # Split command
        command_case = "NaS"
        command_args = []
        if "(" not in command and ")" not in command:
            command_case = command
        else:
            command_case = command[:command.find("(")]
            command_args: list = command[command.find("(") + 1:command.rfind(")")].split(",")

        # Judge 判断指令

        """
        # It will be executed if there's a prefix in command. 当命令有前缀时, 激活此处判断语句
        if "." in command_case:
            command_without_prefix = command_case[command.find(".") + 1:]
            if command[:command.find(".")] == "os":
                match command_without_prefix:
                    case "version":
                    pass

            continue"""

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

            # User Commands 用户命令
            case "relogin":
                system.write_log("Login status be turned to: non_login")
                account_logged_in = func.user.login(usr)

            case "logining":
                system.info.normal_info(account_logged_in)

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
                elif account_logged_in == "guest":
                    raise PermissionError("Have no enough permissions")
                os.system(f"python \"{os.getcwd() + "\\Program Files (p3.12)\\" + app_name}\"")

            # IO Commands I/O 命令
            case "text":
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
                os.remove(os.getcwd()+"\\"+command_args[0])

            # Special Commands 特殊命令
            case "is_admin":
                if account_logged_in == "guest":
                    raise PermissionError("Have no enough permissions")
                system.info.normal_info("You are administrator!")

            case "HELLO_WORLD":
                system.info.error_info(system.consts.COMMAND_HELLO_WORLD_STRINGS)

            case _:
                raise system.MethodError(f"There's no method called \"{command_case if command_case != "" else "'NaS(\
Not a Statement)'"}\"")

        system.write_log(f"Use command: \"{command_case}\", args: {command_args}")

    except Exception as error:
        system.write_log(f"Use command failed: \"{command_case}\", args: {command_args}, cause \
by \"{error}\"")
        system.info.error_info("Catch Runtime Error:", str(error))
