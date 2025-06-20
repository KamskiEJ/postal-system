import tkinter as tk
from tkinter import messagebox

def add_department(root, system):
    dep_window = tk.Toplevel(root)
    dep_window.title("Додати відділення")
    dep_window.geometry("350x250")

    tk.Label(dep_window, text="Назва відділення:").pack(pady=5)
    entry_name = tk.Entry(dep_window, width=30)
    entry_name.pack()

    tk.Label(dep_window, text="Місто:").pack(pady=5)
    entry_city = tk.Entry(dep_window, width=30)
    entry_city.pack()

    tk.Label(dep_window, text="Адреса:").pack(pady=5)
    entry_address = tk.Entry(dep_window, width=30)
    entry_address.pack()

    def save_department():
        name = entry_name.get().strip()
        city = entry_city.get().strip()
        address = entry_address.get().strip()

        if not name or not city or not address:
            messagebox.showerror("Помилка", "Усі поля мають бути заповнені!")
            return

        msg = system.add_department(name, city, address)
        messagebox.showinfo("Успіх", msg)
        dep_window.destroy()

    tk.Button(dep_window, text="Додати", command=save_department, bg="#a3e6a3", width=20).pack(pady=15)