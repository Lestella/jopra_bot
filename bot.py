import telebot
import time
from telebot import types
import os


bot_token = os.environ["BOT_TOKEN"]
# bot_token = os.environ["BOT_TOKEN_TEST"]

bot = telebot.TeleBot(bot_token)


@bot.message_handler(content_types=['new_chat_members'])
def greeting(message):
    bot.reply_to(message,
                 text="Добро пожаловать, {0.first_name}!"
                      "\nПредставься и расскажи нам о себе, иначе мы просто удалим тебя через 10 минут"
                      "\nДа, это обязательно."
                      "\n"
                      "\nА еще обязательно ознакомься с правилами чата и посмотри на полезные ссылки."
                      "\nДля этого напиши /start и выбери интересующий раздел".format(message.from_user, bot.get_me()),
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
def handle_text_message(message):
    # if message.chat.type == 'private':
    if message.text == '\U0001F913 Правила чата':
        send_and_delete(message=message, text='Правила можно почитать тут: https://telegra.ph/Pravila-chata-05-25-2')

    elif message.text == '\U0001F46F Подчаты':
        markup = types.InlineKeyboardMarkup(row_width=1)
        markup.add(
            types.InlineKeyboardButton("Куплю-продам", url="https://t.me/itwivestraderoom"),
            types.InlineKeyboardButton("Книжный клуб", url="https://t.me/kniginiTallina"),
            types.InlineKeyboardButton("Гуляем вместе с детьми", url="https://t.me/joinchat/De31pxTSW5xY35C5wAqgcQ"),
            types.InlineKeyboardButton("Шоппинг", url="https://t.me/shopping_itwives"),
            types.InlineKeyboardButton("Школы-садики", url="http://t.me/itwivesschool"),
            types.InlineKeyboardButton("Клуб любителей настольных игр", url="https://t.me/itwivesnastolki"),
            types.InlineKeyboardButton("Рукоделие", url="https://t.me/ITwiwesKnitting"),
            types.InlineKeyboardButton("QA-шная", url="https://t.me/qa_itwives"),
            types.InlineKeyboardButton("Кулинарный чат", url="http://t.me/extravaganzaoftaste"),
            types.InlineKeyboardButton("Гардеробная", url="https://t.me/itwives_wardrobe"),
            types.InlineKeyboardButton("Зимние забавы.", url="https://t.me/Katok_Tallinn"),
            types.InlineKeyboardButton("Активный отдых в Эстонии.", url="https://t.me/joinchat/Auk2vUXBwbTCa1Oe66uYpw"),
            types.InlineKeyboardButton("Садоводы", url="https://t.me/ITwivesFlowers"),
            types.InlineKeyboardButton("Политика", url="https://t.me/politicsitwives"),
            types.InlineKeyboardButton("Разговорный клуб английский язык ITWC", url="https://t.me/EngForITWC")
        )
        send_and_delete(message=message, text='Это чаты нашего сообщества', markup=markup)

    elif message.text == '\U00002764 Полезные каналы сообщества':
        markup = types.InlineKeyboardMarkup(row_width=1)
        markup.add(
            types.InlineKeyboardButton("Очень Важная Информация", url="https://t.me/info_eesti"),
            #types.InlineKeyboardButton("ITwives News. Дайджест за день", url="https://t.me/itwivesnews"),
            types.InlineKeyboardButton("Таблица рекомендаций", url="https://docs.google.com/spreadsheets/d/1mBFwjuJb49JHBwP48pZfHh-Bfh3xuNMzTGvgQU0duXA/edit?usp=drivesdk"),
            types.InlineKeyboardButton("Доска мастеров", url="https://t.me/itwivesbusiness"),
            types.InlineKeyboardButton("Концерты в Таллине", url="https://t.me/concertivtalline")
        )
        send_and_delete(message=message, text='Tут сконцентрирована самая полезная информация', markup=markup)


def send_and_delete(message, text, markup=None, autodelete=100, notification=True):
    sent_message = bot.send_message(message.chat.id, text, reply_markup=markup, disable_notification=notification)
    bot.delete_message(message.chat.id, message.message_id)
    time.sleep(autodelete)
    bot.delete_message(sent_message.chat.id, sent_message.message_id)


bot.polling(none_stop=True)
