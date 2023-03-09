import pdfplumber
from gtts import gTTS
from pathlib import Path


# ORIGINAL CODE https://youtu.be/Q0lHb-FCATk


def pdf_tomp3(file_path='test.pdf', lang='en'):

    if Path(file_path).is_file() and Path(file_path).suffix == '.pdf':
        # открываем файл для записи, "rb" т.к пдф
        with pdfplumber.PDF(open(file=file_path, mode='rb')) as pdf:
            pages = [page.extract_text() for page in pdf.pages]
        # единый текст
        txt = ''.join(pages)
        # сносы строк в топку
        txt = txt.replace('\n', ' ')
        # записыфваем в файлик
        with open('file.txt', mode='w') as f:
            f.write(txt)
        # читаем текст языком робота
        my_mp3 = gTTS(text=txt, lang=lang)
        # имя файла делаем
        mp3_name = Path(file_path).stem
        my_mp3.save(f'{file_path}.mp3')
        return 'ВСЕ!'
    else:
        return 'нет такого'
