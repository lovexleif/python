#coding:utf-8

from bs4 import BeautifulSoup
from urllib.parse import urljoin
import requests
import csv
import html5lib

URL = 'http://sz.ganji.com/fang1/h1/'
ADDR = 'http://sz.ganji.com'
header = {  # 请求头部
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64; rv:55.0) Gecko/20100101 Firefox/55.0",
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
    "Accept-Language": "zh-CN,zh;q=0.8,en-US;q=0.5,en;q=0.3",
    "Accept-Encoding": "gzip, deflate",
    "Referer": "http://zkeeer.space/",
    "Connection": "keep-alive",
    "Upgrade-Insecure-Requests": "1"
}
def main():
    start_page = 1
    end_page = 10
    price = 7
    with open('ganji.csv','wb') as f:
        csv_writer = csv.writer(f,delimiter = ',')    
        print('start.....')
        while start_page < end_page+1:
            start_page =start_page+1
            print('get:{0}'.format(URL.format(page = start_page,price = price)))
            response = requests.get(URL.format(page = start_page,price = price),headers=header)
            #第一个参数是抓取的HTML文本，第二个是使用那种解释器
            html =BeautifulSoup(response.text,'html.parser')
            print(html)
            #获取房源信息
            house_list = html.select('.f-list>.f-list-item>.f-list-item-wrap')
            print(house_list)
            if not house_list:
                break
            for house in house_list:
                house_title = house.select('.title > a')[0].string.encode('utf-8')
                house_addr1 = house.select('.address-eara>a')[0].string.encode('utf-8')
                house_addr2 = house.select('.address-eara>a')[1].string.encode('utf-8')
                house_addr3 = house.select('.address-eara>a')[2].string.encode('utf-8')
                house_price = house.select('.info>.price>.num')[0].string.encode('utf-8')
                house_url = urljoin(ADDR,house.select('.title>a')[0]['href'])
                csv_write.writerow([house_title,house_addr1,house_addr2,house_addr3,house_price,house_url])
        print('end......')
main()
