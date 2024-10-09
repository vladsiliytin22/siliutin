import os

# Функция для вычисления разности квадратов и квадрата разности
def compare_differences(x, y):
    square_diff = abs(x**2 - y**2)
    diff_square = (x - y)**2
    return square_diff, diff_square

# Функция для перевода сообщений
def translate(text, language):
    translations = {
        'uk': {
            'input_numbers': 'Введіть два числа x, y: ',
            'input_language': 'Введіть мову інтерфейсу: ',
            'save_success': 'Дані збережено в файл',
            'square_diff': 'Модуль різності квадратів |{x}^2-{y}^2| = {result}',
            'diff_square': 'Квадрат різності ({x} - {y})^2 = {result}',
            'compare_result_more': 'Модуль різності більше!',
            'compare_result_less': 'Квадрат різності більше!'
        },
        'en': {
            'input_numbers': 'Enter two numbers x, y: ',
            'input_language': 'Enter interface language: ',
            'save_success': 'Data saved to file',
            'square_diff': 'Absolute difference of squares |{x}^2-{y}^2| = {result}',
            'diff_square': 'Square of difference ({x} - {y})^2 = {result}',
            'compare_result_more': 'Absolute difference is greater!',
            'compare_result_less': 'Square of difference is greater!'
        }
    }
    return translations.get(language, translations['uk']).get(text, text)