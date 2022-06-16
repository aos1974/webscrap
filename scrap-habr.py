# Используемые модули программы

import requests
from fake_headers import Headers 
from bs4 import BeautifulSoup

# Глобальные переменные программы

MAINPAGE_LINK = 'https://habr.com'
FRESHPAGE_LINK = '/ru/all/'
KEYWORDS = ['.NET *', 'C# *', 'Go *', 'PHP *', 'Python *']

# Функции используемые в программе

# функция парсера для страницы habr.com
def habr_parser(txt: str):
    
    # начинаем обработку страницы с помощью методов библиотеки BeautifulSoup
    soup = BeautifulSoup(txt,'html.parser')
    # ищем все статьи на странице
    articles = soup.findAll('article')
    # в каждой найденной статье ищем необходимые нам атрибуты
    for article in articles:
        # получаем Тэги статьи
        article_hubs = article.find_all('a', class_='tm-article-snippet__hubs-item-link')
        # если статья нужной нам темы выводим информацию
        for article_hub in article_hubs:
            if article_hub.text in KEYWORDS:
                article_time = article.find('time')
                print(article_time.attrs['title'], end=' ')
                article_href = article.find('a', class_='tm-article-snippet__title-link')
                print(article_href.text, end=' ')
                print(MAINPAGE_LINK + article_href.attrs['href'])
# end habr_parser

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
# end main

# Основная программа

if __name__ == "__main__":
    main()
    