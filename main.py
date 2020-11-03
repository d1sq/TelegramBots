import telebot
import config
import os
from func import *


admins = config.admins
bot = telebot.TeleBot(config.token, parse_mode='html')
new_user = False




@bot.message_handler(commands=["prms"])
def printUserMessage(message):
    if message.from_user.id in admins or message.from_user.username in admins:
        userids = message.text
        userids = userids.replace("/prms ", "")
        if userids == "/prms":
            bot.send_message(message.chat.id, 'необходимо имя файла')
        else:
            op_file = open('users\\' + userids + '.txt', 'rb')
            bot.send_document(message.chat.id, op_file)
            op_file.close()

    else:
        bot.send_photo(message.chat.id, 'https://i.ytimg.com/vi/Uf8NBVdQ2uk/maxresdefault.jpg', caption='PATHETIC!')



@bot.message_handler(commands=["files"])
def files(message):
    if message.from_user.id in admins or message.from_user.username in admins:
        #print(os.getcwd()) директория
        #print(os.listdir('users\\')) сами файлы
        for i in os.listdir('users\\'):
            bot.send_message(message.chat.id, i)
    else:
        bot.send_photo(message.chat.id, 'https://i.ytimg.com/vi/Uf8NBVdQ2uk/maxresdefault.jpg', caption='PATHETIC!')


@bot.message_handler(commands=["lab1"])
def lab1(message):
    text = message.text
    text = text.replace("/lab1 ", "")

    if text == "/lab1":
        bot.send_message(message.chat.id, "Отсутствует аргумент")
    else:

        alphabet = get_alphabet(text)
        result_array = get_weight(sorted(get_chances_count(text, alphabet), key=lambda x: x[0], reverse=True), text)
        a = ("Введенный текст: \n{}\n".format(text))
        aa = makeMeAString(get_weight(get_chances_count(text, get_alphabet(text)), text))
        b = ("Общее количество знаков: {}".format(sum([result_array[i][1] for i in range(len(result_array))])))
        c = ("Среднее количество информации на знак алфавита: {}".format(sum([i[3] for i in result_array])))
        d = ("При допущении равновероятности появления символов: {}".format(log2(len(alphabet))))

        bot.send_message(message.chat.id, a + "\n" + aa + "\n" + b + "\n" + c + "\n" + d + "\n")


@bot.message_handler(commands=["start"])
def start(message):
    global new_user
    if message.from_user.id == 1149744369:
        bot.send_photo(message.chat.id, 'https://antislang.ru/wp-content/uploads/дурка-2.jpg',
                       caption='Ты как из палаты сбежал, шизоид? + ''\n' 'Доступные команды: /lab1 /joke /creator /help /prms /users /files /free ')
    elif message.from_user.id in admins:
        bot.send_message(message.chat.id,
                         "Здравствуй, создатель" + "\n" "Доступные команды: /lab1 /joke /creator /help /prms /users /files")
    else:
        f = open('users.txt', 'r')

        users = f.read()

        new_user = True
        for i in users.split("\n"):
            if str(message.from_user.id) in i:
                bot.send_message(message.chat.id, "Привет " + i.split('\t')[1] + ', доступные команды: /start /lab1 /joke /creator /help')
                new_user = False
                break

        if (new_user):
            bot.send_message(message.chat.id,
                             "Привет, введите Свое имя!!")


        f.close()



@bot.message_handler(commands=["joke"])
def joke(message):
    bot.send_photo(message.chat.id,
                   "https://sun9-8.userapi.com/impf/oPlY2Tg8ncOKUar9O6IWKaRJ7grdfmijtYnhVA/FuTjoi6vjr8.jpg?size=1280x1274&quality=96&proxy=1&sign=5c22cefaea6cdab64e406918937051de",
                   caption="Купил мужик шляпу, а она ему unexpected indent")
    # bot.send.message(message.chat.id, "Купил мужик шляпу, а она ему unexpected indent")

@bot.message_handler(commands=["free"])
def durka(message):
    if message.from_user.id == 1149744369:
        bot.send_photo(message.chat.id, 'https://sun9-73.userapi.com/impf/c857324/v857324150/35cee/d_aG_SLKlAU.jpg?size=200x0&quality=90&crop=76,0,460,460&sign=2d77f29a61df7863c3a7f358324a162d&ava=1', caption='Ну привет')
    else:
        bot.send_message(message.chat.id, 'Вы не по адресу')

@bot.message_handler(commands=["creator"])
def creator(message):
    bot.send_message(message.chat.id, "@neongm " + "\n" "@Dd1392")



@bot.message_handler(commands=["help"])
def help(message):
    dict = {"lab1": "1 лабораторная работа",
            "creator": "Тот самый",
            "joke": "А что Вы ожидаете?",
            "free": "Специальная команда, флаг доступа SH",
            "users": "Вывод списка пользователей бота",
            "start": "Запуск бота",
            "files": "Получение списка фаилов, флаг доступа admin",
            "prms": "Скачивание фаила, флаг доступа admin"
            }
    found = False
    for i in dict.keys():
        if i in message.text:
            bot.send_message(message.chat.id, dict[i])
            found = True
    if not found:
        bot.send_message(message.chat.id, "в качестве аргумента используется команда")

@bot.message_handler(commands=["users"])
def users(message):
    if message.from_user.id in admins or message.from_user.username in admins:
        f = open('users.txt', 'r', encoding='windows-1251')
        param = f.read()
        for i in param.split('\n'):
             if i == '':
                continue
             bot.send_message(message.chat.id, i)
             print(i)
        f.close()
    else:
        bot.send_photo(message.chat.id, 'https://i.ytimg.com/vi/Uf8NBVdQ2uk/maxresdefault.jpg', caption='PATHETIC!')

@bot.message_handler(content_types=["text"])
def getMessage(message):
    global new_user
    if new_user:
        print(message.text)
        f = open('users.txt', 'a+')
        f.write(str(message.from_user.id) + "\t"+ str(message.text) + "\n")
        f.close()
        new_user = False
        bot.send_message(message.chat.id, "Ну Привет, " + str(message.text))
    else:
        print(
            "UserID: " + str(
                message.from_user.id) + "\n" + "Username: " + message.from_user.first_name + "\n" + "Message: " + message.text)
        file_name = 'users\\' + (str(message.from_user.id)) + ".txt"
        f = open(file_name, 'a+')
        f.write(message.text + '\n')
        f.close()



@bot.message_handler(content_types=["sticker"])
def sticker(message):
    bot.send_message(message.chat.id, 'Зачем ты мне стикеры кидаешь, шизоид?')
    print(
        "UserID: " + str(
            message.from_user.id) + "\n" + "Username: " + message.from_user.first_name + "\n" + "Message: " + message.text)
    file_name = 'users\\' + (str(message.from_user.id)) + ".txt"
    f = open(file_name, 'a')
    f.write(message.text + '\n')
    f.close()



# 477216795
# 1149744369 shiz0id
# 1014838346 Roman
# 406661822 neongm
if __name__ == '__main__':
    bot.infinity_polling()
