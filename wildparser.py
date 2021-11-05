from bs4 import BeautifulSoup
import requests

def getArcticleInfo(art: int):
	url = "https://www.wildberries.ru/catalog/{}/detail.aspx?targetUrl=GP#c36450780".format(art)
	page = requests.get(url)
	if page.status_code != 200:
		return 'Error: The product with this article was not found!'
	else:
		soup = BeautifulSoup(page.text, "html.parser")
		brand = soup.find("span", {'data-link':'text{:product^brandName}'}).get_text()
		name = soup.find("span", {'data-link':'text{:product^goodsName}'}).get_text()

		return {"brand":brand, "name":name}
