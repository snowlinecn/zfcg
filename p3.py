from tkinter import *
from tkinter import ttk
from tkinter import scrolledtext
import tkinter.filedialog

class MainWindow(Frame):
    
    def __init__(self, master=None):
        Frame.__init__(self, master)
        self["padx"] = 1
        self["pady"] = 1
        self.spath = ''
        self.dpath = ''
        self.createWidgets()

    def createWidgets(self):

        self.grid(padx=10, pady=10)
        
        self.slb = Label(self, text=self.spath, justify="left")
        self.slb.grid(row=0, column=1, sticky=W)

        self.dlb = Label(self, text=self.dpath, justify="left")
        self.dlb.grid(row=1, column=1, sticky=W)

        self.sbtn = Button(self, text="源文件夹", width=15, command=self.get_spwd)
        self.sbtn.grid(row=0, column=0, sticky=W)

        self.dbtn = Button(self, text="目标文件夹", width=15, command=self.get_dpwd)
        self.dbtn.grid(row=1, column=0, sticky=W)
        
        self.mvtn = Button(self, text="开始移动", width=15, command=self.move_photo)
        self.mvtn.grid(row=2, column=0, sticky=W)

        self.scr = scrolledtext.ScrolledText(self, width=80, height=18) 
        self.scr.grid(row=3, column=0, columnspan=2)

    def get_spwd(self):
        self.spath = tkinter.filedialog.askdirectory()
        if self.spath != '':
            self.slb.config(text=self.spath)
        else:
            self.slb.config(text="请选择照片文件夹")

    def get_dpwd(self):
        self.dpath = tkinter.filedialog.askdirectory()
        if self.dpath != '':
            self.dlb.config(text=self.dpath)
        else:
            self.dlb.config(text="请选择目标文件夹")
            
    def move_photo(self):
        self.scr.insert(END, "照片将被移动到")
        self.scr.see(END)
    
app = MainWindow()
app.master.title('照片整理工具 V0.9')
app.master.geometry('600x350')
app.mainloop()