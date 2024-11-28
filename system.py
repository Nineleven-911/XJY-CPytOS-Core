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
s...", ""]

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


class MethodError(Exception):
    def __init__(self, method_name):
        pass


# Class Defining Ends


def b64dec(text: str):
    return str(base64.b64decode(eval(f"b'{text}'")))[2:-1]


def b64enc(text: str):
    return str(base64.b64encode(eval(f"b'{text}'")))[2:-1]


def read_config():
    with open("config.json") as file:
        config: dict = json.loads(file.read())

    users: dict = {}
    py_os_core_ver = "Non-Available"

    for key, value in config.items():
        match key:
            case "__comments__":
                continue
            case "py_osc_v":
                py_os_core_ver = value
            case "user":
                for user_name, base64_password in value.items():
                    users[user_name] = b64dec(base64_password)

    return users, py_os_core_ver


def write_log(*value, is_new=False):
    with open("runtime.log", "a") as file:
        for text in value:
            txt = f"[{time.strftime("%Y-%m-%d-%H:%M:%S", time.localtime())}] "
            file.write(txt+str(text) if not is_new else "-"*10+" "+txt+"-"*10)
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
