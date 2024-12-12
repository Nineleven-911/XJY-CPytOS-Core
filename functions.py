# -*- coding: utf-8 -*- 

import os

import system


class user:  # 账号类
    @staticmethod
    def login(usr):
        if usr == {}:  # 判断是否有账号
            system.info.warning_info("No account.")  # 输出警告信息
            system.write_log("Login failed. No account.")  # 输出日志
            return "Guest"  # 返回账号名称  # 返回账号名称
        # 登录
        print("Login: \nGuest account name: Guest, password: 1234\nAccounts:")  # 输出所有账号
        for i in usr.items():  # 输出所有账号 
            print(i[0], end=" ")  # 输出账号名
        print()  # 换行
        while 1:  # 循环
            acc_name = input("\nAccount name: ")  # 输入账号名
            if acc_name not in usr.keys():  # 判断账号名是否存在
                system.info.warning_info("Invalid account name.")  # 输出警告信息
                system.write_log(f"Login failed. Input account name: \"{acc_name}\"")  # 输出日志
                continue  # 继续循环
            pwd = input("Password:")  # 输入密码
            if usr[acc_name][0] != pwd:  # 判断密码是否正确
                system.info.warning_info("Invalid account password, password:", pwd)  # 输出警告信息
                system.write_log(f"Login failed. Input password: \"{pwd}\"")  # 输出日志
                continue  # 继续循环
            # 登录成功,返回账号名
            os.system("cls" if os.name == "nt" else "clear")  # 清屏
            system.info.normal_info(system.consts.OS_ICON, "\n" + "-" * 30 + "\n")  # 输出提示信息
            system.info.normal_info("Welcome!", acc_name)  # 输出提示信息
            system.write_log(f"Login success. Login account: \"{acc_name}\"")  # 输出日志
            return acc_name  # 返回账号名
