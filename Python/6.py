import csv
import os
import tkinter
import numpy as np
import matplotlib as matplotlib
import matplotlib.pyplot as plt
from tkinter import filedialog

def open_file():
    root = tkinter.Tk()
    root.withdraw()
    default_dir = r"C:\\Users\\Administrator\\Documents\\数据"
    file_path = tkinter.filedialog.askopenfilename(title= u'选择文件', initialdir = (os.path.expanduser(default_dir)))
    print(file_path)
    return file_path

def getdata(CAN_ID,start_d,num,dx):
    vec = []
    with open(open_file()) as f:
        f_csv = csv.reader(f)
        for row in f_csv:
            if row[4] == CAN_ID:
                if dx == 0:
                    data = row[5+start_d] * 256 + row[6+start_d]
                elif  dx == 1:
                    data = row[6+start_d] * 256 + row[5+start_d]
                vec.append(data)
    plt.plot(vec)
    plt.show()


if __name__ == '__main__':
    getdata("1100000a\t",2,2,1)