import tkinter as tk
from tkinter import ttk


def button_clicked(event):
    print('Button clicked')


root = tk.Tk()
root.title('How Do I Money??')
root.iconbitmap('./src/hdim/assets/appicon.ico')

W_WID = 800
W_HEI = 400

s_wid = root.winfo_screenwidth()
s_hei = root.winfo_screenheight()

center_x = int(s_wid / 2 - W_WID / 2)
center_y = int(s_hei / 2 - W_HEI / 2)

root.geometry(f'{W_WID}x{W_HEI}+{center_x}+{center_y}')
root.resizable(False, False)

message = ttk.Label(root, text="Hello there").pack()

button = ttk.Button(root, text='Submit')
button.bind('<Return>', button_clicked)
button.bind('<Button>', button_clicked)
button.focus()
button.pack()

root.mainloop()

