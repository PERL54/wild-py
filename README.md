# Телеграм-бот для Продуктлаб
![LOGO](https://programadoresbrasil.com.br/wp-content/uploads/2019/08/telegram.jpg "Telegram")

Простой телеграм бот для парсинга веб страниц. 

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
