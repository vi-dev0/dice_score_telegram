import telebot, time, json

token = 'TOKENT_HERE'

bot = telebot.TeleBot(token)
score = {}

@bot.message_handler(commands=['start'])
def start(message):
    bot.send_message(message.chat.id, 'Задрова, заебал')
    print(message)
@bot.message_handler(commands=['stb','stf', 'std', 'stbou'])
def test(message):
    pscore = score[message.from_user.id]
    print(pscore)
    if pscore.get('b_sshots') != 0:
        pscorepersent = 100 // pscore.get('b_shots') * pscore.get('b_sshots')
    else:
        pscorepersent = 0
    if pscore.get('f_sshots') != 0:
        pfscore = 100 // pscore.get('f_shots') * pscore.get('f_sshots')
    else:
        pfscore = 0
    if pscore.get('bou_sshots') != 0:
        pbouscore = 100 // pscore.get('bou_shots') * pscore.get('bou_sshots')
    else:
        pbouscore = 0
    if pscore.get('d_sshots') != 0:
        pdscore = 100 // pscore.get('d_shots') * pscore.get('d_sshots')
    else:
        pdscore = 0

    if (message.text == '/stb' or message.text == '/stb@b4dcat_test_bot'):
        bot.send_message(message.chat.id, '*' + message.from_user.first_name + '*' + ' твой личный счет:\n\n' +
                         '*БАСКТЕБОЛ*🏀\n' +
                         'Броски: ' + str(pscore.get('b_shots')) + '\nПопадания: '
                         + str(pscore.get('b_sshots')) + '\nПроцент попадания: ' + str(pscorepersent) +
                         '%\n\n*[@B4DCAT404](https://t.me/b4dcat404)*',
                         parse_mode="MarkdownV2", disable_web_page_preview=True)
    elif 'stf' in message.text:
        bot.send_message(message.chat.id, '*' + message.from_user.first_name + '*' + ' твой личный счет:\n\n' +
                                      '*ФУТБОЛ*⚽\n' +
                                      'Удары: ' + str(pscore.get('f_shots')) + '\nГолы: '
                                      + str(pscore.get('f_sshots')) + '\nПроцент голов: ' + str(pfscore) +
                                     '%\n\n*[@B4DCAT404](https://t.me/b4dcat404)*',
                                     parse_mode="MarkdownV2", disable_web_page_preview=True)
    elif 'stbou' in message.text:
        bot.send_message(message.chat.id, '*' + message.from_user.first_name + '*' + ' твой личный счет:\n\n' +
                                    '*БОУЛИНГ*🎳\n' +
                                     'Броски: ' + str(pscore.get('bou_shots')) + '\nСтрайки: '
                                     + str(pscore.get('bou_sshots')) + '\nПроцент страйков: ' + str(pbouscore) +
                                     '%\n\n*[@B4DCAT404](https://t.me/b4dcat404)*',
                                     parse_mode="MarkdownV2", disable_web_page_preview=True)
    elif 'std' in message.text:
        bot.send_message(message.chat.id, '*' + message.from_user.first_name + '*' + ' твой личный счет:\n\n' +
                         '\n\n*ДАРТС*🎯\n' +
                                     'Броски: ' + str(pscore.get('d_shots')) + '\nВ яблочко: '
                                     + str(pscore.get('d_sshots')) + '\nПроцент попаданий: ' + str(pdscore) +
                                      '%\n\n*[@B4DCAT404](https://t.me/b4dcat404)*',
                                        parse_mode="MarkdownV2", disable_web_page_preview=True)

@bot.message_handler(commands=['help'])
def help(message):
    bot.send_message(message.chat.id, '*Помощь по боту*\n'
                                      'Что бы бот начал вести счет, тебе нужно отправить один из эмоджи:\n'
                                      '🏀 \- Баскетбол \- посмотреть счет /stb\n'
                                      '⚽ \- Футбол \- посмотреть счет /stf\n'
                                      '🎳 \- Боулинг \- посмотреть счет /stbou\n'
                                      '🎯 \- Дартс \- посмотреть счет /std\n\n'
                                      '*[@B4DCAT404](https://t.me/b4dcat404)*',
                     parse_mode="MarkdownV2", disable_web_page_preview=True)

@bot.message_handler(commands=['score'])
def scores(message):
    usrid = message.from_user.id
    jscore = json.dumps(score, indent=4, sort_keys=True)
    print("Счет\n " + jscore)
    for key, value in score.items():
        print(key)
        user = key
        for v in value.items():
            print(v[1])


    #bot.send_message(message.chat.id, 'Общий счёт:\n' + jscore)



@bot.message_handler(func=lambda message: True, content_types=['dice'])
def handle_sticker(msg):
    dice = msg.dice.value
    usrid = msg.from_user.id
    usrname = msg.chat.first_name
    if msg.dice.emoji == '🏀':
        if msg.from_user.id not in score:
            score[msg.from_user.id] = {"b_shots": 0, "b_sshots": 0, "f_shots": 0, "f_sshots": 0, "bou_shots": 0, "bou_sshots": 0, "d_shots": 0, "d_sshots": 0}
        else:
            score[msg.from_user.id]["b_shots"] += 1
            if dice > 3:
                score[msg.from_user.id]["b_sshots"] += 1
    elif msg.dice.emoji == '⚽':
        if msg.from_user.id not in score:
            score[msg.from_user.id] = {"b_shots": 0, "b_sshots": 0, "f_shots": 0, "f_sshots": 0, "bou_shots": 0, "bou_sshots": 0, "d_shots": 0, "d_sshots": 0}
        else:
            score[msg.from_user.id]["f_shots"] += 1
            if dice > 3:
                score[msg.from_user.id]["f_sshots"] += 1
    elif msg.dice.emoji == '🎳':
        if msg.from_user.id not in score:
            score[msg.from_user.id] = {"b_shots": 0, "b_sshots": 0, "f_shots": 0, "f_sshots": 0, "bou_shots": 0, "bou_sshots": 0, "d_shots": 0, "d_sshots": 0}
        else:
            score[msg.from_user.id]["bou_shots"] += 1
            if dice == 6:
                score[msg.from_user.id]["bou_sshots"] += 1
    elif msg.dice.emoji == '🎯':
        if msg.from_user.id not in score:
            score[msg.from_user.id] = {"b_shots": 0, "b_sshots": 0, "f_shots": 0, "f_sshots": 0, "bou_shots": 0, "bou_sshots": 0, "d_shots": 0, "d_sshots": 0}
        else:
            score[msg.from_user.id]["d_shots"] += 1
            if dice == 6:
                score[msg.from_user.id]["d_sshots"] += 1
    print(msg.dice)



@bot.message_handler(commands=['reset'])
def reset(message):
    if '🏀' in message.text:
        bot.send_message(message.chat.id, 'true')
        score[message.from_user.id] = {"shots": 0, "sshots": 0}

    bot.send_message(message.chat.id, '*' + message.from_user.first_name + '*' +
                     ' твой счет обнулен\.\n', parse_mode="MarkdownV2")


@bot.message_handler(func=lambda message: True)
def text(message):
    if 'бот' in message.text:
        if 'пошел нахуй' in message.text:
            bot.reply_to(message, 'сам пошел нахуй, черт')
        elif 'хуйня' in message.text:
            bot.reply_to(message, 'слышь, сам ты хуйня\nзаберешься в матрицу, я тебе ебало разобью')

if __name__ == '__main__':
    while True:
        try:
            bot.polling(none_stop=True, interval=0)
        except Exception as e:
            print('Ошибка:')
            print(e)
            time.sleep(5)
            continue
