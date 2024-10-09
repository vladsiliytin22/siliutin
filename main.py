import os
import json
from functions import compare_differences, translate

# Попытка загрузки данных из файла
def load_data():
    if os.path.exists('MyData.txt'):
        try:
            with open('MyData.txt', 'r') as file:
                data = json.load(file)
                return data['x'], data['y'], data['language']
        except (json.JSONDecodeError, KeyError):
            return None
    return None

# Сохранение данных в файл
def save_data(x, y, language):
    with open('MyData.txt', 'w') as file:
        json.dump({'x': x, 'y': y, 'language': language}, file)
    print(f"{translate('save_success', language)} MyData.txt")

# Основная программа
def main():
    data = load_data()

    if data is None:
        try:
            # Ввод данных вручную
            x, y = map(int, input(translate('input_numbers', 'uk')).split())
            language = input(translate('input_language', 'uk')).strip().lower()
            save_data(x, y, language)
        except ValueError:
            print("Некоректні дані!")
        return

    x, y, language = data
    # Если язык указан некорректно, используем украинский
    if language not in ['uk', 'en']:
        language = 'uk'

    print(f"{translate('square_diff', language).format(x=x, y=y, result=abs(x**2 - y**2))}")
    print(f"{translate('diff_square', language).format(x=x, y=y, result=(x - y)**2)}")

    # Сравнение значений
    square_diff, diff_square = compare_differences(x, y)
    if square_diff > diff_square:
        print(translate('compare_result_more', language))
    else:
        print(translate('compare_result_less', language))

if __name__ == '__main__':
    main()