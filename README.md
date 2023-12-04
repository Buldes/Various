# Various python programs

 ***

## List
#### - sys_info.py
#### - spam_bot.py

 --- 

## About



### sys_info.py
_sys_info.py_ is modul (using _psutil_), that gives you these following information about your pc:
+ cpu statics
+ disk statics
+ memory statics

Every function returns a list:

+ cpu = (cpu_usage, cpu_temperature)
+ disk = (free, total)
+ memory = (free, total)

It will automatically return it in GB, but you can manually set ist to bytes using `[function](to_GB = False)`

### spam_bot.py
_spam_bot.py_ is a python programmed spam-bot using _customtkinter_ for the UI and _pyautogui_ for the spamming.

 **How to use:**
 
You will find these following things:
+ _Text_ - Entry
+ _Time delay_ - Slider 
+ _Count_ - Entry
+ _Enter Key_ - Button

This is what they do:
+ _Text_: This is the text, that will write. You can use `[num]` for the _counter_ output.
+ _Time delay_: This is the Time between every single periode. For example if the time delay is 1 sec.: _wait 0.5 sec. > writes text > wait 0.5 sec. > presse "Enter Key"_
+ _Count_: This is how often the text will send. You have to write an _int_ in the entry.
+ _Enter Key_: This is the Key, that will press, after the text is written.

You can also use the function _spam_start()_ in your own project like at _sys_info.py_. Just import it.

**What _spam_start()_ do and how to configure:**
+ _spam_start()_ starts the spam and end until its over.

__Configure:__

This is the normal configuration:

``spam_start(rawText="[num]", count=1, enterKey="enter", timeSpace=0)``

The names are nearly the same as in the UI...
+ rawText = _Text_
+ count = _Count_
+ enterKey = _Enter Key_
+ timeSpace = _Time Delay_

... and it also does the exact same thing. (Read _"spam_bot.py" > "How to use"_ to understand if you don't read it)