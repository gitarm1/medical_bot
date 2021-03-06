import telebot
from telebot import types
import codecs

bot = telebot.TeleBot("1390952647:AAFSCxQtduW6AcyTHagmGCVPMWjMx3-DSQc")
admin_id = 1398279961
need_help_id = None
need_help = None

teeth = ("Кариес", "пульпит", "киста", "кисту", "пломба", "пломбу", "вылечить", "лечить", "лечение", "канал", "каналу", "дырка", "болит", "боль", "ноет", "нерв")
implantant = ("имплантация", "имплантат", "имплант", "вставить", "искусственный", "astra", "antogym", "dentium")
protezis = ("all on 4", "мост", "протез", "протезирование", "несъемные", "съемные", "бюгельные", "покрывные")
kids = ("детей", "ребенок", "детский", "ребенку")
vinirs = ("виниры", "керамические", "композитные", "накладки")
desenn = ("Десны", "десна", "кровоточит", "воспалилась")
xirurgg = ("хирургия", "хирург", "синус", "лифтинг", "резекция", "корень", "удаление", "удалить", "корня", "мудрости", "коренного", "коренной")
teeth_clean = ("ультразвуковая", "ультразвук", "чистка", "отчистить", "почистить", "air flow", "камень", "камня")
teeth_esim = ("отбеливание", "отбелить", "скайсы", "стразы")
prikus = ("брекеты", "элайнеры", "прикус", "прикуса", "исправить", "исправление")

def merge(ls1,ls2):
    for item in ls1:
        if item in ls2:
            return True


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


    ls4 = message.text.split()
    if merge(ls4,teeth) == True:
        need_help_id = message.chat.id
        with open("items.txt" , "w+") as f:
            f.write(str(need_help_id))
        print(need_help_id)

        bot.send_message(message.chat.id, """Вам подходит раздел «Лечение зубов»🦷

Ваш вопрос передан врачам, через несколько минут Вам ответят...""")
        bot.send_message(admin_id, 'Вопрос от пользователя:\n' + message.text)

    elif merge(ls4,implantant):
        bot.send_message(message.chat.id, """Вам подходит раздел «Имплантация»🦷

Ваш вопрос передан врачам, через несколько минут Вам ответят...""")
        bot.send_message(admin_id, 'Вопрос от пользователя:\n' + message.text)

    elif merge(ls4,protezis):
        bot.send_message(message.chat.id, """Вам подходит раздел «Протезирование»🦷

Ваш вопрос передан врачам, через несколько минут Вам ответят...""")
        bot.send_message(admin_id, 'Вопрос от пользователя:\n' + message.text)



    elif merge(ls4,kids):
        bot.send_message(message.chat.id, """Вам подходит раздел «Детская стоматология»🦷

Ваш вопрос передан врачам, через несколько минут Вам ответят...""")
        bot.send_message(admin_id, 'Вопрос от пользователя:\n' + message.text)


    elif merge(ls4,vinirs):
        bot.send_message(message.chat.id, """Вам подходит раздел «Виниры»🦷

Ваш вопрос передан врачам, через несколько минут Вам ответят...""")
        bot.send_message(admin_id, 'Вопрос от пользователя:\n' + message.text)


    elif merge(ls4,desenn):
        bot.send_message(message.chat.id, """Вам подходит раздел «Лечение десен»🦷

Ваш вопрос передан врачам, через несколько минут Вам ответят...""")
        bot.send_message(admin_id, 'Вопрос от пользователя:\n' + message.text)


    elif merge(ls4,xirurgg):
        bot.send_message(message.chat.id, """Вам подходит раздел «Хирургия»🦷

Ваш вопрос передан врачам, через несколько минут Вам ответят...""")
        bot.send_message(admin_id, 'Вопрос от пользователя:\n' + message.text)


    elif merge(ls4,teeth_clean):
        bot.send_message(message.chat.id, """Вам подходит раздел «Чистка зубов»🦷

Ваш вопрос передан врачам, через несколько минут Вам ответят...""")
        bot.send_message(admin_id, 'Вопрос от пользователя:\n' + message.text)

    elif merge(ls4,teeth_esim):
        bot.send_message(message.chat.id, """Вам подходит раздел «Эстетическая стоматология»🦷

Ваш вопрос передан врачам, через несколько минут Вам ответят...""")
        bot.send_message(admin_id, 'Вопрос от пользователя:\n' + message.text)

    elif merge(ls4,prikus):
        bot.send_message(message.chat.id, """Вам подходит раздел «Исправление прикуса»🦷

Ваш вопрос передан врачам, через несколько минут Вам ответят...""")
        bot.send_message(admin_id, 'Вопрос от пользователя:\n' + message.text)

    elif message.chat.id == admin_id:
        bot.send_message(admin_id, 'Ваш ответ передан пользователю.')
        with open("items.txt" , "r") as f:
            need = f.read()
        print(need)

        bot.send_message(int(need), 'Ответ от врача:\n' + message.text)

    global need_help

    if need_help and message.chat.id == need_help:
        bot.send_message(message.chat.id, 'Ваш вопрос передан администраторам, через несколько минут Вам ответят...')
        g = codecs.open("gorod.txt", "r+", "utf-8")
        gorod = g.read()
        g.close()

        l = codecs.open("razdel.txt", "r+", "utf-8")
        razdel = l.read()
        l.close()

        h = codecs.open("adres.txt", "r+", "utf-8")
        adres = h.read()
        h.close()

        bot.send_message(admin_id, """Пользователь - @{},
Имя - {},
Город - {},
Адрес - {},
Раздел - {}

{}
""".format(message.from_user.username,message.from_user.first_name, gorod, adres, razdel, message.text))
    elif message.chat.id == admin_id:
        # bot.send_message(message.chat.id, 'Ваш овтет передан пользователю.')

        bot.send_message(need_help, 'Ответ от администратора:\n' + message.text)
        need_help = None

