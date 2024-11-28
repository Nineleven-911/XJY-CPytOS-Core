import base64
import json
import os
import pathlib
import time
import colorama
import random
import tqdm
# import pwinput

import system

# Init 初始化部分
system.write_log(None, is_new=True)

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

print("Login: \nGuest account name: guest, password: PWD\nAccounts:")
for i in usr.items():
    print(i[0], end=" ")
while 1:
    acc_name = input("\nAccount name: ")
    if acc_name not in usr.keys():
        system.info.warning_info("Invalid account name.")
        continue
    pwd = input("Password:")
    if usr[acc_name] != pwd:
        system.info.warning_info("Invalid account password, password:", pwd)
        continue
    os.system("cls" if os.name == "nt" else "clear")
    system.info.normal_info(system.consts.OS_ICON, "\n" + "-" * 30 + "\n")
    system.info.normal_info("Welcome!", acc_name)
    break

# Main Loop 主循环
system.info.normal_info("[OS]:Login status TRUE, Accepted Login.")
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

            case _:
                raise system.MethodError(f"There's no method called \"{command_case if command_case != "" else "'NaS(\
Not a Statement)'"}\"")

    except Exception as error:
        system.info.error_info("Catch Runtime Error:", str(error))
