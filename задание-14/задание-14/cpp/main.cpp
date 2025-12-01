#include <iostream>
#include <string>
#include <cmath>

using namespace std;

// Класс Insect (Насекомое)
class Insect {
private:
    string species;      // Вид насекомого
    int lifespan;        // Продолжительность жизни (в днях)
    double weight;       // Вес (в граммах)
    bool canFly;         // Умеет летать

public:
    // 1) Конструктор по умолчанию (для требования 1а)
    Insect() {
        species = "Неизвестно";
        lifespan = 0;
        weight = 0.0;
        canFly = false;
        cout << "Создано насекомое конструктором по умолчанию" << endl;
    }

    // 2) Конструктор с параметрами (для требования 1б)
    Insect(string sp, int life, double w, bool fly) {
        species = sp;
        lifespan = life;
        weight = w;
        canFly = fly;
        cout << "Создано насекомое конструктором с параметрами" << endl;
    }

    // 3) Конструктор копирования (для требования 1б)
    Insect(const Insect& other) {
        species = other.species;
        lifespan = other.lifespan;
        weight = other.weight;
        canFly = other.canFly;
        cout << "Создано насекомое конструктором копирования" << endl;
    }

    // 4) Функция для вывода информации (для требования 1а)
    void displayInfo() {
        cout << "Вид: " << species << endl;
        cout << "Продолжительность жизни: " << lifespan << " дней" << endl;
        cout << "Вес: " << weight << " г" << endl;
        cout << "Умеет летать: " << (canFly ? "Да" : "Нет") << endl;
    }

    // 5) Функция для ввода данных (для требования 1в)
    void inputData() {
        cout << "Введите вид насекомого: ";
        getline(cin, species);
        cout << "Введите продолжительность жизни (в днях): ";
        cin >> lifespan;
        cout << "Введите вес (в граммах): ";
        cin >> weight;
        cout << "Умеет летать (1 - Да, 0 - Нет): ";
        cin >> canFly;
        cin.ignore(); // Очистка буфера
    }

    // 6) Функция для расчета плотности веса (имеет входные параметры и возвращаемое значение) - для требования 1в
    double calculateDensity(double volume) {
        if (volume > 0) {
            return weight / volume;
        }
        return 0.0;
    }

    // 7) Функция для проверки, является ли насекомое долгожителем - для требования 1г
    bool isLongLived() {
        return lifespan > 365; // Более года
    }

    // 8) Перегруженная функция isLongLived с параметром (для требования 1г)
    bool isLongLived(int thresholdDays) {
        return lifespan > thresholdDays;
    }

    // 9) Функция для сравнения насекомых по весу - для требования 1г
    bool isHeavierThan(Insect other) {
        return weight > other.weight;
    }

    // 10) Геттеры (для работы с полями)
    string getSpecies() { return species; }
    int getLifespan() { return lifespan; }
    double getWeight() { return weight; }
    bool getCanFly() { return canFly; }

    // 11) Сеттеры (для работы с полями)
    void setSpecies(string sp) { species = sp; }
    void setLifespan(int life) { 
        if (life >= 0) lifespan = life;
        else cout << "Ошибка: продолжительность жизни не может быть отрицательной!" << endl;
    }
    void setWeight(double w) { 
        if (w >= 0) weight = w;
        else cout << "Ошибка: вес не может быть отрицательным!" << endl;
    }
    void setCanFly(bool fly) { canFly = fly; }

    // 12) Функция для расчета относительного возраста
    double calculateRelativeAge(int currentAge) {
        if (lifespan > 0) {
            return (double)currentAge / lifespan;
        }
        return 0.0;
    }
};

