from cargo import Cargo
from lift import Lift
from manual_lifting import ManualLifting


def main():
    # Ввод данных
    weight = int(input("Введите вес груза (кг): "))
    floor = int(input("Введите этаж подъема: "))
    has_lift = input("Есть ли лифт? (да/нет): ").strip().lower() == "да"
    cargo_fits = input("Влезает ли груз в лифт? (да/нет): ").strip().lower() == "да"

    # Создание объектов
    cargo = Cargo(weight)
    lift = Lift(has_lift, cargo_fits)
    manual_lifting = ManualLifting(weight, floor, lift.can_use_lift())

    # Итоговый расчет
    total_price = cargo.base_price + manual_lifting.calculate_manual_price()

    # Вывод результатов
    print("\nРезультаты расчета:")
    print(cargo)
    print(lift)
    print(manual_lifting)
    print(f"Итоговая стоимость: {total_price} руб.")


if __name__ == "__main__":
    main()
