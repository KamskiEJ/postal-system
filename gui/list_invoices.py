import tkinter as tk
from tkinter import messagebox

def list_invoices(root, system):
    invoices = system.list_invoices()

    if invoices.strip() == "Немає накладних у системі.":
        messagebox.showinfo("Накладні", invoices)
        return

    invoice_window = tk.Toplevel(root)
    invoice_window.title("Список накладних")
    invoice_window.geometry("500x500")

    text_box = tk.Text(invoice_window, wrap="word", padx=10, pady=10, font=("Arial", 10))
    text_box.insert("1.0", invoices)
    text_box.config(state="disabled")
    text_box.pack(expand=True, fill="both")