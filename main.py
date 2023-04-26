from getmp3 import pdf_tomp3, message_text_to_mp3, new_one
import telebot
import os
token = '5839887390:AAFQi0mI1Vw-Mur0sHmPE3kuYpyZaRExLns'

bot = telebot.TeleBot(token)


@bot.message_handler(commands=['help'])
def on_help(message):
    bot.send_message(message.chat.id, 'Вот список того, что я могу: отправьте мне файл в формате .pdf или .txt, и я скину вам mp3 с содержимым '
                                      'файла, вы также можеет выбрать язык, по умолчанию английский (en), но вы можете сделать русский (ru).'
                                      'Также я могу проxитать ваше сообщение выбраным языком, для этого отправьте собщение с таким синтаксисом:'
                                      '"Прочитай на (выберите русский или английский): ВАШЕ СООБЩЕНИЕ"(ковычки не нужны)')


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
        text = message.text.lower()
        try:
            mp3_name = pdf_tomp3(file_path=src, lang=f'{text}')
            bot.send_document(chat_id, open(f'{mp3_name}.mp3', 'rb'))
        except:
            bot.send_message(chat_id, 'Чета вы напутали..... Попробуйте еще разок!)')


@bot.message_handler(content_types=['text'])
def on_simple_text(message):
    text = message.text
    if 'Прочитай на русском:' in text:
        mp3_name = pdf_tomp3(message_text_to_mp3(text.split(': ')[1]), 'ru')
        bot.send_document(message.chat.id, open(f'{mp3_name}.mp3', 'rb'))
        os.remove(message_text_to_mp3(text.split(': ')[1]))
        os.remove(f'{mp3_name}.mp3')
    elif 'Прочитай на английском:' in text:
        mp3_name = pdf_tomp3(message_text_to_mp3(text.split(': ')[1]), 'en')
        bot.send_document(message.chat.id, open(f'{mp3_name}.mp3', 'rb'))
        os.remove(message_text_to_mp3(text.split(': ')[1]))
        os.remove(f'{mp3_name}.mp3')
    elif 'Сделай пдф:' in text:
        try:

            bot.send_document(message.chat.id, open(f"{new_one(text.split(': ')[1])}", 'rb'))
            os.remove(new_one(text))
        except UnicodeEncodeError:
            pass
    else:
        bot.send_message(message.chat.id, 'Я бы мог с вами пообщаться, если бы мой создатель дорбавил мне такой функциолнал(')


def main():
    bot.polling(none_stop=True)


if __name__ == '__main__':
    main()
