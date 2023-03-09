import pdfplumber
from gtts import gTTS
from pathlib import Path
from getmp3 import pdf_tomp3


def main():
    filename = input('имя файла пж:')
    lang = input('язык пж')
    print(pdf_tomp3(file_path=filename, lang=lang))


if __name__ == '__main__':
    main()