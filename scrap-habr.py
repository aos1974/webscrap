# Используемые модули программы

import requests
from fake_headers import Headers 
from bs4 import BeautifulSoup

# Глобальные переменные программы

MAINPAGE_LINK = 'https://habr.com'
FRESHPAGE_LINK = '/ru/all/'

# Функции используемые в программе

# парсер для страницы habr.com
def habr_parser(txt: str):
    pass

# Главная функция программы

def main():
    
    # формируем строку подключения и заголовки запроса
    page_link = MAINPAGE_LINK + FRESHPAGE_LINK
    headers = Headers(os="win", headers=True).generate()
    # получаем страницу с сайта
    response = requests.get(page_link, headers=headers)
    # проверяем статус ответа на ошибки
    if response.status_code == 200:
        habr_parser(response.text)
    else:
        print(f'Ошибка выполнения запроса к сайту {page_link}.')
        print(f'Код ошибки: {response.status_code}')
        exit

# Основная программа

if __name__ == "__main__":
    main()
    