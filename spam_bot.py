"""Spam Bot"""
'Imports'
import pyautogui as pag
import customtkinter as ctk
import time
import sys

'Definitions'


def spam_start(text="[num]", count=1, enterKey="enter", timeSpace=0):
    if timeSpace < 0:
        print("[ERROR] invalid Syntax: timeSpace under 0")
        sys.exit()
    if type(timeSpace) != int:
        print("[ERROR] invalid Syntax: timeSpace is a", type(timeSpace), " | must be a int")
        sys.exit()
    if count <= 0:
        print("[ERROR] invalid Syntax: count under 1")
        sys.exit()
    if type(count) != int:
        print("[ERROR] invalid Syntax: count is a", type(count), " | must be a int")
        sys.exit()

    for numb in range(0, count):
        try:
            if "[num]" in text:
                text = text.replace("[num]", str(numb))
            pag.write(str(text))

            pag.press(enterKey)

            time.sleep(timeSpace)
        except:
            print("[ERROR] Invalid Syntax: error in text or enterKey")
            sys.exit()

time.sleep(1)
spam_start(count=10, text="Num: [num]")