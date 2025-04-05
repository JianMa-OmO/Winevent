# coding=utf-8
# 编写由gihub:JianMa OmO 
# 最后修改时间2024/4/5
import Main_calculate
# tkinter美化包
import ttkbootstrap as tb

root = tb.Window(themename="cosmo")
root.title("Winevent")
root.geometry("600x700")
notebook = tb.Notebook(root)
infoframe = tb.Frame(root)
toolsframe = tb.Frame(root)

# 开始下载文件的响应函数
def start_download():
    Main_calculate.download(get_input(inputat))

# 获取文本输入框的内容
def get_input(__input):
    return __input.get()

# 创建下载文件的子窗口
def create_windowalltools():
    # 生名inputat, get_buttonat为全局变量
    global inputat, get_buttonat
    # 创建子窗口
    wat_window = tb.Toplevel(root)
    wat_window.title("输入软件名字")
    wat_window.geometry("400x300")
    # 文本输入框
    inputat = tb.Entry(wat_window)
    inputat.pack()
    get_buttonat = tb.Button(wat_window, text="确定", command=start_download)
    get_buttonat.pack()
    wat_window.mainloop()

# 系统信息标签要显示的内容
infotext = [
    f"Windows版本号：{Main_calculate.Windows_v()}",
    f"Windows版本：Windows{Main_calculate.Windows_e()}",
    f"电脑制造商：{Main_calculate.computer_manufacturer()}",
    f"电脑型号：{Main_calculate.computer_model()}",
    f"处理器名称：{Main_calculate.processor_name()}",
    f"处理器架构：{Main_calculate.processor_acchitecture()}",
    f"主板序列号：{Main_calculate.mainboard_n()}",
    f"Bios序列号：{Main_calculate.bios_n()}",
    f"硬盘序列号：{Main_calculate.hard_n()}"
]
# 工具标签要显示的按钮文本
toolstext = ["版本", "关闭休眠文件", "开发软件"]
# 工具标签要执行的函数
toolscmd = [Main_calculate.vermessage, Main_calculate.cleanpowercfg, create_windowalltools]
# 渲染系统信息标签要显示的内容
for i, text in enumerate(infotext):
    tb.Label(infoframe, text=text).place(x=0, y=i * 35)

# 渲染工具标签要显示的按钮文本
for i, (text, cmd) in enumerate(zip(toolstext, toolscmd)):
    tb.Button(toolsframe, text=text, command=cmd).place(x=i * 200, y=0)

# 创建两个标签
notebook.add(infoframe, text="🖥️系统信息")
notebook.add(toolsframe, text="🛠️工具")
notebook.pack(padx=10, pady=5, fill=tb.BOTH, expand=True)
root.mainloop()