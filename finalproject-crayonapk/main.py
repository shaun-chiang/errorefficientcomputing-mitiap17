# main.py
# Crayon Batch UI
# Created by Shaun Chiang for mit iap '17 - Error Efficient Computing
# Requires crayon binary, python 3.
# Recursively looks through selected folder and applies crayon color transformations.

from tkinter.filedialog import askdirectory, askopenfilename
import os, tkinter as tk, tkinter.ttk
from functools import partial


image_store = []

def crayonbin_callback():
    global crayonbin
    crayonbin.set(askopenfilename(title="Choose Crayon Binary"))

def rootdir_callback():
    global rootdir
    rootdir.set(askdirectory(title="Choose Project Directory"))

def go_callback(controller):
    for root, subFolders, files in os.walk(rootdir.get()):
        for file in files:
            if file.endswith(".png"):
                # run command here
                print("{0} --lambda {1} --bitmap {2}".format(crayonbin.get(),lambda_value.get(), file))

                os.system("{0} --lambda {1} --bitmap {2}".format(crayonbin.get(),lambda_value.get(), file))
                # print(os.path.join(root,file))
                # image_store.append(os.path.join(root,file))


class MainApplication(tk.Tk):
    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)
        container = tk.Frame(self)
        container.pack(side="top", fill="both", expand=True)

        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)

        self.frames = {}

        for F in [StartPage]:
            frame = F(container, self)

            self.frames[F] = frame

            frame.grid(row=0, column=0, sticky="nsew")

        self.show_frame(StartPage)

    def show_frame(self, cont):
        frame = self.frames[cont]
        frame.tkraise()

class StartPage(tk.Frame):
    def __init__(self, parent, controller):
        global crayonbin, rootdir,lambda_value
        tk.Frame.__init__(self,parent)
        lambda_value = tk.StringVar()
        lambda_value.set(0.0059)
        crayonbin = tk.StringVar()
        crayonbin.set("Set Crayon Binary Path...")
        rootdir = tk.StringVar()
        rootdir.set("Set Project Directory Path...")
        crayon_label = tkinter.Label(self, text="Crayon Binary:".format(crayonbin), width=10).grid(row=0, column=0)
        crayonbin_label = tkinter.Label(self, textvariable=crayonbin).grid(row=0, column=1)
        crayon_button = tkinter.Button(self, text="Browse..", command=crayonbin_callback).grid(row=0, column=2)
        root_label = tkinter.Label(self, text="Root Dir:", width=10).grid(row=1, column=0)
        rootdir_label = tkinter.Label(self, textvariable=rootdir).grid(row=1, column=1)
        rootdir_button = tkinter.Button(self, text="Browse..", command=rootdir_callback).grid(row=1, column=2)
        go_button = tkinter.Button(self, text="Go!", command=partial(go_callback, controller)).grid(row=2, column=0)
        entry = tkinter.Entry(self, textvariable = lambda_value).grid(row=2,column=1)







if __name__ == "__main__":

    app = MainApplication()
    app.mainloop()
