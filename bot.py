import telebot
from telebot import types
import os

bot_token = os.environ["BOT_TOKEN"]

bot = telebot.TeleBot(bot_token)


@bot.message_handler(content_types=['new_chat_members'])
def greeting(message):
    bot.reply_to(message,
                 text='Добро пожаловать, {0.first_name}!\nРасскажи нам о себе, пожалуйста.\nОбязательно ознакомься с '
                      'правилами чата и '
                      'посмотри на полезные ссылки. Для этого напиши /start'.format(message.from_user, bot.get_me()),
                 parse_mode='html')


@bot.message_handler(commands=['start'])
def welcome(message):
    # keybord
    markup = types.ReplyKeyboardMarkup(row_width=2, resize_keyboard=True, one_time_keyboard=True)
    item1 = types.KeyboardButton("\U0001F913 Правила чата")
    item2 = types.KeyboardButton("\U0001F46F Подчаты")
    item3 = types.KeyboardButton("\U00002764 Полезные каналы сообщества")

    markup.add(item1, item2, item3)
    bot.send_message(message.chat.id,
                     "Смотри сколько у нас есть всего интересного:", reply_markup=markup)


@bot.message_handler(content_types=['text'])
def lalala(message):
    # if message.chat.type == 'private':
    if message.text == '\U0001F913 Правила чата':
        bot.send_message(message.chat.id, 'Правила можно почитать тут: https://telegra.ph/Pravila-chata-05-25-2')
    elif message.text == '\U0001F46F Подчаты':
        markup = types.InlineKeyboardMarkup(row_width=1)
        item1 = types.InlineKeyboardButton("Куплю-продам", url="https://t.me/itwivestraderoom")
        item2 = types.InlineKeyboardButton("Книжный клуб", url="https://t.me/kniginiTallina")
        item3 = types.InlineKeyboardButton("Гуляем вместе с детьми", url="https://t.me/joinchat/De31pxTSW5xY35C5wAqgcQ")
        item4 = types.InlineKeyboardButton("Шоппинг", url="https://t.me/shopping_itwives")
        item5 = types.InlineKeyboardButton("Школы-садики", url="http://t.me/itwivesschool")
        item6 = types.InlineKeyboardButton("Клуб любителей настольных игр", url="https://t.me/itwivesnastolki")
        item7 = types.InlineKeyboardButton("Рукоделие", url="https://t.me/ITwiwesKnitting")
        item8 = types.InlineKeyboardButton("QA-шная", url="https://t.me/qa_itwives")
        item9 = types.InlineKeyboardButton("Кулинарный чат", url="http://t.me/extravaganzaoftaste")
        item10 = types.InlineKeyboardButton("Гардеробная", url="https://t.me/itwives_wardrobe")
        item11 = types.InlineKeyboardButton("Зимние забавы.", url="https://t.me/Katok_Tallinn")
        item12 = types.InlineKeyboardButton("Активный отдых в Эстонии.",
                                            url="https://t.me/joinchat/Auk2vUXBwbTCa1Oe66uYpw")
        item13 = types.InlineKeyboardButton("Садоводы", url="https://t.me/ITwivesFlowers")

        markup.add(item1, item2, item3, item4, item5, item6, item7, item8, item9, item10, item11, item12, item13)

        bot.send_message(message.chat.id, 'Это чаты нашего сообщества',
                         reply_markup=markup)

    elif message.text == '\U00002764 Полезные каналы сообщества':
        markup = types.InlineKeyboardMarkup(row_width=1)
        item1 = types.InlineKeyboardButton("Очень Важная Информация", url="https://t.me/info_eesti")
        item2 = types.InlineKeyboardButton("ITwives News. Дайджест за день", url="https://t.me/itwivesnews")

        markup.add(item1, item2)
        bot.send_message(message.chat.id,
                         'Tут сконцентрирована самая полезная информация',
                         reply_markup=markup)
    clear_first_message(message)


def clear_first_message(message):
    if message.text == "\U0001F913 Правила чата":
        bot.delete_message(message.chat.id, message.message_id)
    if message.text == "\U0001F46F Подчаты":
        bot.delete_message(message.chat.id, message.message_id)
    if message.text == "\U00002764 Полезные каналы сообщества":
        bot.delete_message(message.chat.id, message.message_id)


def clear_last_message(message):
    if message.text == "Правила можно почитать тут: https://telegra.ph/Pravila-chata-05-25-2":
        bot.delete_message(message.chat.id, message.inline_message_id)


bot.polling(none_stop=True)
