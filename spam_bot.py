"""Spam Bot"""
'Imports'
import pyautogui as pag
import customtkinter as ctk
import time
import sys
import _thread
import tkinter
import tkinter.messagebox
import keyboard

'Definitions'


def spam_start(rawText="[num]", count=1, enterKey="enter", timeSpace=0):
    if timeSpace < 0:
        print("[ERROR] invalid Syntax: timeSpace under 0")
        sys.exit()
    if type(timeSpace) != int and type(timeSpace) != float:
        print("[ERROR] invalid Syntax: timeSpace is a", type(timeSpace), " | must be a int or float")
        sys.exit()
    if count <= 0:
        print("[ERROR] invalid Syntax: count under 1")
        sys.exit()
    if type(count) != int:
        print("[ERROR] invalid Syntax: count is a", type(count), " | must be a int")
        sys.exit()

    for numb in range(0, count):
        try:
            time.sleep(timeSpace / 2)

            pag.write(str(rawText.replace("[num]", str(numb + 1))), _pause=False)

            time.sleep(timeSpace / 2)

            pag.press(enterKey)
        except:
            print("[ERROR] Invalid Syntax: error in text or enterKey")
            sys.exit()


if __name__ == '__main__':
    ctk.set_appearance_mode("System")
    ctk.set_default_color_theme("blue")

    main = ctk.CTk()
    main.geometry("700x320")
    main.title("SpamBot")
    main.iconbitmap('Logo256x256.ico')

    frame = ctk.CTkFrame(master=main, width=700, height=320)
    frame.pack()

    # Variables
    rText = tkinter.StringVar()
    cText = tkinter.StringVar()
    timeDelay = 5
    counter = 1
    enterKey = "enter"


    # dfinitions
    def button_text():
        global rText, cText, timeSlider, newKeyButon, button1, textEntry, countEntry, timeDelay, enterKey
        time.sleep(1)
        button1.configure(text="Start in 4 sec.")
        time.sleep(1)
        button1.configure(text="Start in 3 sec.")
        time.sleep(1)
        button1.configure(text="Start in 2 sec.")
        time.sleep(1)
        button1.configure(text="Start in 1 sec.")
        time.sleep(1)
        button1.configure(text="Spamming...")

        try:
            spam_start(rawText=textEntry.get(), count=int(countEntry.get()), enterKey=enterKey,
                       timeSpace=timeDelay)
        except:
            tkinter.messagebox.showwarning("Error", "Input Error: check your Entry boxes \n Text: should be a string "
                                                    "\n Count: should be a int")

        EnableButton()

    def EnableButton():
        newKeyButon.configure(state="normal", fg_color="#1F6AA5", text=f"Current Key: <{enterKey}>")
        timeSlider.configure(state="normal", button_color="#1F6AA5", progress_color="#AAB0B5")
        textEntry.configure(state="normal", text_color="#ffffff")
        countEntry.configure(state="normal", text_color="#ffffff")
        button1.configure(state="normal", fg_color="#1F6AA5", text="Start")

    def DisableButton():
        global textEntry, timeSlider, countEntry, button1, newKeyButon
        newKeyButon.configure(state="disabled", fg_color="#1F2AA2", text="[Loading...]")
        timeSlider.configure(state="disabled", button_color="#2f2f2f", progress_color="#1f1f1f")
        textEntry.configure(state="disabled", text_color="#9f9f9f")
        countEntry.configure(state="disabled", text_color="#9f9f9f")
        button1.configure(state="disabled", fg_color="#1F2AA2", text="[Loading...]")


    def start():
        global enterKey
        DisableButton()
        button1.configure(text="Start in 5 sec.")
        newKeyButon.configure(text=f"Pressing <{enterKey}> after every message.")
        _thread.start_new_thread(button_text, ())


    def ReadKeyboardInput():
        global newKeyButon, button1, enterKey
        DisableButton()
        button1.configure(text="Can't start. Waiting for Keyboard input")
        newKeyButon.configure(text="Waiting for Keyboard input. Press any key you want to.")
        _thread.start_new_thread(ReadKeyboardInputThread, ())

    def ReadKeyboardInputThread():
        global enterKey
        enterKey = keyboard.read_event(suppress=True).name
        EnableButton()

    # for Text
    frame1 = ctk.CTkFrame(master=frame, width=680, bg_color="#2f2f2f", height=50)
    frame1.place(x=10, y=10)

    textEntry = ctk.CTkEntry(master=frame1, placeholder_text="use '[num]' for counter-output", width=570, height=40,
                             placeholder_text_color="grey")  # , text_font=("Calibri", 14)
    textEntry.place(x=100, y=5)

    lable1 = ctk.CTkLabel(master=frame1, text="Text:", width=60, height=40)  # , text_font=("Calibri", 18)
    lable1.place(x=10, y=5)


    # for Time delay
    def time_delay(event):
        global timeDelay
        lable3.configure(text=str(round(event, 2)) + " sec.")
        timeDelay = round(event, 2)


    frame2 = ctk.CTkFrame(master=frame, width=680, bg_color="#2f2f2f", height=50)
    frame2.place(x=10, y=70)

    timeSlider = ctk.CTkSlider(master=frame2, width=450, from_=0, to=10, command=time_delay)
    timeSlider.place(x=130, y=20)

    lable2 = ctk.CTkLabel(master=frame2, text="Time delay:", width=60, height=40)  # , text_font=("Calibri", 18)
    lable2.place(x=10, y=5)

    lable3 = ctk.CTkLabel(master=frame2, text="5.00 sec.", width=60, height=40)  # , text_font=("Calibri", 16)
    lable3.place(x=600, y=5)

    # for counter
    frame3 = ctk.CTkFrame(master=frame, width=680, bg_color="#2f2f2f", height=50)
    frame3.place(x=10, y=130)

    countEntry = ctk.CTkEntry(master=frame3, placeholder_text="how often the message will send", width=570, height=40,
                              placeholder_text_color="grey")  # , text_font=("Calibri", 14)
    countEntry.place(x=100, y=5)

    lable4 = ctk.CTkLabel(master=frame3, text="Count:", width=60, height=40)  # , text_font=("Calibri", 18)
    lable4.place(x=10, y=5)

    # for enterKey
    frame4 = ctk.CTkFrame(master=frame, width=680, bg_color="#2f2f2f", height=50)
    frame4.place(x=10, y=190)

    # keys = open("key.txt", "r").read().replace("'", "").replace("[", "").replace("]", "").replace(" ", "").split(",")

    newKeyButon = ctk.CTkButton(master=frame4, command=ReadKeyboardInput, width=570, height=40,
                                text=f"Current Key: <{enterKey}>")
    newKeyButon.place(x=100, y=5)

    lable5 = ctk.CTkLabel(master=frame4, text="Enter Key:", width=60, height=40)  # , text_font=("Calibri", 18)
    lable5.place(x=10, y=5)

    # Button
    button1 = ctk.CTkButton(master=frame, width=660, height=50, text="START",
                            command=start)  # , text_font=("Calibri", 18)
    button1.place(x=20, y=260)

    main.mainloop()