@bot.callback_query_handler(func=lambda call: True)
def callback_inline(call):
    global need_help

    if call.message:
        if call.data == "kazan":

            g = codecs.open("gorod.txt", "w", "utf-8")
            g.write("Казань")
            g.close()
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
            g = codecs.open("gorod.txt", "w", "utf-8")
            g.write("Альметьевск")
            g.close()
            keyboard = types.InlineKeyboardMarkup(row_width=1)

            e = types.InlineKeyboardButton(text="ул. Ленина, 113", callback_data="10")
            g = types.InlineKeyboardButton(text="ул. Ленина, 50", callback_data="11")

            keyboard.add(g,e)
            bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,  text = """Пожалуйста, выберите клинику""", reply_markup=keyboard)




        if call.data == "4":
            h = codecs.open("adres.txt", "w+", "utf-8")
            h.write("ул. Чистопольская, 15")
            h.close()

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

        if call.data == "5":
            h = codecs.open("adres.txt", "w+", "utf-8")
            h.write("ул. Адоратского, 3")
            h.close()

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

        if call.data == "6":
            h = codecs.open("adres.txt", "w+", "utf-8")
            h.write("ул. Павлюхина, 87")
            h.close()
            print("creater")

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


        if call.data == "7":
            h = codecs.open("adres.txt", "w+", "utf-8")
            h.write("ул. Фучика, 88")
            h.close()

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


        if call.data == "8":
            h = codecs.open("adres.txt", "w+", "utf-8")
            h.write("пр. Победы, 152/33")
            h.close()

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


        if call.data == "9":
            h = codecs.open("adres.txt", "w+", "utf-8")
            h.write("Ф. Амирхана, 23")
            h.close()

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



        if call.data == "10":
            h = codecs.open("adres.txt", "w+", "utf-8")
            h.write("ул. Ленина, 113")
            h.close()

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



        if call.data == "11":
            h = codecs.open("adres.txt", "w+", "utf-8")
            h.write("ул. Ленина, 50")
            h.close()

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
            l = codecs.open("razdel.txt", "w+", "utf-8")
            l.write("Лечение зубов")
            l.close()
            bot.send_message(call.message.chat.id, 'Напишите вопрос:')
            need_help = call.message.chat.id
        if call.data == "implant":
            l = codecs.open("razdel.txt", "w+", "utf-8")
            l.write("Имплантация")
            l.close()
            bot.send_message(call.message.chat.id, 'Напишите вопрос:')
            need_help = call.message.chat.id
        if call.data == "protez":
            l = codecs.open("razdel.txt", "w+", "utf-8")
            l.write("Протезирование")
            l.close()
            bot.send_message(call.message.chat.id, 'Напишите вопрос:')
            need_help = call.message.chat.id
        if call.data == "erexeq":
            l = codecs.open("razdel.txt", "w+", "utf-8")
            l.write("Детская стоматология")
            l.close()
            bot.send_message(call.message.chat.id, 'Напишите вопрос:')
            need_help = call.message.chat.id
        if call.data == "vinir":
            l = codecs.open("razdel.txt", "w+", "utf-8")
            l.write("Виниры")
            l.close()
            bot.send_message(call.message.chat.id, 'Напишите вопрос:')
            need_help = call.message.chat.id
        if call.data == "desen":
            l = codecs.open("razdel.txt", "w+", "utf-8")
            l.write("Лечение десен")
            l.close()
            bot.send_message(call.message.chat.id, 'Напишите вопрос:')
            need_help = call.message.chat.id
        if call.data == "xirurg":
            l = codecs.open("razdel.txt", "w+", "utf-8")
            l.write("Хирургия")
            l.close()
            bot.send_message(call.message.chat.id, 'Напишите вопрос:')
            need_help = call.message.chat.id
        if call.data == "zubi_ch":
            l = codecs.open("razdel.txt", "w+", "utf-8")
            l.write("Чистка зубов")
            l.close()
            bot.send_message(call.message.chat.id, 'Напишите вопрос:')
            need_help = call.message.chat.id
        if call.data == "estet":
            l = codecs.open("razdel.txt", "w+", "utf-8")
            l.write("Эстетическая стоматология")
            l.close()
            bot.send_message(call.message.chat.id, 'Напишите вопрос:')
            need_help = call.message.chat.id




bot.polling()
