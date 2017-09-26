import requests

url_response=requests.get("http://zkeeer.space")
print(url_response.status_code,url_response.text)