int main() {
    setlocale(LC_ALL, "Russian");

    cout << "=== ДЕМОНСТРАЦИЯ КЛАССА INSECT ===\n" << endl;

    // 1. Использование конструктора по умолчанию
    cout << "1. Создание насекомого с помощью конструктора по умолчанию:" << endl;
    Insect insect1;
    insect1.displayInfo();
    cout << endl;

    // 2. Использование конструктора с параметрами
    cout << "2. Создание насекомого с помощью конструктора с параметрами:" << endl;
    Insect insect2("Бабочка Монарх", 210, 0.75, true);
    insect2.displayInfo();
    cout << endl;

    // 3. Использование конструктора копирования
    cout << "3. Создание насекомого с помощью конструктора копирования:" << endl;
    Insect insect3(insect2);
    insect3.displayInfo();
    cout << endl;

    // 4. Использование функции ввода данных
    cout << "4. Ввод данных для насекомого:" << endl;
    Insect insect4;
    insect4.inputData();
    cout << "\nВведенные данные:" << endl;
    insect4.displayInfo();
    cout << endl;

    // 5. Использование функции с входными параметрами и возвращаемым значением
    cout << "5. Расчет плотности веса насекомого:" << endl;
    double volume = 1.5; // объем в см³
    double density = insect2.calculateDensity(volume);
    cout << "Плотность бабочки (вес/объем): " << density << " г/см³" << endl;
    cout << endl;

    // 6. Использование функции isLongLived (без параметров)
    cout << "6. Проверка, является ли насекомое долгожителем:" << endl;
    cout << "Бабочка Монарх - долгожитель: " << (insect2.isLongLived() ? "Да" : "Нет") << endl;
    cout << endl;

    // 7. Использование перегруженной функции isLongLived (с параметром)
    cout << "7. Проверка долгожительства с порогом 100 дней:" << endl;
    cout << "Бабочка Монарх живет больше 100 дней: " << (insect2.isLongLived(100) ? "Да" : "Нет") << endl;
    cout << endl;

    // 8. Использование функции сравнения
    cout << "8. Сравнение насекомых по весу:" << endl;
    cout << "Бабочка тяжелее введенного насекомого: " << (insect2.isHeavierThan(insect4) ? "Да" : "Нет") << endl;
    cout << endl;

    // 9. Использование геттеров
    cout << "9. Использование геттеров:" << endl;
    cout << "Вид insect2: " << insect2.getSpecies() << endl;
    cout << "Вес insect2: " << insect2.getWeight() << " г" << endl;
    cout << "Умеет летать insect2: " << (insect2.getCanFly() ? "Да" : "Нет") << endl;
    cout << endl;

    // 10. Использование сеттеров
    cout << "10. Использование сеттеров (изменение insect1):" << endl;
    insect1.setSpecies("Муравей");
    insect1.setLifespan(365);
    insect1.setWeight(0.01);
    insect1.setCanFly(false);
    insect1.displayInfo();
    cout << endl;

    // 11. Использование функции для расчета относительного возраста
    cout << "11. Расчет относительного возраста насекомого:" << endl;
    int currentAge = 100;
    double relativeAge = insect2.calculateRelativeAge(currentAge);
    cout << "Относительный возраст бабочки в возрасте " << currentAge << " дней: " << relativeAge * 100 << "% от общей продолжительности жизни" << endl;
    cout << endl;

    // 12. Создание массива насекомых
    cout << "12. Работа с массивом насекомых:" << endl;
    Insect insects[3] = {
        Insect("Пчела", 180, 0.1, true),
        Insect("Жук-олень", 730, 2.5, true),
        Insect("Таракан", 100, 0.05, false)
    };

    for (int i = 0; i < 3; i++) {
        cout << "Насекомое " << i + 1 << ":" << endl;
        insects[i].displayInfo();
        cout << "Долгожитель (>1 года): " << (insects[i].isLongLived(365) ? "Да" : "Нет") << endl;
        cout << endl;
    }

    cout << "=== ДЕМОНСТРАЦИЯ ЗАВЕРШЕНА ===" << endl;

    return 0;
}
