import telebot, random, time

bot = telebot.TeleBot('1024854764:AAH47BVSzMW_eSPLSwZ1id-s1Jz_1yLu_os')
MEMES = [
    ('image1',
     ['дэтылэн -- плавник', 'би- -- быть, иметься'],
     ['dim', 'pl', 'nfut', 'ends', 'poss']),
    ('image2',
     ['би -- я', 'чоралан- -- звенеть'],
     ['cond', 'ends', 'neg']),
    ('image3',
     ['няя -- песня шамана'],
     []),
    ('image4',
     ['авурангка -- говорящий', 'делгэнкэн -- осёл', 'би- -- быть, иметься'],
     ['poss', 'nfut', 'ends']),
    ('image5',
     ['эро -- межд. ну', 'ибго -- да, хорошо, нормально', 'гирка- -- идти', 'буй -- нежилое место, лес'],
     ['purp', 'ends', 'dir'])
]

GRAMMAR = {
    'dim': 'dim',
    'cond': 'cond',
    'dir': 'dir',
    'ends': 'ends',
    'neg': 'neg',
    'nfut': 'nfut',
    'pl': 'pl',
    'poss': 'poss',
    'purp': 'purp'
}


def choose_meme():
    data = random.choice(MEMES)
    return data


def main_menu():
    mark_up = telebot.types.InlineKeyboardMarkup()
    item = telebot.types.InlineKeyboardButton(text='HSE', url='hse.ru')
    mark_up.add(item)
    item = telebot.types.InlineKeyboardButton(text='Получить мем', callback_data='2')
    mark_up.add(item)
    return mark_up


def send_photo(id, data):
    mark_up = telebot.types.InlineKeyboardMarkup()
    item = telebot.types.InlineKeyboardButton(text='Покажи лексику', callback_data='1')
    mark_up.add(item)
    item = telebot.types.InlineKeyboardButton(text='Покажи грамматику', callback_data='3')
    mark_up.add(item)
    item = telebot.types.InlineKeyboardButton(text='Получить мем', callback_data='2')
    mark_up.add(item)
    photo = data[0]
    bot.send_photo(chat_id=id, photo=photo, reply_markup=mark_up)

    @bot.callback_query_handler(func=None)
    def gotit(message):
        if message.data == '2':
            send_meme(message, data)


def send_help(id, data, n):
    data = data[n]
    if n == 1:
        string = '\n'.join(data)
        bot.send_message(chat_id=id, text=string)
    if n == 2:
        for item in data:
            bot.send_photo(chat_id=id, photo=GRAMMAR[item])


def send_meme(message, data):
    send_photo(message.from_user.id, data)


@bot.message_handler(commands=['start'])
def start_message(message):
    id = message.chat.id
    mark_up = main_menu()
    bot.send_message(id, 'Привет, я эвенский мемодел!\nЯ создан, чтобы помочь тебе в изучении эвенского.\n' + \
                     'Что ты хочешь сделать? Можешь посетить сайт Вышки или получить мем', reply_markup=mark_up)

    @bot.callback_query_handler(func=None)
    def gotit(message):
        if message.data == '2':
            data = choose_meme()
            send_meme(message, data)
        if message.data == '1':
            idd = message.message.json['photo'][0]['file_id']
            print(idd)
            if str(idd) == 'AgADBAADQKoxG7n8dVPgVNf8Kx0UBesrsRoABAEAAwIAA20AA_QBCAABFgQ':
                data = MEMES[1]
                send_help(message.from_user.id, data, 1)
            if str(idd) == 'AgADBAADIaoxG4G4dFPL8HQQQe0aH58_thsABAEAAwIAA20AAxcxAAIWBA':
                data = MEMES[0]
                send_help(message.from_user.id, data, 1)
            if str(idd) == 'AgADBAADpaoxGw3AdVNYm--jGvrV3g6mtBsABAEAAwIAA20AAy0yAAIWBA':
                data = MEMES[4]
                send_help(message.from_user.id, data, 1)
            if str(idd) == 'AgADBAAD26oxG0PlbVMNqplppohHYRRiqBsABAEAAwIAA20AAwP7BAABFgQ':
                data = MEMES[3]
                send_help(message.from_user.id, data, 1)
            if str(idd) == 'AgADBAADNqoxGzpGdFNc3tZF-x3IeVsSthsABAEAAwIAA20AA2ozAAIWBA':
                data = MEMES[2]
                send_help(message.from_user.id, data, 1)
        if message.data == '3':
            idd = message.message.json['photo'][0]['file_id']
            print(idd)
            if str(idd) == 'AgADBAADQKoxG7n8dVPgVNf8Kx0UBesrsRoABAEAAwIAA20AA_QBCAABFgQ':
                data = MEMES[1]
                send_help(message.from_user.id, data, 2)
            if str(idd) == 'AgADBAADIaoxG4G4dFPL8HQQQe0aH58_thsABAEAAwIAA20AAxcxAAIWBA':
                data = MEMES[0]
                send_help(message.from_user.id, data, 2)
            if str(idd) == 'AgADBAADpaoxGw3AdVNYm--jGvrV3g6mtBsABAEAAwIAA20AAy0yAAIWBA':
                data = MEMES[4]
                send_help(message.from_user.id, data, 2)
            if str(idd) == 'AgADBAAD26oxG0PlbVMNqplppohHYRRiqBsABAEAAwIAA20AAwP7BAABFgQ':
                data = MEMES[3]
                send_help(message.from_user.id, data, 2)
            if str(idd) == 'AgADBAADNqoxGzpGdFNc3tZF-x3IeVsSthsABAEAAwIAA20AA2ozAAIWBA':
                data = MEMES[2]
                send_help(message.from_user.id, data, 2)
        if message.data == '5':
            bot.send_message(chat_id=message.from_user.id, text='5469 0300 1129 4428')
        if message.data == '6':
            bot.send_message(chat_id=message.from_user.id, text='2200 2408 7806 8978')

