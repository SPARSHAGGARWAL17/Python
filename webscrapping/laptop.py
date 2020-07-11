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
_name = 1
_price = 2
_rating = 3
def driver():
    browser = webdriver.Chrome('D:\\Work\\Work2\\chromedriver.exe')
    browser.get('https://www.amazon.in/s?k=laptop&ref=nb_sb_noss')
    page = browser.page_source
    soup = BeautifulSoup(page,features='lxml')
    return soup
def get_data(soup):
    time.sleep(5)
    data = {}
    data['name'] = []
    data['price'] = []
    data['ratings'] = []
    for i in soup.findAll(name='div', attrs={'class': 's-include-content-margin s-border-bottom s-latency-cf-section' }):
        a = i.find(name='span', attrs={
                   'class': 'a-size-medium a-color-base a-text-normal'})
        p = i.find(name='span', attrs={'class': 'a-offscreen'})
        r = i.find(name='span', attrs={'class': 'a-icon-alt'})
        data['name'].append(a.text)
        if p != None:
            data['price'].append(p.text)
        else:
            data['price'].append('None')
        if r != None:
            rat = r.text.split(' ')[0]
            data['ratings'].append(rat)
        else:
            data['ratings'].append('None')
    print('Data Successfully Scrapped.')
    return(data)
def load_data(sheet,workbook,data):
    row = sheet.max_row+1
    for i in range(len(data['name'])):
        sheet.cell(row+i,_name).value = data['name'][i]
        sheet.cell(row+i,_price).value = data['price'][i]
        sheet.cell(row+i,_rating).value = data['ratings'][i]
    workbook.save(file)
    print('File saved Successfully!')
soup = driver()
data = get_data(soup)
load_data(sheet,workbook,data)
