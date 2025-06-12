from department import Department
from client import Client
from invoice import Invoice
from product import Product


class PostalSystem:
    def __init__(self, system_name):
        self.__system_name = system_name
        self.__departments = []
        self.__clients = []
        self.__products = []
        self.__invoices = []
        self.Product = Product
        self.Client = Client
        self.Department = Department
        self.Invoice = Invoice



    def add_department(self, name: str, city: str, address: str):
        department = Department(name, city, address)
        self.__departments.append(department)
        return f"Відділення '{name}' у місті '{city}' додано."

    def add_client(self, client_name: str, client_id: str):
        client = Client(client_name, client_id)
        self.__clients.append(client)
        return f"Клієнт '{client_name}' зареєстрований."

    def add_product(self, name: str, product_id: str, weight: float, sender_id: str, receiver_id: str):
        product = Product(name, product_id, weight, sender_id, receiver_id)
        self.__products.append(product)
        return f"Товар '{name}' додано."

    def create_invoice(self, invoice_number: str, sender_id: str, receiver_id: str, items: list):
        invoice = Invoice(invoice_number, sender_id, receiver_id, items)
        self.__invoices.append(invoice)
        return f"Накладну №'{invoice_number}' створено між {sender_id} та {receiver_id}."

    def list_invoices(self):
        if not self.__invoices:
            return "Немає накладних у системі."
        return "\n\n".join([inv.get_summary() for inv in self.__invoices])

    def show_statistics(self):
        stats = []
        stats.append("\n=== Статистика поштової системи ===")
        stats.append(f"Назва системи: {self.__system_name}")
        stats.append(f"Загальна кількість відділень: {len(self.__departments)}")
        stats.append(f"Загальна кількість клієнтів: {len(self.__clients)}")
        stats.append(f"Загальна кількість товарів: {len(self.__products)}")
        stats.append(f"Загальна кількість накладних: {len(self.__invoices)}")

        if self.__departments:
            stats.append("\nСписок відділень:")
            for dep in self.__departments:
                stats.append(f"- {dep.name} ({dep.city})")

        return "\n".join(stats)
