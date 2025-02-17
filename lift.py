class Lift:
    def __init__(self, has_lift: bool, cargo_fits: bool):
        """
        :param has_lift: Есть ли работающий лифт
        :param cargo_fits: Влезает ли груз в лифт
        """
        self.has_lift = has_lift
        self.cargo_fits = cargo_fits

    def can_use_lift(self) -> bool:
        """Проверяет, можно ли воспользоваться лифтом."""
        return self.has_lift and self.cargo_fits

    def __str__(self):
        return "Лифт доступен" if self.can_use_lift() else "Лифт недоступен"
