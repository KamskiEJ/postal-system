class Client:
    def __init__(self, name: str, client_id: str, email: str="", phone: str=""):
        self.name = name
        self.client_id = client_id
        self.email = email
        self.phone = phone
        self.invoices = []
        self.products = []

    def add_invoice(self, invoice):
        self.invoices.append(invoice)

    def add_product(self, product):
        self.products.append(product)

    def get_summary(self):
        return (
            f"Клієнт: {self.name} (ID - {self.client_id})\n"
            f"Email: {self.email if self.email else 'Немає'}\n"
            f"Телефон: {self.phone if self.phone else 'Немає'}\n"
            f"Кількість накладних: {len(self.invoices)}\n"
            f"Кількість товарів: {len(self.products)}"
        )
