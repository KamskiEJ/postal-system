import tkinter as tk
from tkinter import messagebox

def add_client(root, system):
    client_window = tk.Toplevel(root)
    client_window.title("Додати клієнта")
    client_window.geometry("350x300")

    tk.Label(client_window, text="Ім'я клієнта:").pack(pady=5)
    entry_name = tk.Entry(client_window, width=30)
    entry_name.pack()

    tk.Label(client_window, text="ID клієнта:").pack(pady=5)
    entry_id = tk.Entry(client_window, width=30)
    entry_id.pack()

    tk.Label(client_window, text="Email (необов’язково):").pack(pady=5)
    entry_email = tk.Entry(client_window, width=30)
    entry_email.pack()

    tk.Label(client_window, text="Телефон (необов’язково):").pack(pady=5)
    entry_phone = tk.Entry(client_window, width=30)
    entry_phone.pack()

    def save_client():
        name = entry_name.get().strip()
        client_id = entry_id.get().strip()
        email = entry_email.get().strip()
        phone = entry_phone.get().strip()

        if not name or not client_id:
            messagebox.showerror("Помилка", "Ім’я та ID клієнта — обов’язкові поля!")
            return

        msg = system.add_client(name, client_id)

        for client in system._PostalSystem__clients:
            if client.client_id == client_id:
                client.email = email
                client.phone = phone
                break

        messagebox.showinfo("Успіх", msg)
        client_window.destroy()

    tk.Button(client_window, text="Додати", command=save_client, bg="#a3e6a3", width=20).pack(pady=15)
