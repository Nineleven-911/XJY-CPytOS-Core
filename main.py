import base64
import json
import os
import pathlib
import time
import colorama
import random
# import pwinput

import system

# Init 初始化部分

# Initiation for Nuitka (为Nuitka的初始化，因为Nuitka的处理逻辑是: 不用到，不打包)

colorama.init()
os.system("cls" if os.name == "nt" else "clear")
usr, os_ver = system.read_config()
print(
    fr"""XJY-DOS <Alpha 0.02.0 Remake>
[Development Version]: Build in XJY-CPython Operating System Core Version <0.01.0>
{system.consts.OS_ICON}
""")
system.information.information_info("[OS]: Need login(Catch exception) - [xjy.os.status.exception.need_login]")
# Initiation ends
# Login 登录账户部分

print("Login: \nGuest account name: guest, password: PWD\nAccounts:")
for i in usr.items():
    print(i[0], end=" ")
while 1:
    acc_name = input("\nAccount name: ")
    if acc_name not in usr.keys():
        system.information.warning_info("Invalid account name.")
        continue
    pwd = input("Password:")
    if usr[acc_name] != pwd:
        system.information.warning_info("Invalid account password, password:", pwd)
        continue
    system.information.information_info("Welcome!", acc_name)
    break

# Main Loop 主循环
system.information.information_info("[OS]:Login status TRUE, Accepted Login.")
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
                system.information.information_info("Config information:", os_ver, " System information: \
XJY-CPython Operating System Core <0.01.0> \nOS Version: Alpha Build 00101.03067.19377.11001")
            case "exit":
                system.information.information_info("You can close the Operating-System now.")
                break
            case "tips":
                system.information.information_info(random.choice(system.consts.TIPS))
                raise IOError
            case "HELLO_WORLD":
                system.information.error_info(system.consts.COMMAND_HELLO_WORLD_STRINGS)

            case _:
                raise system.MethodError(f"There's no method called \"" + command_case + "\"")

    except Exception as error:
        print("Catch Runtime Error:", error)
