# -*- coding: utf-8 -*-

import base64
import json
import time

import colorama


class consts:
    OS_ICON = r""" __  __      _  __   __           ____   ____     ___    ____       ____                       
 \ \/ /     | | \ \ / /          / ___| |  _ \   / _ \  / ___|     / ___|   ___    _ __    ___ 
  \  /   _  | |  \ V /   _____  | |     | |_) | | | | | \___ \    | |      / _ \  | '__|  / _ \
  /  \  | |_| |   | |   |_____| | |___  |  __/  | |_| |  ___) |   | |___  | (_) | | |    |  __/
 /_/\_\  \___/    |_|            \____| |_|      \___/  |____/     \____|  \___/  |_|     \___|"""

    NEW_OS_ICON_0_04_0 = r"""___  _    _ ___  _       ____  ____  ____  ____    ____  ____  ____  _____
\  \//   / |\  \//      /   _\/  __\/  _ \/ ___\  /   _\/  _ \/  __\/  __/
 \  /    | | \  / _____ |  /  |  \/|| / \||    \  |  /  | / \||  \/||  \
 /  \ /\_| | / /  \____\|  \__|  __/| \_/|\___ |  |  \__| \_/||    /|  /_
/__/\\\____//_/         \____/\_/   \____/\____/  \____/\____/\_/\_\\____\ """

    TIPS = ["Try command 'HELLO_WORLD'!", "If you like this, try Professional version of XJY-CPytOS!", "Ooh~Everybody \
is Kong Fu fighting~", "Welcome to my world~ renew your definition~", "Chinese catchphrase: Dead pigs are not afraid \
of boiling water's hot!", "Do you know Python is different of any programming languages?", "Say \"Hello, World!\" to \
programming languages!", "The shirt costs 9 pound 15 pence!", "Steven He: EMOTIONAL DAMAGE!?", "Click here to add text\
s...", "", "Something wrong...", "Trans_back (more recent cell lost): ("]

    COMMAND_HELLO_WORLD_STRINGS = r"""Traceback (most recent call last):
    File "D:\helloworld.py", line 1, in <module>
        print("Hello, Word!")
    ^^^^^^^^^^^^^^^^^^^^^^^^^
IndentationError: unexpected indent
    
    
> Process 'command 'D:\Java\jdk-23\bin\java.exe'' finished with non-zero exit value -1
    
* Try:
> Run with --stacktrace option to get the stack trace.
> Run with --info or --debug option to get more log output.
> Run with --scan to get full insights.
> Get more help at https://help.gradle.org.
BUILD FAILED in 2m 26s
1 actionable tasks: 1 executed
    
    
error C1145141919810: ----------
 1 >已完成生成项目“a.vcxproj”的操作 - 失败。
========== 生成: 0 成功，1 失败，0 最新，0 已跳过 ==========
========== 生成 于 21:16 完成，耗时 00.797 秒 =========="""
    xChar = {
        # 数字区 01-0A
        "1": "01", "2": "02", "3": "03", "4": "04", "5": "05", "6": "06", "7": "07", "8": "08", "9": "09", "0": "0A",
        # 大写字母区 0B-24
        "A": "0B", "B": "0C", "C": "0D", "D": "0E", "E": "0F", "F": "10", "G": "11", "H": "12", "I": "13", "J": "14",
        "K": "15", "L": "16", "M": "17", "N": "18", "O": "19", "P": "1A", "Q": "1B", "R": "1C", "S": "1D", "T": "1E",
        "U": "1F", "V": "20", "W": "21", "X": "22", "Y": "23", "Z": "24",
        # 小写字母区 25-3E
        "a": "25", "b": "26", "c": "27", "d": "28", "e": "29", "f": "2A", "g": "2B", "h": "2C", "i": "2D", "j": "2E",
        "k": "2F", "l": "30", "m": "31", "n": "32", "o": "33", "p": "34", "q": "35", "r": "36", "s": "37", "t": "38",
        "u": "39", "v": "3A", "w": "3B", "x": "3C", "y": "3D", "z": "3E",
        # 英文特殊符号区 3F-4C
        ".": "3F", "!": "40", "?": "41", "\"": "42", "'": "43", "(": "44", ")": "45", " ": "46",
        "\\": "47", "/": "48", "<": "49", ">": "4A", ",": "4B", ":": "4C"
    }


class MethodError(Exception):
    def __init__(self, method_name):
        pass


class ParametersNotFoundError(Exception):
    def __init__(self, texts):
        pass


# Class Defining Ends


