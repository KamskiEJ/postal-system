class PostalSystem:
    def __init__(self, system_name):
        self.__system_name = system_name
        self.__departments = []
        self.__clients = []
        self.__products = []
        self.__invoices = []

    def add_departments(self, department_name: str, department_address: str):
        department_info = {"name": department_name, "address": department_address}
        self.__departments.append(department_info)
        return f"Department '{department_name}' added."

    def add_clients(self, client_name: str, client_id: str):
        client_info = {"name": client_name, "id": client_id}
        self.__clients.append(client_info)
        return f"Client '{client_name}' registered."

    def add_product(self, product_name: str):
        product_info = {"name": product_name}
        self.__products.append(product_info)
        return f"Product '{product_name}' added."

    def create_invoice(self, invoice_number: str, client_id: str, items: list):
        invoice_info = {
            "number": invoice_number,
            "client_id": client_id,
            "items": items
        }
        self.__invoices.append(invoice_info)
        return f"Invoice '{invoice_number}' created."

    def show_statistics(self):

        stats = []
        stats.append("\n=== Postal System Statistics ===")
        stats.append(f"System name: {self.__system_name}")
        stats.append(f"Total departments: {len(self.__departments)}")
        stats.append(f"Total clients: {len(self.__clients)}")
        stats.append(f"Total products: {len(self.__products)}")
        stats.append(f"Total invoices: {len(self.__invoices)}")
        return "\n".join(stats)