import telebot 
import wildparser

TOKEN = ""

bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=['start','help'])
def welcome(msg):
	bot.send_message(msg.chat.id, """
Wildberries BOT by [PERL54](https://t.me/PERL54)
GitHub page: [wild-py](https://github.com/PERL54/wild-py)

*Commands:*
- /get\_brand <article>
- /get\_title <article>

*For example:*
- /get\_brand 38567378
	""", parse_mode="Markdown")

@bot.message_handler(commands=['get_brand'])
def get_brand(msg):
	text = msg.text
	try:
		article = int(text.split(" ")[1])
		data = wildparser.getArcticleInfo(article)
		if type(data) == dict:
			bot.send_message(msg.chat.id, "*Article*: {} \n*Brand*: {}".format(article, data['brand']), parse_mode= 'Markdown')
		else:
			bot.send_message(msg.chat.id, data)
	except Exception as e:
		bot.send_message(msg.chat.id, "Something went wrong! Check that the input is correct.", parse_mode= 'Markdown')
	
@bot.message_handler(commands=['get_title'])
def get_title(msg):
	text = msg.text
	try:
		article = int(text.split(" ")[1])
		data = wildparser.getArcticleInfo(article)
		bot.send_message(msg.chat.id, "*Article*: {} \n*Title*: {}".format(article, data['name']), parse_mode= 'Markdown')
	except Exception as e:
		bot.send_message(msg.chat.id, "Something went wrong! Check that the input is correct.", parse_mode= 'Markdown')


bot.infinity_polling()