@bot.message_handler(regexp='Новый мем')
def one(message):
    data = choose_meme()
    send_meme(message, data)


@bot.message_handler(commands=['sites'])
def sites(message):
    mark_up = telebot.types.InlineKeyboardMarkup()
    wiki = telebot.types.InlineKeyboardButton('Even Wiki', url='https://en.wikipedia.org/wiki/Even_language')
    glotto = telebot.types.InlineKeyboardButton('Even Glotto', url='https://glottolog.org/resource/languoid/id/even1260')
    mark_up.add(wiki, glotto)
    bot.send_message(message.chat.id, 'Почитай про эвенский!', reply_markup=mark_up)

@bot.message_handler(commands=['support'])
def sites(message):
    mark_up = telebot.types.InlineKeyboardMarkup()
    sber = telebot.types.InlineKeyboardButton('Сбербанк', callback_data='5')
    vtb = telebot.types.InlineKeyboardButton('ВТБ', callback_data='6')
    mark_up.add(sber, vtb)
    bot.send_message(message.chat.id, 'Ты можешь поддержать проект, номер какой карты тебе скинуть?', reply_markup=mark_up)

    @bot.callback_query_handler(func=None)
    def sup(message):
        if message.data == '2':
            data = choose_meme()
            send_meme(message, data)
        if message.data == '1':
            idd = message.message.json['photo'][0]['file_id']
            print(idd)
            if str(idd) == 'AgADBAADQKoxG7n8dVPgVNf8Kx0UBesrsRoABAEAAwIAA20AA_QBCAABFgQ':
                data = MEMES[1]
                send_help(message.from_user.id, data, 1)
            if str(idd) == 'AgADBAADIaoxG4G4dFPL8HQQQe0aH58_thsABAEAAwIAA20AAxcxAAIWBA':
                data = MEMES[0]
                send_help(message.from_user.id, data, 1)
            if str(idd) == 'AgADBAADpaoxGw3AdVNYm--jGvrV3g6mtBsABAEAAwIAA20AAy0yAAIWBA':
                data = MEMES[4]
                send_help(message.from_user.id, data, 1)
            if str(idd) == 'AgADBAAD26oxG0PlbVMNqplppohHYRRiqBsABAEAAwIAA20AAwP7BAABFgQ':
                data = MEMES[3]
                send_help(message.from_user.id, data, 1)
            if str(idd) == 'AgADBAADNqoxGzpGdFNc3tZF-x3IeVsSthsABAEAAwIAA20AA2ozAAIWBA':
                data = MEMES[2]
                send_help(message.from_user.id, data, 1)
        if message.data == '3':
            idd = message.message.json['photo'][0]['file_id']
            print(idd)
            if str(idd) == 'AgADBAADQKoxG7n8dVPgVNf8Kx0UBesrsRoABAEAAwIAA20AA_QBCAABFgQ':
                data = MEMES[1]
                send_help(message.from_user.id, data, 2)
            if str(idd) == 'AgADBAADIaoxG4G4dFPL8HQQQe0aH58_thsABAEAAwIAA20AAxcxAAIWBA':
                data = MEMES[0]
                send_help(message.from_user.id, data, 2)
            if str(idd) == 'AgADBAADpaoxGw3AdVNYm--jGvrV3g6mtBsABAEAAwIAA20AAy0yAAIWBA':
                data = MEMES[4]
                send_help(message.from_user.id, data, 2)
            if str(idd) == 'AgADBAAD26oxG0PlbVMNqplppohHYRRiqBsABAEAAwIAA20AAwP7BAABFgQ':
                data = MEMES[3]
                send_help(message.from_user.id, data, 2)
            if str(idd) == 'AgADBAADNqoxGzpGdFNc3tZF-x3IeVsSthsABAEAAwIAA20AA2ozAAIWBA':
                data = MEMES[2]
                send_help(message.from_user.id, data, 2)
        if message.data == '5':
            bot.send_message(chat_id=message.from_user.id, text='5469 0300 1129 4428')
        if message.data == '6':
            bot.send_message(chat_id=message.from_user.id, text='2200 2408 7806 8978')

while True:
    try:
        bot.polling(none_stop=True)
    except Exception:
        print('Error')
        time.sleep(3)
