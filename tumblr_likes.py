import os
import requests
import lxml
from bs4 import BeautifulSoup

url = 'https://www.tumblr.com/login'
ua = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/61.0.3163.100 Safari/537.36'
headers = {
	'User-Agent':ua,

}

s = requests.Session()
r = s.post(url, headers=headers)
soup = BeautifulSoup(r.text,'lxml')
form_key = soup.find('meta',attrs={'name':'tumblr-form-key'})['content']
payload = {
	'user[email]':'username',
	'user[password]':'password',
	'form_key':form_key,
}

s.post(url, headers=headers, data=payload)

links_toget = ['https://www.tumblr.com/likes/page/' + str(num) for num in range(1,8)]
vurls = []
for link in links_toget:
	r = s.get(link)
	soup = BeautifulSoup(r.text,'lxml')
	for source in soup.find_all('source'):
		vurls.append(source['src'])

_dir = r'C:\Users\jms29\Downloads\video\tumblr'
if not os.path.exists(_dir):
	os.mkdir(_dir)

length = len(vurls)
count = 0
for url in vurls:
	filename = str(count) + '.mp4'
	file_path = os.path.join(_dir, filename)
	with open(file_path, 'wb') as f:
		count += 1
		print('downloading %d/%d	 %s  ...'%(count,length,url))
		f.write(requests.get(url).content)


