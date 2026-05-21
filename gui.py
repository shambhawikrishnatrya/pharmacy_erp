import tkinter as tk
from tkinter import ttk


window = tk.Tk()

window.title("Pharmacy ERP")
window.geometry("900x600")

label = tk.Label(window, text="Pharmacy ERP System")
label.pack()

button = tk.Button(window, text="Add Medicine")
button.pack()

window.mainloop()