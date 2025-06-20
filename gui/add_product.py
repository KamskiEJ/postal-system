import tkinter as tk
from tkinter import messagebox


def add_product(root, system):
    product_window = tk.Toplevel(root)
    product_window.title("Додати товар")
    product_window.geometry("350x350")

    tk.Label(product_window, text="Назва товару:").pack(pady=5)
    entry_name = tk.Entry(product_window, width=30)
    entry_name.pack()

    tk.Label(product_window, text="ID товару:").pack(pady=5)
    entry_id = tk.Entry(product_window, width=30)
    entry_id.pack()

    tk.Label(product_window, text="Вага (кг):").pack(pady=5)
    entry_weight = tk.Entry(product_window, width=30)
    entry_weight.pack()

    tk.Label(product_window, text="ID відправника:").pack(pady=5)
    entry_sender = tk.Entry(product_window, width=30)
    entry_sender.pack()

    tk.Label(product_window, text="ID одержувача:").pack(pady=5)
    entry_receiver = tk.Entry(product_window, width=30)
    entry_receiver.pack()

    def save_product():
        name = entry_name.get().strip()
        pid = entry_id.get().strip()
        weight = entry_weight.get().strip()
        sender = entry_sender.get().strip()
        receiver = entry_receiver.get().strip()

        if not name or not pid or not weight or not sender or not receiver:
            messagebox.showerror("Помилка", "Усі поля є обов'язковими!")
            return

        try:
            weight = float(weight)
        except ValueError:
            messagebox.showerror("Помилка", "Вага повинна бути числом!")
            return

        msg = system.add_product(name, pid, weight, sender, receiver)
        messagebox.showinfo("Успіх", msg)
        product_window.destroy()

    tk.Button(product_window, text="Додати товар", command=save_product, bg="#d0f0c0", width=20).pack(pady=15)