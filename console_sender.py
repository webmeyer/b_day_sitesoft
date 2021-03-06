from PyQt5 import QtCore, QtGui, QtWidgets
from bs4 import BeautifulSoup
from selenium.common.exceptions import NoSuchElementException
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
import time
import random
import os
from gui import *
from selenium import webdriver

firefox_options = webdriver.FirefoxOptions()
firefox_options.add_argument('--headless')
firefox_options.add_argument('--no-sandbox')
firefox_options.add_argument('user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.88 Safari/537.36')

chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument("--headless")
chrome_options.add_argument("--no-sandbox")
chrome_options.add_argument("user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.88 Safari/537.36")

FOLDER = os.getcwd()  # путь к рабочей директории
USED_LIST = []

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

def account_login(_browser, account):   # ЛОГИНИМСЯ В АКК
    acc = account.split(':')
    _email = acc[0]
    _password = acc[-1]
    _browser.find_element_by_name('email').send_keys(_email)
    _browser.find_element_by_name('password').send_keys(_password)
    _browser.find_element_by_xpath('//button[@class="button t-blue s-a"]').click()
    time.sleep(10)

def check_bday_today_and_send_message(_browser, _url):   # Для ручного режима
    soup = BeautifulSoup(_browser.page_source, 'html.parser')
    orange_blocks = soup.findAll('div', class_='c-block cg-2 t-2 t-orange message')
    for block in orange_blocks:
        bday_today = block.find('div', class_='b-important-theme').text
        bday_name = block.find('div', class_='b-important-title').text
        if bday_today == 'Сегодня отмечает день рождения':
            _browser.find_element_by_xpath("//div[@class='b-comment']//textarea[@name='message_text']").send_keys('С Днём Рождения!')
            _browser.find_element_by_xpath("//div[@class='b-comment']//input[@type='submit']").click()
            time.sleep(2)
            print('Отправил поздравление!', bday_name)

def start_work():
    url_vkp = 'https://vkp.sitesoft.su/'
    browser = webdriver.Firefox(options=firefox_options)
    browser.get(url_vkp)
    browser.implicitly_wait(10)

    soup = BeautifulSoup(browser.page_source, 'html.parser')
    account_login(browser, account_get())
    check_bday_today_and_send_message(browser, url_vkp)
    browser.close()
    browser.quit()

start_work()

