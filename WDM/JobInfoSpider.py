# -*- coding: utf-8 -*-
from bs4 import BeautifulSoup as bs
from urllib.parse import urljoin
from urllib.request import urlopen
import csv

csv_file = open("JobFairInfo.csv","w")
csv_writer = csv.writer(csv_file, delimiter=',')
Career_url = "http://career.buaa.edu.cn/"
for i in range(22,25):
    Cpy_Names = []
    Cpy_Times = []
    Cpy_Adresses = []
    Cpy_url = []
    url = urljoin(Career_url, 'getjobFairCalMeetingInfoAction.dhtml?selectDate=2017-09-%02d' % i)
    response = urlopen(url)
    html = bs(response.read(),'html.parser')#指定parser解析器"html.parser"
    CompanyNames = html.findAll('a')
    Csstimes = html.findAll('span',{"class":"csstime"})
    Cssadresses = html.findAll('span',{"class":"cssadress"})
    for name in CompanyNames:
        Cpy_url.append(urljoin(Career_url, name["href"]))
        #上面一句中name中只有a一个tag，只能直接定位"herf"，
        #所以使用name.select("a")[0]["herf"]是不能select到"a"的
        Cpy_Names.append(name.get_text())
    for time in Csstimes:
        Cpy_Times.append(time.get_text())
    for adrs in Cssadresses:
        Cpy_Adresses.append(adrs.get_text())
    for k in range(len(Cpy_Names)):
        
        csv_writer.writerow([Cpy_Names[k], Cpy_Times[k], Cpy_Adresses[k], Cpy_url[k]])
csv_file.close()
