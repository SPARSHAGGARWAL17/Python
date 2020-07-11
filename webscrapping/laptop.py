from bs4 import BeautifulSoup
from selenium import webdriver
import time
import openpyxl as op
# FILE NAME GOES HERE
file = 'data.xlsx'
workbook = op.load_workbook(file)
sheet = workbook['Sheet1']
name = []
price =[]
rating = []
browser = webdriver.Chrome('D:\\Work\\Work2\\chromedriver.exe')
browser.get('https://www.amazon.in/s?k=laptop&ref=nb_sb_noss')
page = browser.page_source
soup = BeautifulSoup(page,features='lxml')
def get_data(soup):
    name = []
    price = []
    rating = []
    for i in soup.findAll(name='div', attrs={'class': 's-include-content-margin s-border-bottom s-latency-cf-section' }):
        a = i.find(name='span', attrs={
                   'class': 'a-size-medium a-color-base a-text-normal'})
        p = i.find(name='span', attrs={'class': 'a-offscreen'})
        r = i.find(name='span', attrs={'class': 'a-icon-alt'})
        name.append(a.text)
        if p != None:
            price.append(p.text)
        if r != None:
            rating.append(r.text.split(' ')[0])
    return(name,price,rating)
time.sleep(5)
# name,price,rating = get_data(soup)
def load_data(sheet,workbook):
    row = sheet.max_row()
    print(row)
load_data(sheet,workbook)