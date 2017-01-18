# main.py
# Created by Shaun Chiang for mit iap '17 - Error Efficient Computing
# Requires crayon binary.
# Recursively looks through selected folder and applies crayon color transformations.

from tkinter.filedialog import askdirectory, askopenfilename
import os, tkinter, tkinter.ttk
def crayonbin_callback():
    crayonbin = askopenfilename(title="Choose Crayon Binary")

def rootdir_callback():
    rootdir = askdirectory(title="Choose Project Directory")

def go_callback():
    for root, subFolders, files in os.walk(rootdir):
        for file in files:
            if file.endswith(".png"):
                # run command here
                # os.system("{0} --lambda 0.000059 --bitmap {1}".format(crayonbin, rootdir))
                print(file)



if __name__ == '__main__':
    top = tkinter.Tk()

    crayonbin=""
    rootdir=""

    crayon_label=tkinter.Label(top, text="Crayon Binary:", width=10)
    crayon_label.pack(side=tkinter.LEFT)
    crayon_button = tkinter.Button(top, text="Browse..", command=crayonbin_callback)
    crayon_button.pack()
    rootdir_label = tkinter.Label(top, text="Root Dir:", width=10)
    rootdir_label.pack(side=tkinter.LEFT)
    rootdir_button = tkinter.Button(top, text="Browse..", command=rootdir_callback)
    rootdir_button.pack()
    go_button = tkinter.Button(top, text="Go!", command = go_callback)
    go_button.pack()



    top.mainloop()