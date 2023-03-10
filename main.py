from getmp3 import pdf_tomp3
import telebot

token = '5839887390:AAFQi0mI1Vw-Mur0sHmPE3kuYpyZaRExLns'

bot = telebot.TeleBot(token)


@bot.message_handler(commands=['start'])
def start_msg(message):
    bot.send_message(message.chat.id, 'Привет! Я - ботяра, который может "прочитать" глупым роботским голосом текcт, '
                                  'PDF файл или тектовый файл в формате mp3')

bot.polling(none_stop=True)

def main():
    filename = input('имя файла пж:')
    lang = input('язык пж')
    print(pdf_tomp3(file_path=filename, lang=lang))


if __name__ == '__main__':
    main()