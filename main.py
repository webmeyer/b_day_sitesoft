from bs4 import BeautifulSoup
import requests
from selenium.common.exceptions import NoSuchElementException
from selenium import webdriver
import time
import random
import os
chrome_options = webdriver.ChromeOptions()
chrome_options.binary_location = os.environ.get("GOOGLE_CHROME_BIN")
chrome_options.add_argument("--headless")
chrome_options.add_argument("--disable-dev-shm-usage")
chrome_options.add_argument("--no-sandbox")
chrome_options.add_argument("user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.88 Safari/537.36")

def account_get():
    folder = os.getcwd()  # путь к рабочей директории
    file = open(folder + '/acc.txt', 'r')  # файл с аккаунтами
    for line in file.readlines():  # берём строку с данными для логина
        line = line.strip()
        account = line.split(':')
        email = account[0]
        password = account[1]
        acc = email + ':' + password
        return acc

def create_bday_message():
    bday_textlist = []
    folder = os.getcwd()  # путь к рабочей директории
    file = open(folder + '/bday_text.txt', 'r', encoding='utf-8')  # файл с поздравлениями
    for _text in file.readlines():
        bday_textlist.append(_text)
    bday_message_raw = random.choice(bday_textlist)
    bday_message = bday_message_raw.replace("&nbsp;", " ")
    for string in bday_textlist:   # Удаляем поздравление из списка
        if bday_message_raw in string:
            bday_textlist.remove(string)

    return bday_message

def main():
    url_vkp = 'https://vkp.sitesoft.su/'
    create_bday_message()
main()