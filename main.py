from getmp3 import pdf_tomp3
import telebot
from pathlib import Path

token = '5839887390:AAFQi0mI1Vw-Mur0sHmPE3kuYpyZaRExLns'

bot = telebot.TeleBot(token)


@bot.message_handler(commands=['start'])
def start_msg(message):
    bot.send_message(message.chat.id, 'Привет! Я - ботяра, который может "прочитать" глупым роботским голосом текcт, '
                                  'PDF файл или текcтовый файл в формате mp3. Я создан только для этого,'
                                      ' так что сразу отправляйте мне файл, '
                                      'больше ничего жмать не надо)')


@bot.message_handler(content_types=['document'])
def handle_docs_photo(message):
    chat_id = message.chat.id
    src = 'C:/Users/Владик/OneDrive/Рабочий стол/Tgbot-PDF-to-sound/' + message.document.file_name
    try:
        file_info = bot.get_file(message.document.file_id)
        downloaded_file = bot.download_file(file_info.file_path)
        with open(src, 'wb') as new_file:
            new_file.write(downloaded_file)
            new_file.close()

    except:
        bot.send_message(message.chat.id, 'Я так особо не разбирался, но вы что то сделали не так. Пожалуйста, следуйте указаниям')

    bot.send_message(message.chat.id,
                     'Отлично! Теперь скажите, на каком языке прочитать? (en - английский, ru - русский)')

    @bot.message_handler(content_types=['text'])
    def on_message(message):
        chat_id = message.chat.id
        text = message.text
        mp3_name = pdf_tomp3(file_path=src, lang=f'{text}')
        bot.send_document(chat_id, open(f'{mp3_name}.mp3', 'rb'))


def main():
    bot.polling(none_stop=True)


if __name__ == '__main__':
    main()