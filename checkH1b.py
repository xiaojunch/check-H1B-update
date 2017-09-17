import requests
from bs4 import BeautifulSoup

headers = {
        'Accept': 'text/html, application/xhtml+xml, image/jxr, */*',
        'Accept-Encoding': 'gzip, deflate',
        'Accept-Language':
        'en-US, en; q=0.8, zh-Hans-CN; q=0.5, zh-Hans; q=0.3',
        'Cache-Control': 'no-cache',
        'Connection': 'Keep-Alive',
        'Content-Type': 'application/x-www-form-urlencoded',
        'Host': 'egov.uscis.gov',
        'Referer': 'https://egov.uscis.gov/casestatus/mycasestatus.do',
        'User-Agent':
        'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/46.0.2486.0 Safari/537.36 Edge/13.10586'
    }
url = "https://egov.uscis.gov/casestatus/mycasestatus.do"
data = {'changeLocale':'', "appReceiptNum": 'eac1713754536', 'initCaseSearch': 'CHECK+STATUS'}

res = requests.post(url, data=data, headers=headers)

soup = BeautifulSoup(res.text,"lxml")

soup.find('div',{'class':"rows text-center"}).h1.text