# coding=utf-8
# 编写由gihub:JianMa OmO 
# 最后修改时间2024/4/5
import platform
import wmi
from tkinter import messagebox, Tk, ttk
import requests
import os


w = wmi.WMI()

# 获取Windows版本号，如10.0.26100
def Windows_v():
    return platform.version()

# 获取Windows版本，如Windows11
def Windows_e():
    return platform.release()

# 获取电脑制造商名称，如Thunderobot
def computer_manufacturer():
    return w.Win32_ComputerSystem()[0].Manufacturer

# 获取电脑型号，如Thunderbook16
def computer_model():
    return w.Win32_ComputerSystem()[0].Model

# 获取处理器名称，如Intel64 Famliy Model 186 setpping 2
def processor_name():
    return platform.processor()

# 获取处理器架构，如64bit
def processor_acchitecture():
    return list(platform.architecture())

# 获取主板序列号，如0929WE00J303
def mainboard_n():
    return ''.join(mbn.SerialNumber.strip() for mbn in w.Win32_BaseBoard())

# 获取bios序列号，如JT900001UKIS
def bios_n():
    return ''.join(biosn.SerialNumber.strip() for biosn in w.Win32_BIOS())

# 获取硬盘序列号，如38TG_2ISE_20QQ_02DE
def hard_n():
    return ''.join(hardn.SerialNumber for hardn in w.Win32_DiskDrive())

def vermessage():
    messagebox.showinfo(title="版本", message="版本v1.1.4。")

# 清理休眠文件（需要管理员权限）
def cleanpowercfg():
    import os
    os.system("powercfg -h off")
    messagebox.showinfo(title="提示", message="清除文件已关闭。")

# 下载函数
def download(whatdownload):
    __all_download = {"python" : "https://mirrors.huaweicloud.com/python/3.13.2/python-3.13.2.exe",
                      "jdk" : "https://repo.huaweicloud.com:8443/artifactory/java-local/jdk/13+33/jdk-13_windows-x64_bin.exe"}
    if whatdownload not in __all_download.keys():
        messagebox.showerror("下载","没有找到下载源。")
    elif not  whatdownload == "000-激活-win11":
        # 下载文件      
        f = requests.get(__all_download[whatdownload])
        with open("E:\one user\Code\python\Winevent/{}.exe".format(whatdownload),"wb") as d:
            d.write(f.content)
        messagebox.showinfo("下载","下载完毕，已保存至程序文件夹！")
