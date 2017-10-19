#coding: utf-8
from bs4 import BeautifulSoup
from urllib.parse import urljoin # Python3
import requests
import csv
import time
import random
url = "http://bj.58.com/pinpaigongyu/pn/{page}/?minprice=2000_3000"
page = 0
csv_file = open("rent.csv","w", -1,"UTF-8")# 指定encoding模式
csv_writer = csv.writer(csv_file, delimiter=',')

while True:
    page += 1
    print("fetch: ", url.format(page=page))
    response = requests.get(url.format(page=page))# 抓取目标页面
    html = BeautifulSoup(response.text,"html.parser")# 指定parser解析器"html.parser"
    house_list = html.select(".list > li")# 获取class=list的元素下的所有li元素

    if not house_list:
        break
    
    for house in house_list:
        house_title = house.select("h2")[0].string
        house_url = urljoin(url, house.select("a")[0]["href"])# 获取绝对路径
        house_info_list = house_title.split()

        if "公寓" in house_info_list[1] or "青年社区" in house_info_list[1]:
            house_location = house_info_list[0].split("】")[1]
        else:
            house_location = house_info_list[1]

        house_money = house.select(".money")[0].select("b")[0].string
        csv_writer.writerow([house_title, house_location, house_money, house_url])# 按行写入csv文件
    key = random.randint(2,4)
    if page%key == 0:
        time.sleep(key)
csv_file.close()
