import tkinter as tk

def show_statistics(root, system):
    stats_window = tk.Toplevel(root)
    stats_window.title("Статистика системи")
    stats_window.geometry("400x400")

    stats_text = system.show_statistics()

    text_box = tk.Text(stats_window, wrap="word", padx=10, pady=10, font=("Arial", 10))
    text_box.insert("1.0", stats_text)
    text_box.config(state="disabled")  # робимо тільки для читання
    text_box.pack(expand=True, fill="both")