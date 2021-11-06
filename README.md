# Телеграм-бот для Продуктлаб

![LOGO](https://programadoresbrasil.com.br/wp-content/uploads/2019/08/telegram.jpg "Telegram")

Простой телеграм бот для парсинга товаров Wildberries по артиклю

* **/get_brand** <article> - для получения бренда/изготовителя товара 
* **/get_title** <article> - для получения названия товара

___
  
В файле `wildparser.py` хранится сам парсер. Для его, и не только, работы потребуется наличие следующих библиотек:
1. **Requests** - устанавливается через `pip install requests`
2. **BeautifulSoup** - устанвока - `pip install beautifulsoup4`
3. **Telebot** - а тут не все так очевидно - `pip install pyTelegramBotAPI`
  
___
  
Запуск производится через файл `bot.py` командой `python bot.py`. Токен прописыпается там же, в 4 строке. Например:
```python
>>> TOKEN = "3151593693:AGFUe2HVyrJwrPKbPJJq6eM8P3eIpshZgY0"
```
  
___
  
Все товары сохраняются в базе данных `databse/products.db` - за основу взята **Sqlite3**. База данных имеет следующую структуру:

| Столбец | Характеристики |
| ------- | -------------- |
| id | INTEGER, PRIMARY, AUTOINCREMENT |
| article | INTEGER |
| brand | TEXT |
| title | TEXT |

___
![kavo](https://img.shields.io/badge/Developed%20by-PERL54-9cf)
