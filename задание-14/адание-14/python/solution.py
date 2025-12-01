class Insect:
    """
    Класс Insect (Насекомое) для описания характеристик насекомого
    """
    
    # 1а) Конструктор по умолчанию и с параметрами
    def __init__(self, species="Неизвестно", lifespan=0, weight=0.0, can_fly=False):
        """
        Конструктор с параметрами (для требования 1б)
        
        Args:
            species (str): Вид насекомого
            lifespan (int): Продолжительность жизни (в днях)
            weight (float): Вес (в граммах)
            can_fly (bool): Умеет ли летать
        """
        self.species = species
        self.lifespan = lifespan
        self.weight = weight
        self.can_fly = can_fly
        print(f"Создано насекомое: {species}")
    
    # 1б) Конструктор копирования
    @classmethod
    def copy(cls, other):
        """Конструктор копирования (для требования 1б)"""
        return cls(other.species, other.lifespan, other.weight, other.can_fly)
    
    # 1б) Еще один конструктор - из словаря данных
    @classmethod
    def from_dict(cls, data):
        """Конструктор из словаря данных (третий конструктор для требования 1б)"""
        return cls(
            data.get('species', 'Неизвестно'),
            data.get('lifespan', 0),
            data.get('weight', 0.0),
            data.get('can_fly', False)
        )
    
    # 1а) Функция класса для вывода информации
    def display_info(self):
        """Вывод информации о насекомом (для требования 1а)"""
        print(f"Вид: {self.species}")
        print(f"Продолжительность жизни: {self.lifespan} дней")
        print(f"Вес: {self.weight} г")
        print(f"Умеет летать: {'Да' if self.can_fly else 'Нет'}")
        print("-" * 30)
    
    # 1в) Функция с входными параметрами и возвращаемым значением
    def calculate_density(self, volume):
        """
        Расчет плотности веса (для требования 1в)
        
        Args:
            volume (float): Объем насекомого (в см³)
        
        Returns:
            float: Плотность (г/см³)
        """
        if volume > 0:
            return self.weight / volume
        return 0.0
    
    # 1в) Еще одна функция класса
    def input_data(self):
        """Ввод данных о насекомом (для требования 1в)"""
        print("Введите данные о насекомом:")
        self.species = input("Вид насекомого: ")
        self.lifespan = int(input("Продолжительность жизни (в днях): "))
        self.weight = float(input("Вес (в граммах): "))
        fly_input = input("Умеет летать (да/нет): ").lower()
        self.can_fly = fly_input in ['да', 'yes', 'y', '1']
        print("Данные успешно сохранены!")
    
    # 1г) Функция для проверки долгожительства
    def is_long_lived(self):
        """Проверка, является ли насекомое долгожителем"""
        return self.lifespan > 365  # Более года
    
    # 1г) Перегрузка функции is_long_lived (с параметром)
    def is_long_lived_threshold(self, threshold_days):
        """
        Проверка долгожительства с заданным порогом
        (перегрузка для требования 1г)
        
        Args:
            threshold_days (int): Порог в днях
        
        Returns:
            bool: True если живет больше порога
        """
        return self.lifespan > threshold_days
    
    # 1г) Еще одна функция класса
    def compare_weight(self, other_insect):
        """
        Сравнение веса с другим насекомым
        
        Args:
            other_insect (Insect): Другое насекомое для сравнения
        
        Returns:
            str: Результат сравнения
        """
        if self.weight > other_insect.weight:
            return f"{self.species} тяжелее {other_insect.species}"
        elif self.weight < other_insect.weight:
            return f"{self.species} легче {other_insect.species}"
        else:
            return f"{self.species} и {other_insect.species} имеют одинаковый вес"
    
    # Геттеры
    def get_species(self):
        return self.species
    
    def get_lifespan(self):
        return self.lifespan
    
    def get_weight(self):
        return self.weight
    
    def get_can_fly(self):
        return self.can_fly
    
    # Сеттеры
    def set_species(self, species):
        self.species = species
    
    def set_lifespan(self, lifespan):
        if lifespan >= 0:
            self.lifespan = lifespan
        else:
            print("Ошибка: продолжительность жизни не может быть отрицательной!")
    
    def set_weight(self, weight):
        if weight >= 0:
            self.weight = weight
        else:
            print("Ошибка: вес не может быть отрицательным!")
    
    def set_can_fly(self, can_fly):
        self.can_fly = can_fly
    
    # Дополнительная функция
    def calculate_relative_age(self, current_age):
        """
        Расчет относительного возраста
        
        Args:
            current_age (int): Текущий возраст насекомого
        
        Returns:
            float: Относительный возраст (0-1)
        """
        if self.lifespan > 0:
            return current_age / self.lifespan
        return 0.0
    
    def __str__(self):
        """Строковое представление объекта"""
        return (f"Насекомое: {self.species}, "
                f"жизнь: {self.lifespan} дн., "
                f"вес: {self.weight} г, "
                f"летает: {'Да' if self.can_fly else 'Нет'}")


