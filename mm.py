import telebot
from telebot import types

bot = telebot.TeleBot("1397565480:AAGG25AIQizfuyim14v0oTTz_upuG2IDTyM")
admin_id = 64189817 #491657362
need_help_id = None

@bot.message_handler(commands=['start'])
def any_msg(message):
    keyboard = types.InlineKeyboardMarkup()
    kazan = types.InlineKeyboardButton(text="Казань", callback_data="kazan")
    almetyevsk = types.InlineKeyboardButton(text="Альметьевск", callback_data="almetyevsk")
    keyboard.add(kazan, almetyevsk)
    bot.send_message(message.chat.id, """Здравствуйте! Добро пожаловать в телеграм-бот клиники Стомус.
Выберите Ваш город""", reply_markup=keyboard)


@bot.message_handler(content_types=['text'])
def send_text(message):
    global need_help_id
    print(message)
    if need_help_id and message.chat.id == need_help_id:
        bot.send_message(message.chat.id, 'Ваш вопрос передан врачам, через несколько минут Вам ответят...')

        bot.send_message(admin_id, 'Вопрос от пользователя:\n' + message.text)
    elif message.chat.id == admin_id:
        bot.send_message(message.chat.id, 'Ваш ответ передан пользователю.')

        bot.send_message(need_help_id, 'Ответ от врача:\n' + message.text)
        need_help = None


@bot.callback_query_handler(func=lambda call: True)
def callback_inline(call):
    global need_help_id

    if call.message:
        if call.data == "kazan":
            keyboard = types.InlineKeyboardMarkup(row_width=1)

            a = types.InlineKeyboardButton(text="ул. Чистопольская, 15", callback_data="4")

            b = types.InlineKeyboardButton(text="ул. Адоратского, 3", callback_data="5")
            c = types.InlineKeyboardButton(text="ул. Павлюхина, 87", callback_data="6")
            d = types.InlineKeyboardButton(text="ул. Фучика, 88", callback_data="7")
            e = types.InlineKeyboardButton(text="пр. Победы, 152/33", callback_data="8")
            f = types.InlineKeyboardButton(text="Ф. Амирхана, 23", callback_data="9")

            keyboard.add(a,b,c,d,e,f)
            bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,  text = """Пожалуйста, выберите клинику""", reply_markup=keyboard)

        if call.data == "almetyevsk":
            keyboard = types.InlineKeyboardMarkup(row_width=1)

            e = types.InlineKeyboardButton(text="ул. Ленина, 113", callback_data="10")
            g = types.InlineKeyboardButton(text="ул. Ленина, 50", callback_data="11")

            keyboard.add(g,e)
            bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,  text = """Пожалуйста, выберите клинику""", reply_markup=keyboard)




        if call.data == "4" or call.data == "5" or call.data == "6" or call.data == "7" or call.data == "8" or call.data == "9" or call.data == "10" or call.data == "11":

            keyboard = types.InlineKeyboardMarkup(row_width=1)
            zubi = types.InlineKeyboardButton(text="Лечение зубов", callback_data="zubi")
            implant = types.InlineKeyboardButton(text="Имплантация", callback_data="implant")
            protez = types.InlineKeyboardButton(text="Протезирование", callback_data="protez")
            erexeq = types.InlineKeyboardButton(text="Детская стоматология", callback_data="erexeq")
            vinir = types.InlineKeyboardButton(text="Виниры", callback_data="vinir")
            desen = types.InlineKeyboardButton(text="Лечение десен", callback_data="desen")
            xirurg = types.InlineKeyboardButton(text="Хирургия", callback_data="xirurg")
            zubi_ch = types.InlineKeyboardButton(text="Чистка зубов", callback_data="zubi_ch")
            estet = types.InlineKeyboardButton(text="Эстетическая стоматология", callback_data="estet")


            keyboard.add(zubi, implant, protez, erexeq, vinir, desen, xirurg, zubi_ch, estet)
            bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,  text = """Пожалуйста, напишите причину обращения.
Или выберите подходящую категорию""", reply_markup=keyboard)

        if call.data == "zubi":
            bot.send_message(call.message.chat.id, 'Напишите запрос:')
            need_help_id = call.message.chat.id


bot.polling()
