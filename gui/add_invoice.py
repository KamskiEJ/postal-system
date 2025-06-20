import tkinter as tk
from tkinter import messagebox


def create_invoice(root, system):
    window = tk.Toplevel(root)
    window.title("Створити накладну")
    window.geometry("400x400")

    tk.Label(window, text="Номер накладної:").pack(pady=5)
    entry_number = tk.Entry(window, width=30)
    entry_number.pack()

    tk.Label(window, text="ID відправника:").pack(pady=5)
    entry_sender = tk.Entry(window, width=30)
    entry_sender.pack()

    tk.Label(window, text="ID одержувача:").pack(pady=5)
    entry_receiver = tk.Entry(window, width=30)
    entry_receiver.pack()

    tk.Label(window, text="Назви товарів (через кому):").pack(pady=5)
    entry_products = tk.Entry(window, width=40)
    entry_products.pack()

    def save_invoice():
        number = entry_number.get().strip()
        sender = entry_sender.get().strip()
        receiver = entry_receiver.get().strip()
        products_str = entry_products.get().strip()

        if not number or not sender or not receiver or not products_str:
            messagebox.showerror("Помилка", "Усі поля є обов'язковими!")
            return

        products = [p.strip() for p in products_str.split(",") if p.strip()]
        if not products:
            messagebox.showerror("Помилка", "Список товарів не може бути порожнім!")
            return

        msg = system.create_invoice(number, sender, receiver, products)
        messagebox.showinfo("Успіх", msg)
        window.destroy()

    tk.Button(window, text="Створити накладну", command=save_invoice, bg="#f0d0a0", width=25).pack(pady=20)