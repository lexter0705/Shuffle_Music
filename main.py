import tkinter as tk
from tkinter import *
from tkinter import ttk
from tkinter import filedialog
import tkinter.messagebox as mb
import Files_random
import os
import sys

window = Tk()
window.title('Shuffle Music')
window.geometry('512x570')
window.resizable(False, False)
print(window)

# check path with files def
def resource_path(relative_path):
   try:
        # PyInstaller creates a temp folder and stores path in _MEIPASS
      base_path = sys._MEIPASS
   except Exception:
      base_path = os.path.abspath(".")

   return os.path.join(base_path, relative_path)

window.iconbitmap(resource_path("")+'icon.ico')
img_i = PhotoImage(file=resource_path("")+"icon.png")
text_but = "C:"

filepath_one = None

# select folder def
def path_func():
   global filepath_one  
   filepath = filedialog.askdirectory()
   if filepath != "":
      road.configure(text=filepath)
      filepath_one = filepath
      
# shuffle files def
def main_func():
   is_success = Files_random.func_mix(filepath_one)
   print(is_success)
   if is_success[0] == False:
      mb.showerror("Ошибка", is_success[1])
   else:
      mb.showinfo("Информация", "Файлы перемешаны успешно!")
      


# road to path
road = ttk.Label(
   text=text_but,
   justify=CENTER,
)
road.pack(fill=BOTH)

# select folder button
swap_btn = Button(
   text="Выбрать путь",
   command = path_func,
   borderwidth=1,
   relief="solid"
)
swap_btn.pack(fill=BOTH)

# buutton shuffle
cal_btn = Button(
   text="Размешать",
   command = main_func,
)
cal_btn.pack(anchor=S, fill=BOTH)

#Image
img = Label(
   text=text_but,
   justify=CENTER,
   image=img_i
)
img.pack(fill=BOTH, padx=30)

#start app
if __name__ == "__main__":
   window.mainloop()
