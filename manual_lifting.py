class ManualLifting:
    PRICE_PER_FLOOR_PER_100KG = 300

    def __init__(self, cargo_weight: int, floor: int, lift_available: bool):
        """
        :param cargo_weight: Вес груза
        :param floor: На какой этаж поднимаем (если 1 этаж, то это 0 подъема)
        :param lift_available: Можно ли использовать лифт
        """
        self.cargo_weight = cargo_weight
        self.floor = max(floor - 1, 0)  # Этажи считаются с 1, а плата — за поднятие
        self.lift_available = lift_available

    def calculate_manual_price(self) -> int:
        """Рассчитывает стоимость ручного подъема, если лифт недоступен."""
        if self.lift_available:
            return 0
        multiplier = (self.cargo_weight // 100) + (1 if self.cargo_weight % 100 else 0)
        return self.floor * self.PRICE_PER_FLOOR_PER_100KG * multiplier

    def __str__(self):
        price = self.calculate_manual_price()
        return f"Стоимость ручного подъема: {price} руб."
