class Cargo:
    PRICE_TABLE = {
        50: 300,
        100: 1000,
        300: 2000
    }

    def init(self, weight: int):
        self.weight = weight
        self.base_price = self.calculate_base_price()

    def calculate_base_price(self) -> int:
        """Определяет базовую стоимость подъема груза по таблице."""
        for max_weight, price in sorted(self.PRICE_TABLE.items()):
            if self.weight <= max_weight:
                return price
        return max(self.PRICE_TABLE.values())  # Если больше 300 кг, берем максимум

    def str(self):
        return f"Груз {self.weight} кг, базовая стоимость: {self.base_price} руб."