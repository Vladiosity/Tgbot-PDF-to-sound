import pdfplumber
from gtts import gTTS
from pathlib import Path
from fpdf import FPDF



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
        my_mp3.save(f'{mp3_name}.mp3')
        return mp3_name

        #ТУТ САМ ДЕЛАЛ, НО ПО АНАЛОГИИ С ОРИГ ВИДОСОМ
    elif Path(file_path).is_file() and Path(file_path).suffix == '.txt':
        with open(f'{file_path}', mode='r') as txfile:
            textline = txfile.read()
        textline = textline.replace('\n', ' ')
        with open('filetxt.txt', mode='w') as txf:
            txf.write(textline)
        my_mp3 = gTTS(text=textline, lang=lang)
        mp3_name = Path(file_path).stem
        my_mp3.save(f'{mp3_name}.mp3')
        return mp3_name
    else:
        return 'нет такого'

def message_text_to_mp3(text):
    with open('new_text.txt', mode='w') as nt:
        nt.write(text)
    return 'new_text.txt'

def new_one(text_message):
    new_pdf = FPDF()
    new_pdf.add_page()
    new_pdf.set_font("times", size=14)
    new_pdf.cell(200, 10, text_message, ln=1, align='L')
    new_pdf.output("your_text.pdf")
    return "your_text.pdf"
