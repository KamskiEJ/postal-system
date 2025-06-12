class Product:
    def __init__(self, name: str, product_id: str, weight: float, sender_id: str, receiver_id: str):
        self.name = name
        self.product_id = product_id
        self.weight = weight
        self.sender_id = sender_id
        self.receiver_id = receiver_id
        self.current_department = None
        self.delivered = False

    def mark_delivered(self):
        self.delivered = True

    def assing_department(self, department: str):
        self.current_department = department

    def get_summary(self):
        return (
            f"Товар: {self.name} (ID: {self.product_id})\n"
            f"Вага: {self.weight} кг. \n"
            f"Відправник: {self.sender_id}\n"
            f"Одержувач: {self.receiver_id}\n"
            f"Поточне віділення: {self.current_department if self.current_department else 'Невідоме'}\n"
            f"Статус: {'Доставлено' if self.delivered else 'У дорозі'}"
        )