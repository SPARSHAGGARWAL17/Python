from bs4 import BeautifulSoup
from selenium import webdriver
import time
import openpyxl as op
# FILE NAME GOES HERE
file = 'data.xlsx'
_name = 1
_price = 2
_rating = 3
data = {}
data['name'] = []
data['price'] = []
data['ratings'] = []
browser = webdriver.Chrome('D:\\Work\\Work2\\chromedriver.exe')
browser.get('https://www.amazon.in/s?k=laptop&ref=nb_sb_noss')
def get_data(data):
    page = browser.page_source
    soup = BeautifulSoup(page)
    time.sleep(5)
    for i in soup.findAll(name='div', attrs={'class': 's-include-content-margin s-border-bottom s-latency-cf-section'}):
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
def load_data(data):
    workbook = op.load_workbook(file)
    sheet = workbook['Sheet1']
    print(len(data['name']))
    for i in range(len(data['name'])):
        row = 2+i
        if sheet.cell(row,_name).value == None:
            sheet.cell(row,_name).value = data['name'][i]
            sheet.cell(row,_price).value = data['price'][i]
            sheet.cell(row,_rating).value = data['ratings'][i]
    workbook.save(file)
    workbook.close()
    print('File saved Successfully!')
for i in range(5):
    data = get_data(data)
    time.sleep(2)
    print(f'Page {i+1} done.')
    time.sleep(2)
    browser.find_element_by_xpath(f'//a[text()="Next"]').click()
load_data(data)
