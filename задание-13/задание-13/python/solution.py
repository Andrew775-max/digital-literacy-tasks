# Цыремпилов Андрей НКАбд-06-25
# Задание 13: Структура Printer с сортировкой

class Printer:
    def __init__(self, country, speed, quality, price):
        self.country = country
        self.speed = speed
        self.quality = quality
        self.price = price
    
    def __str__(self):
        return f"{self.country}, {self.speed} стр/мин, {self.quality}, {self.price} руб."

def create_printers():
    """Создаем список принтеров для демонстрации"""
    printers = [
        Printer("Япония", 30, "высокое", 15000),
        Printer("Китай", 25, "среднее", 8000),
        Printer("Германия", 35, "высокое", 20000),
        Printer("США", 28, "среднее", 12000),
        Printer("Корея", 32, "высокое", 18000)
    ]
    return printers

def sort_by_price(printers):
    """Сортировка по цене (по возрастанию)"""
    return sorted(printers, key=lambda x: x.price)

def sort_by_speed(printers):
    """Сортировка по скорости (по убыванию)"""
    return sorted(printers, key=lambda x: x.speed, reverse=True)

def sort_by_country(printers):
    """Сортировка по стране (по алфавиту)"""
    return sorted(printers, key=lambda x: x.country)

def print_list(printers, title):
    """Вывод списка принтеров"""
    print(f"\n=== {title} ===")
    for i, p in enumerate(printers, 1):
        print(f"{i}. {p}")

def main():
    """Основная функция программы"""
    printers = create_printers()
    
    print_list(printers, "Исходный список принтеров")
    
    # Сортировка по цене
    sorted_by_price = sort_by_price(printers)
    print_list(sorted_by_price, "Отсортировано по цене (возрастание)")
    
    # Сортировка по скорости
    sorted_by_speed = sort_by_speed(printers)
    print_list(sorted_by_speed, "Отсортировано по скорости (убывание)")
    
    # Сортировка по стране
    sorted_by_country = sort_by_country(printers)
    print_list(sorted_by_country, "Отсортировано по стране (алфавит)")

if __name__ == "__main__":
    main()
