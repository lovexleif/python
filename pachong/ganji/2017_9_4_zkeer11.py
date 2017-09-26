import requests

tar_url = "http://zkeeer.space"  # 目标网页
param = {"p": 383}  # 请求头的参数
header = {  # 请求头部
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64; rv:55.0) Gecko/20100101 Firefox/55.0",
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
    "Accept-Language": "zh-CN,zh;q=0.8,en-US;q=0.5,en;q=0.3",
    "Accept-Encoding": "gzip, deflate",
    "Referer": "http://zkeeer.space/",
    "Connection": "keep-alive",
    "Upgrade-Insecure-Requests": "1"
}
url_response = requests.get(url=tar_url, params=param, headers=header)
print(url_response.status_code, url_response.text)
