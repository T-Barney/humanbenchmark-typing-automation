import time
from selenium import webdriver
from bs4 import BeautifulSoup
import pyautogui

browser = webdriver.Chrome()

url = "https://humanbenchmark.com/tests/typing"
browser.get(url)

browser.implicitly_wait(4)

soup = BeautifulSoup(browser.page_source, 'html.parser')
spans = soup.find_all('span', class_='incomplete')
text_to_type = ''.join([span.get_text() for span in spans])
print(text_to_type)

pyautogui.write(text_to_type, interval=0)

time.sleep(9999)