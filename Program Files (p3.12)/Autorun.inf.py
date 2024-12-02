import time
from pynput import keyboard

with open("autorun.txt", encoding="UTF-8") as file:
    text = file.read()
keyboard = keyboard.Controller()
keyboard.type(text)