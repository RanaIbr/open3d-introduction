import open3d as o3d
from tkinter import *
import tkinter as tk
from tkinter.filedialog import askopenfilename


def main():
    root = tk.Tk()
    root.geometry('500x500')
    root.title('Open3D')
    root.resizable(False, False)
    button = tk.Button(root, text='choose .ply file', command=lambda: select_file(label))
    button.pack()
    label = tk.Label(root)
    label.pack()
    root.mainloop()


def select_file(labell):
    filename = askopenfilename()  # show an "Open" dialog box and return the path to the selected file
    print(filename)
    labell.config(text=filename)
    open_file(filename)


def open_file(filename):
    pcd = o3d.io.read_point_cloud(filename)
    pcd.paint_uniform_color([5, 0.706, 0])
    o3d.visualization.draw_geometries_with_editing([pcd], width=500, height=500)


main()