"""def b64dec(text: str):
    return str(base64.b64decode(eval(f"b'{text}'")))[2:-1]


def b64enc(text: str):
    return str(base64.b64encode(eval(f"b'{text}'")))[2:-1]"""

# 定义解密字典
xChar_inv = {v: k for k, v in consts.xChar.items()}


# 加密函数
def encrypt(text):
    encrypted_text = ''
    for char in text:
        if char in consts.xChar:
            encrypted_text += consts.xChar[char]
        else:
            encrypted_text += char  # 对于不在字典中的字符，保持原样
    return encrypted_text


# 解密函数
def decrypt(encoded_text):
    decrypted_text = ''
    for i in range(0, len(encoded_text), 2):
        code = encoded_text[i:i + 2]
        if code in xChar_inv:
            decrypted_text += xChar_inv[code]
        else:
            decrypted_text += code  # 对于不在字典中的编码，保持原样
    return decrypted_text


def require_args(nums: int, args: list):
    if len(args) != nums:
        raise ParametersNotFoundError(f"Parameters requires: {nums}, found: {len(args)}")
    else:
        return 0


def read_config():
    """
    Example:
    Admin:qwerty?admin,Guest:1234?guest

    Result:
    {"Admin": ("qwerty","admin"), "Guest": ("1234", "guest")}
    """
    users = {}  # 使用字典来存储用户信息
    with open("SAM", encoding="utf-8") as file:
        text = decrypt(file.read())
    for grp in text.split(","):
        # 分割用户名、密码和用户组
        # Example: Admin:qwerty?admin
        name = grp[:grp.find(":")]
        pwd = grp[grp.find(":")+1:grp.find("?")]
        group = grp[grp.find("?")+1:]
        users[name] = (pwd, group)
    return users


def write_log(*value, is_new=False):
    with open("runtime.log", "a", encoding="utf-8") as file:
        for text in value:
            txt = f"[{time.strftime("%Y-%m-%d-%H:%M:%S", time.localtime())}] "
            file.write(txt + str(text) if not is_new else "-" * 10 + " " + txt + "-" * 10)
            file.write("\n")


class info:
    @staticmethod
    def error_info(*values, sep: str = " ", end: str = "\n"):
        for i in values:
            print(colorama.Fore.RED + i, end=sep)
        print(colorama.Fore.RESET, end=end)

    @staticmethod
    def warning_info(*values, sep: str = " ", end: str = "\n"):
        for i in values:
            print(colorama.Fore.YELLOW + i, end=sep)
        print(colorama.Fore.RESET, end=end)

    @staticmethod
    def normal_info(*values, sep: str = " ", end: str = "\n"):
        print(colorama.Fore.RESET, end="")
        for i in values:
            print(i, end=sep)
        print(end=end)


class Loadingbar:
    class Classics:
        def __init__(self):
            self._shape = ["<", ">", "=", 0, 10, 0]
            self._runningtime = 1

        def setAttribute(self, start: str = "<", end: str = ">", middle: str = "=", minvalue: int = 0,
                         maxvalue: int = 10, value: int = 0):
            self._shape = [start, end, middle, minvalue, maxvalue, value]

        def sleeptime_use(self):
            # Rules: Sleep Time=self._shape[4]*self._runningtime+1 #
            print(self._shape[0], end="")
            time.sleep(self._runningtime)
            for i in range(self._shape[4]):
                print(self._shape[2], end="")
                time.sleep(self._runningtime)
            print(self._shape[1])

        def processuse(self):
            if self._shape[5] == 0:
                print(self._shape[0], end="")
            elif self._shape[5] == self._shape[4]:
                print(self._shape[1], end="")
            elif self._shape[3] <= self._shape[5] <= self._shape[4]:
                print(self._shape[2], end="")
            else:
                self._shape[-1] += 1
                raise IndexError(f"Loading Bar object {self} index out of range.")
            self._shape[-1] += 1

    class Rollings:
        def __init__(self):
            self._shape = ["-", "/", "|", "\\"]
            self._rollingAllTimes = 50
            self._sleepTime = 0.2

        def setAttribute(self, shape_list: list, rollingAllTimes: int = 10, sleepTime: float = 0.4):
            self._shape = shape_list
            self._sleepTime = sleepTime
            self._rollingAllTimes = rollingAllTimes

        def use(self):
            lenOfList = len(self._shape)
            for i in range(self._rollingAllTimes):
                print(self._shape[i % lenOfList], end="", flush=True)
                time.sleep(self._sleepTime)
                print("\b" * len(self._shape[i % lenOfList]), end="", flush=True)
