"""Spam Bot"""
'Imports'
import pyautogui as pag
import customtkinter as ctk
import time
import sys

'Definitions'


def spam_start(rawText="[num]", count=1, enterKey="enter", timeSpace=0):
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
            pag.write(str(rawText.replace("[num]", str(numb + 1))), _pause=False)

            pag.press(enterKey)

            time.sleep(timeSpace)
        except:
            print("[ERROR] Invalid Syntax: error in text or enterKey")
            sys.exit()


if __name__ == '__main__':
    ctk.set_appearance_mode("System")
    ctk.set_default_color_theme("blue")

    main = ctk.CTk()
    main.geometry("700x320")

    frame = ctk.CTkFrame(master=main, width=700, height=320)
    frame.pack()

    # Variables
    rText = "[num]"
    timeDelay = 5
    counter = 1

    # for Text
    frame1 = ctk.CTkFrame(master=frame, width=680, bg_color="#2f2f2f", height=50)
    frame1.place(x=10, y=10)

    textEntry = ctk.CTkEntry(master=frame1, placeholder_text="use '[num]' for counter-output", width=570, height=40,
                             placeholder_text_color="grey")
    textEntry.place(x=100, y=5)

    lable1 = ctk.CTkLabel(master=frame1, text="Text:", width=60, height=40, text_font=("Calibri", 18))
    lable1.place(x=10, y=5)

    # for Time delay
    def time_delay(event):
        global timeDelay
        lable3.configure(text=str(round(event, 1)) + " sec.")
        timeDelay = round(event, 1)


    frame2 = ctk.CTkFrame(master=frame, width=680, bg_color="#2f2f2f", height=50)
    frame2.place(x=10, y=70)

    timeSlider = ctk.CTkSlider(master=frame2, width=450, from_=0, to=10, command=time_delay)
    timeSlider.place(x=130, y=20)

    lable2 = ctk.CTkLabel(master=frame2, text="Time delay:", width=60, height=40, text_font=("Calibri", 18))
    lable2.place(x=10, y=5)

    lable3 = ctk.CTkLabel(master=frame2, text="5.0 sec.", width=60, height=40, text_font=("Calibri", 16))
    lable3.place(x=600, y=5)

    # for counter
    frame3 = ctk.CTkFrame(master=frame, width=680, bg_color="#2f2f2f", height=50)
    frame3.place(x=10, y=130)

    countEntry = ctk.CTkEntry(master=frame3, placeholder_text="how often the message will send", width=570, height=40,
                              placeholder_text_color="grey")
    countEntry.place(x=100, y=5)

    lable4 = ctk.CTkLabel(master=frame3, text="Count:", width=60, height=40, text_font=("Calibri", 18))
    lable4.place(x=10, y=5)

    # for enterKey
    frame4 = ctk.CTkFrame(master=frame, width=680, bg_color="#2f2f2f", height=50)
    frame4.place(x=10, y=190)

    keys = open("key.txt", "r").read().replace("'", "").replace("[", "").replace("]", "").split(",")

    keyEntry = ctk.CTkOptionMenu(master=frame4, width=300, height=40, values=keys, text_font=("Calibri", 16),
                                 dynamic_resizing=True)
    keyEntry.place(x=130, y=5)
    keyEntry.set("entre")

    lable5 = ctk.CTkLabel(master=frame4, text="Enter Key:", width=60, height=40, text_font=("Calibri", 18))
    lable5.place(x=10, y=5)

    # Button
    button = ctk.CTkButton(master=frame, width=660, height=50, text="START", text_font=("Calibri", 18)).place(x=20, y=260)

    main.mainloop()