def main():
    """Главная функция для демонстрации всех возможностей класса"""
    print("=" * 50)
    print("ДЕМОНСТРАЦИЯ КЛАССА INSECT (НАСЕКОМЫЕ)")
    print("=" * 50)
    
    # 1. Использование конструктора по умолчанию
    print("\n1. Создание насекомого конструктором по умолчанию:")
    insect1 = Insect()
    insect1.display_info()
    
    # 2. Использование конструктора с параметрами
    print("\n2. Создание насекомого конструктором с параметрами:")
    insect2 = Insect("Бабочка Монарх", 210, 0.75, True)
    insect2.display_info()
    
    # 3. Использование конструктора копирования
    print("\n3. Создание насекомого конструктором копирования:")
    insect3 = Insect.copy(insect2)
    insect3.display_info()
    
    # 4. Использование третьего конструктора (из словаря)
    print("\n4. Создание насекомого конструктором из словаря:")
    insect_data = {
        'species': 'Пчела медоносная',
        'lifespan': 180,
        'weight': 0.1,
        'can_fly': True
    }
    insect4 = Insect.from_dict(insect_data)
    insect4.display_info()
    
    # 5. Использование функции с параметрами и возвращаемым значением
    print("\n5. Расчет плотности веса насекомого:")
    volume = 1.5  # объем в см³
    density = insect2.calculate_density(volume)
    print(f"Плотность {insect2.get_species()}: {density:.3f} г/см³")
    
    # 6. Использование функции is_long_lived (без параметров)
    print("\n6. Проверка долгожительства:")
    print(f"{insect2.get_species()} - долгожитель: {'Да' if insect2.is_long_lived() else 'Нет'}")
    print(f"{insect4.get_species()} - долгожитель: {'Да' if insect4.is_long_lived() else 'Нет'}")
    
    # 7. Использование перегруженной функции is_long_lived (с параметром)
    print("\n7. Проверка долгожительства с порогом 100 дней:")
    threshold = 100
    result1 = insect2.is_long_lived_threshold(threshold)
    result2 = insect4.is_long_lived_threshold(threshold)
    print(f"{insect2.get_species()} живет > {threshold} дней: {'Да' if result1 else 'Нет'}")
    print(f"{insect4.get_species()} живет > {threshold} дней: {'Да' if result2 else 'Нет'}")
    
    # 8. Использование функции compare_weight
    print("\n8. Сравнение веса насекомых:")
    comparison = insect2.compare_weight(insect4)
    print(comparison)
    
    # 9. Использование геттеров
    print("\n9. Использование геттеров:")
    print(f"Вид insect2: {insect2.get_species()}")
    print(f"Вес insect2: {insect2.get_weight()} г")
    print(f"Умеет летать insect2: {'Да' if insect2.get_can_fly() else 'Нет'}")
    
    # 10. Использование сеттеров
    print("\n10. Использование сеттеров (изменение insect1):")
    insect1.set_species("Муравей рыжий")
    insect1.set_lifespan(365)
    insect1.set_weight(0.02)
    insect1.set_can_fly(False)
    insect1.display_info()
    
    # 11. Использование функции calculate_relative_age
    print("\n11. Расчет относительного возраста:")
    current_age = 100
    relative_age = insect2.calculate_relative_age(current_age)
    print(f"Относительный возраст {insect2.get_species()} в {current_age} дней: "
          f"{relative_age:.2%} от общей жизни")
    
    # 12. Демонстрация __str__ метода
    print("\n12. Строковое представление объектов:")
    print(insect1)
    print(insect2)
    print(insect3)
    print(insect4)
    
    # 13. Создание массива насекомых
    print("\n13. Работа со списком насекомых:")
    insects_list = [
        Insect("Стрекоза", 60, 0.3, True),
        Insect("Жук-олень", 730, 2.5, True),
        Insect("Таракан", 100, 0.05, False),
        Insect("Богомол", 180, 0.8, False)
    ]
    
    for i, insect in enumerate(insects_list, 1):
        print(f"\nНасекомое {i}:")
        insect.display_info()
        print(f"Долгожитель (>200 дней): {'Да' if insect.is_long_lived_threshold(200) else 'Нет'}")
    
    # 14. Дополнительная демонстрация функции ввода данных
    print("\n" + "=" * 50)
    print("ДОПОЛНИТЕЛЬНАЯ ДЕМОНСТРАЦИЯ: ВВОД ДАННЫХ")
    print("=" * 50)
    
    new_insect = Insect()
    new_insect.input_data()
    print("\nВведенные данные:")
    new_insect.display_info()
    
    print("\n" + "=" * 50)
    print("ДЕМОНСТРАЦИЯ ЗАВЕРШЕНА")
    print("=" * 50)


if __name__ == "__main__":
    main()
