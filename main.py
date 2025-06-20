from postal_system import PostalSystem
from gui.add_client import add_client
from gui.add_department import add_department as open_add_department
from gui.add_product import add_product as open_add_product
from gui.add_invoice import create_invoice as open_create_invoice
from gui.show_statistics import show_statistics as show_statistics_window
from gui.list_invoices import list_invoices as list_invoices_window
import tkinter as tk


system = PostalSystem("Masabo")

# Створення вікна
root = tk.Tk()
root.title("Поштова система")
root.geometry("400x500")
root.resizable(False, False)

# Заголовок
title_label = tk.Label(root, text="Поштова Система Masabo", font=("Arial", 16, "bold"), pady=10)
title_label.pack()

button_frame = tk.Frame(root, padx=20, pady=20)
button_frame.pack(expand=True)


def open_add_client_window():
    add_client(root, system)


def add_product():
    open_add_product(root, system)


def add_department():
    open_add_department(root, system)


def create_invoice():
    open_create_invoice(root, system)

def show_statistics():
    show_statistics_window(root, system)


def list_invoices():
    list_invoices_window(root, system)



buttons = [
    ("➕ Додати клієнта", open_add_client_window),
    ("📦 Додати товар", add_product),
    ("🏢 Додати відділення", add_department),
    ("🧾 Створити накладну", create_invoice),
    ("📊 Показати статистику", show_statistics),
    ("📄 Показати всі накладні", list_invoices),
]

for (text, command) in buttons:
    tk.Button(button_frame, text=text, command=command, width=30, height=2, bg="#cce6ff").pack(pady=5)

root.mainloop()