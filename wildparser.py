from bs4 import BeautifulSoup
import requests
import sqlite3

connection = sqlite3.connect(r'database/products.db', check_same_thread=False)
sql = connection.cursor()

sql.execute("CREATE TABLE IF NOT EXISTS `products`( `id` INTEGER PRIMARY KEY NOT NULL, `article` INT, `brand` TEXT, `title` TEXT, UNIQUE(article, brand, title));")

def getArcticleInfo(art: int):
	url = "https://www.wildberries.ru/catalog/{}/detail.aspx?targetUrl=GP#c36450780".format(art)
	page = requests.get(url)
	if page.status_code != 200:
		return 'Error: The product with this article was not found!'
	else:
		soup = BeautifulSoup(page.text, "html.parser")
		brand = soup.find("span", {'data-link':'text{:product^brandName}'}).get_text()
		name = soup.find("span", {'data-link':'text{:product^goodsName}'}).get_text()
		data = {"brand":brand, "name":name}
		dictToDB(art, data)
		return data

def dictToDB(article: int, data: dict):
	try:
		sql.execute("INSERT INTO products(article, brand, title) VALUES (?,?,?)", (article, data["brand"], data["name"]))
	except Exception as e:
		pass
	connection.commit()