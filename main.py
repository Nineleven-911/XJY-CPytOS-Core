import base64
import json
import os
import pathlib
import time
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

is_login = False

# Variables Defining Ends

# Initiation for Nuitka (为Nuitka的初始化，因为Nuitka的处理逻辑是: 不用到，不打包)
colorama.init()
os.system("cls" if os.name == "nt" else "clear")
usr, os_ver = system.read_config()
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

while 1:
    try:
        command = input(" >>>")
        # Split command
        command_case = "NaS"
        command_parameters = []
        if "(" not in command and ")" not in command:
            command_case = command
        else:
            command_case = command[:command.find("(")]
            command_parameters: list = command[command.find("(") + 1:command.find(")")].split(",")

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
                system.info.normal_info("Config info:", os_ver, " System info: \
XJY-CPython Operating System Core <0.01.0> \nOS Version: Alpha Build 00101.03067.19377.11001")
            case "exit":
                system.info.normal_info("You can close the Operating-System now.")
                break
            case "tips":
                system.info.normal_info(random.choice(system.consts.TIPS))

            case "HELLO_WORLD":
                system.info.error_info(system.consts.COMMAND_HELLO_WORLD_STRINGS)

            # User Commands 用户命令
            case "relogin":
                system.info.normal_info("Login status be turned to: non_login")
                account_logged_in = func.user.login(usr)

            # Applications Commands 软件命令
            case "apps_list":
                print(f"----------Directory of \"{os.getcwd()+"\\Program Files (p3.12)"}\"----------")
                for file_name in os.listdir(os.getcwd()+"\\Program Files (p3.12)"):
                    file_loc = os.getcwd() + "\\Program Files (p3.12)\\" + file_name
                    file_last_write_date = datetime.fromtimestamp(os.stat(file_loc).st_mtime)
                    print(f"<{file_last_write_date}> {file_name} <xOS Application>")

            case "run":
                system.require_args(1, command_parameters)
                app_name = command_parameters[0]
                if app_name not in os.listdir(os.getcwd()+"\\Program Files (p3.12)\\"):
                    raise FileNotFoundError(f"Can't find an application called \"{app_name}\"")
                elif account_logged_in == "guest":
                    raise PermissionError("Have no enough permissions")
                os.system(f"python \"{os.getcwd()+"\\Program Files (p3.12)\\"+app_name}\"")

            # Storage Commands 存储空间命令

            # Special Commands 特殊命令
            case "is_admin":
                if account_logged_in == "guest":
                    raise PermissionError("Have no enough permissions")
                system.info.normal_info("You are administrator!")

            case _:
                raise system.MethodError(f"There's no method called \"{command_case if command_case != "" else "'NaS(\
Not a Statement)'"}\"")

        system.write_log(f"Use command: \"{command_case}\", args: \"{command_parameters}\"")

    except Exception as error:
        system.write_log(f"Use command failed: \"{command_case}\", args: \"{command_parameters}\", cause \
by \"{error}\"")
        system.info.error_info("Catch Runtime Error:", str(error))
