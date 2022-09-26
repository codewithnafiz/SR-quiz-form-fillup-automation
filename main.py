import datetime
from dateutil.relativedelta import relativedelta
from selenium import webdriver
import time
import pandas as pd
import xlsxwriter

# workbook = xlsxwriter.Workbook('nafizdone.xlsx')
# worksheet = workbook.add_worksheet()

from selenium.webdriver.common.alert import Alert

web = webdriver.Chrome()
# worksheet.write(0, 0, 'name')
row = 1

def fillform(li):
    web.get('https://quiz.sheikhrussel.gov.bd/quiz/profile')
    web.implicitly_wait(7)
    last = web.find_element("xpath", '//*[@id="main"]/section[2]/div/div/div[3]/div/table/tbody/tr[15]/td/button[1]')
    last.click()
    web.implicitly_wait(2)
    last = web.find_element("xpath", '//*[@id="form"]/div[7]/div/select/option[3]')
    last.click()
    time.sleep(3)
    last = web.find_element("xpath", '//*[@id="form"]/div[20]/div/input')
    last.click()
    time.sleep(2)
    web.switch_to.alert.accept()
    last = web.find_element("xpath", '//*[@id="header"]/div/nav/ul/li[3]/a')
    last.click()
    web.implicitly_wait(5)


def signup(li):
    web.get('https://quiz.sheikhrussel.gov.bd/login')
    web.implicitly_wait(2)
    last = web.find_element("xpath", '//*[@id="exampleInputEmail1"]')
    last.send_keys('0' + str(li[3]))
    last = web.find_element("xpath", '//*[@id="exampleInputPassword1"]')
    last.send_keys(li[3])
    last = web.find_element("xpath", '/html/body/div/div/div/div/div/div/form/div[3]/label/input')
    last.click()
    last = web.find_element("xpath", '/html/body/div/div/div/div/div/div/form/div[4]/input')
    last.click()
    time.sleep(2)
    if web.current_url == 'https://quiz.sheikhrussel.gov.bd/login':
        return
    fillform(li)


# def fill(li):
#     if relativedelta(datetime.datetime.now(), li[5]).years>=13:
#         web.get('https://quiz.sheikhrussel.gov.bd/kha_group_registration')
#     else:
#         web.get('https://quiz.sheikhrussel.gov.bd/ka_group_registration')
#     time.implicitly_wait(2)
#     last = web.find_element("xpath", '//*[@id="exampleInputEmail1"]')
#     last.send_keys(li[0])
#     RadioButtonPeriod = web.find_element("xpath", '/html/body/div/div/div/div/div/div/form/div[2]/input[2]')
#     RadioButtonPeriod.click()
#     last = web.find_element("xpath", '//*[@id="mobile"]')
#     last.send_keys('0'+str(li[3]))
#     last = web.find_element("xpath", '//*[@name="password"]')
#     last.send_keys(li[3])
#     last = web.find_element("xpath", '//*[@name="password_confirmation"]')
#     last.send_keys(li[3])
#     last = web.find_element("xpath", '/html/body/div/div/div/div/div/div/form/div[5]/select[1]')
#     last.send_keys(li[5].date().day)
#     last = web.find_element("xpath", '/html/body/div/div/div/div/div/div/form/div[5]/select[2]')
#     last.send_keys(li[5].date().month)
#     last = web.find_element("xpath", '/html/body/div/div/div/div/div/div/form/div[5]/select[3]')
#     last.send_keys(li[5].date().year)
#     last = web.find_element("xpath", '/html/body/div/div/div/div/div/div/form/div[6]/select/option[2]')
#     last.click()
#     last = web.find_element("xpath", '/html/body/div/div/div/div/div/div/form/div[8]/div/label/input')
#     last.click()
#     while True:
#         if web.current_url=='https://quiz.sheikhrussel.gov.bd/login':
#             signup(li)
#             return True

if __name__ == '__main__':
    df = pd.read_excel('nafiz.xlsx', sheet_name=0)
    for i in df.values:
        if i[-1] == 'valid':
            signup(i)
        # else:
        #     worksheet.write(row, 0, i[0])
        #     worksheet.write(row, 1, 'invalid info')
        # row+=1
    # workbook.close()
