# jopra_bot


Delayed message
sent_message = bot.send_message(message.chat.id, 'Tут сконцентрирована самая полезная информация', reply_markup=markup)
bot.delete_message(message.chat.id, message.message_id)
time.sleep(10)
bot.delete_message(sent_message.chat.id, sent_message.message_id)
