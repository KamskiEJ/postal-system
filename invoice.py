from datetime import datetime

class Invoice:
    def __init__(self, invoice_number: str, sender_id: str, receiver_id: str, products: list):
        self.invoice_number = invoice_number
        self.sender_id = sender_id
        self.receiver_id = receiver_id
        self.products = products
        self.status = "Створена"
        self.creation_date = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    def mark_delivered(self):
        self.status = "Доставлено"
        return f"Накладна №{self.invoice_number} позначена як доставлена."

    def add_product(self, product_name: str):
        if product_name not in self.products:
            self.products.append(product_name)
            return f"Товар '{product_name}' додано до накладної."
        return f"Товар '{product_name}' вже є в накладній."

    def get_summary(self):
        summary = [
            f"=== Накладна №{self.invoice_number} ===",
            f"Відправник ID: {self.sender_id}",
            f"Отримувач ID: {self.receiver_id}",
            f"Кількість товарів: {len(self.products)}",
            f"Статус: {self.status}",
            f"Дата створення: {self.creation_date}",
            "Список товарів:"
        ]
        for product_name in self.products:
            summary.append(f"- {product_name}")
        return "\n".join(summary)
