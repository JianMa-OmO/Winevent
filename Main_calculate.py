# By Beiyu
# Modification time 2025.3.15
# This is main is file first(calc) 
import platform
import wmi
from tkinter import messagebox, Tk, ttk
import requests
import os


w = wmi.WMI()
activatecommand = ["slmgr /ipk W269N-WFGWX-YVC9B-4J6C9-T83GX","slmgr /skms kms.loli.best","slmgr /ato"]

# 获取Windows版本号，如10.0.26100
def Windows_v():
    return platform.version()

# 获取Windows版本，如Windows11
def Windows_e():
    return platform.release()

# 获取电脑制造商名称，如Thunder
def computer_manufacturer():
    return w.Win32_ComputerSystem()[0].Manufacturer


def computer_model():
    return w.Win32_ComputerSystem()[0].Model

def processor_name():
    return platform.processor()


def processor_acchitecture():
    return list(platform.architecture())


def mainboard_n():
    return ''.join(mbn.SerialNumber.strip() for mbn in w.Win32_BaseBoard())


def bios_n():
    return ''.join(biosn.SerialNumber.strip() for biosn in w.Win32_BIOS())


def hard_n():
    return ''.join(hardn.SerialNumber for hardn in w.Win32_DiskDrive())

def vermessage():
    messagebox.showinfo(title="版本", message="版本v1.1.4。")


def cleanpowercfg():
    import os
    os.system("powercfg -h off")
    messagebox.showinfo(title="提示", message="清除文件已关闭。")

def actiave():
    for a in activatecommand:
        os.system(a)

# 下载函数
def download(whatdownload):
    __all_download = {"python" : "https://mirrors.huaweicloud.com/python/3.13.2/python-3.13.2.exe",
                      "jdk" : "https://repo.huaweicloud.com:8443/artifactory/java-local/jdk/13+33/jdk-13_windows-x64_bin.exe",
                      "000-激活-win11" : lambda : actiave()}
    if whatdownload not in __all_download.keys():
        messagebox.showerror("下载","没有找到下载源。")
    elif not  whatdownload == "000-激活-win11":
        # 下载文件      
        f = requests.get(__all_download[whatdownload])
        with open("E:\one user\Code\python\Winevent/{}.exe".format(whatdownload),"wb") as d:
            d.write(f.content)
        messagebox.showinfo("下载","下载完毕，已保存至程序文件夹！")