from department import Department


class PostalSystem:
    def __init__(self, system_name):
        self.__system_name = system_name
        self.__departments = []
        self.__clients = []
        self.__products = []
        self.__invoices = []

    def add_department(self, name: str, city: str, address: str):
        department = Department(name, city, address)
        self.__departments.append(department)
        return f"Відділення '{name}' у місті '{city}' додано."

    def add_client(self, client_name: str, client_id: str):
        client_info = {"name": client_name, "id": client_id}
        self.__clients.append(client_info)
        return f"Клієнт '{client_name}' зареєстрований."

    def add_product(self, product_name: str):
        product_info = {"name": product_name}
        self.__products.append(product_info)
        return f"Товар '{product_name}' додано."

    def create_invoice(self, invoice_number: str, client_id: str, items: list):
        invoice_info = {
            "number": invoice_number,
            "client_id": client_id,
            "items": items
        }
        self.__invoices.append(invoice_info)
        return f"Накладну №'{invoice_number}' створено."

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
