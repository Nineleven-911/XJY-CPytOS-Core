# -*- coding: utf-8 -*-

import os

import system


class user:
    @staticmethod
    def login(usr):
        print("Login: \nGuest account name: guest, password: PWD\nAccounts:")
        for i in usr.items():
            print(i[0], end=" ")
        while 1:
            acc_name = input("\nAccount name: ")
            if acc_name not in usr.keys():
                system.info.warning_info("Invalid account name.")
                system.write_log(f"Login failed. Input account name: \"{acc_name}\"")
                continue
            pwd = input("Password:")
            if usr[acc_name][0] != pwd:
                system.info.warning_info("Invalid account password, password:", pwd)
                system.write_log(f"Login failed. Input password: \"{pwd}\"")
                continue
            os.system("cls" if os.name == "nt" else "clear")
            system.info.normal_info(system.consts.OS_ICON, "\n" + "-" * 30 + "\n")
            system.info.normal_info("Welcome!", acc_name)
            system.write_log(f"Login success. Login account: \"{acc_name}\"")
            return acc_name
