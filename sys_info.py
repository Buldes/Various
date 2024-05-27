"""System Infos"""
'Imports'
import psutil
import os
import subprocess

'Definitions'


# CPU
def get_cpu():
    if os.name == "posix":
        cpu_temp_every = str(psutil.sensors_temperatures())
        cpu_temp = cpu_temp_every[42:47]
        cpu_usage = str(psutil.cpu_percent())
        return cpu_usage, cpu_temp.replace("=", "")
    else:
        cpu_usage = str(psutil.cpu_percent())
        return cpu_usage


# Memory/Ram
def get_memory(to_GB=True, round_num=1):
    memory = psutil.virtual_memory()
    if to_GB:
        available = round(memory.available / 1000.0**3, round_num)
        total = round(memory.total / 1000.0**3, round_num)
    else:
        available = round(memory.available, round_num)
        total = round(memory.total, round_num)
    return available, total


# disk
def get_disk(to_GB=True, round_num=1):
    disk = psutil.disk_usage("/")
    if to_GB:
        free = round(disk.free / 1000.0 / 1000.0 / 1000, round_num)
        total = round(disk.total / 1000.0 / 1000.0 / 1000, round_num)
    else:
        free = round(disk.free, round_num)
        total = round(disk.total, round_num)
    return free, total

def get_voltage():
    return subprocess.run(["sudo", "vcgencmd", "measure_volts"], capture_output=True).stdout.decode()[5:9]

def info():
    print("************************************** \n"
          "             -sys_info-             \n"
          "disk_statistic(to_GB, round_num):\n"
          "   return list (free, total)\n"
          "    of disk\n"
          "\n"
          "memory_statistic(to_GB, round_num):\n"
          "   return list (available, total)\n"
          "    of memory\n"
          "\n"
          "get_cpu():\n"
          "   return list (usage in %, temperature)\n"
          "\n"
          "get_voltage():\n"
          "    return value of current voltage of the system (fr rasppbery)"
          "\n"
          "to_GB:\n"
          "   converts to GB\n"
          "\n"
          "round_num:\n"
          "   round the number\n"
          "**************************************")


if __name__ == '__main__':
    'Windows'
    if os.name == 'nt':
        import tkinter as tk
        import _thread
        import time

        # Frame erstellen
        main = tk.Tk()
        main.title("Statistic")
        main.configure(bg="#000000")


        def config():
            while 1:
                time.sleep(0.5)
                cpu_lable.configure(text="CPU: " + str(get_cpu()) + "%")
                memory.configure(
                    text="MEMORY: " + str(round(get_memory()[0], 1)) + " / " + str(
                        get_memory()[1]) + "GB")
                disk.configure(text="DISK: " + str(get_disk()[0]) + " / " + str(get_disk()[1]) + "GB")


        # Lable
        sys_info = tk.Label(bg="#090909", width=20, height=2, fg="#ffffff", text="-sys_info-", font=10)
        sys_info.pack()

        cpu_lable = tk.Label(bg="#0a0a0a")
        cpu_lable.configure(width=25, height=2, fg="#ffffff", text="Load...")
        cpu_lable.pack()

        memory = tk.Label(bg="#0a0a0a")
        memory.configure(width=25, height=2, fg="#ffffff", text="Load...")
        memory.pack()

        disk = tk.Label(bg="#0a0a0a")
        disk.configure(width=25, height=2, fg="#ffffff", text="Load...")
        disk.pack()

        _thread.start_new_thread(config, ())

        main.mainloop()

    if os.name == 'posix':
        import time

        info()
        time.sleep(0.5)
        while True:
            print("---------sys_info---------")
            print("cpu_usage:", get_cpu()[0], "%")
            print("cpu_temp:", get_cpu()[1], "°C")
            print("memory:" + str(get_memory()[0]) + "/" + str(get_memory()[1]))
            print("disk:" + str(get_disk()[0]) + "/" + str(get_disk()[1]))
            print("voltage:" + str(get_voltage()) + "V")
            print("--------------------------")
            time.sleep(1)
