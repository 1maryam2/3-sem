import httpx
from bs4 import BeautifulSoup
import sqlite3
conn = sqlite3.connect('horo.db', check_same_thread=False)
headers={
    'accept-language': 'ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7',
    'user-aggent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.0.0 Safari/537.36',
    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9'
}
async def get_response(link: str):
    async with httpx.AsyncClient(headers=headers, follow_redirects=True) as htx:
        result: httpx.Response = await htx.get(url=link)
        if result.status_code != 200:
            return await get_response(link=link)
        else:
            return await result.aread()
async def get_text_of_horoscope(zodiac: str):
    link = f'https://horo.mail.ru/prediction/{zodiac}/today/'
    response_result = await get_response(link=link)
    beautifulsoup: BeautifulSoup = BeautifulSoup(response_result, features='lxml')
    text_element = beautifulsoup.find(name='div', class_='b6a5d4949c e45a4c1552')
    return text_element.text if text_element else "Гороскоп не найден."