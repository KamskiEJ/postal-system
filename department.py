class Department:
    def __init__(self, name: str, city: str, address: str):
        self.name = name
        self.city = city
        self.address = address
        self.products = []
        self.employees = []

    def receive_product(self, product: str) -> str:
        self.products.append(product)
        return f"Продукт '{product}' прийнято у відділенні '{self.name}'."

    def issue_product(self, product: str):
        if product in self.products:
            self.products.remove(product)
            return f"Продукт '{product}' видано з відділення '{self.name}'."
        else:
            return f"Продукт '{product}' не знайдено у відділенні '{self.name}'."

    def check_invoices(self):
        if not self.products:
            return f"У відділенні '{self.name}' наразі немає товарів."
        product_list = "\n".join(f"- {p}" for p in self.products)
        return f"Список товарів у відділенні '{self.name}':\n{product_list}"
