import requests
import os
from bs4 import BeautifulSoup
'''
windows, download your liked video in tumblr
11/1/2017
'''

UA = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/61.0.3163.100 Safari/537.36'
HEADERS = {
	'User-Agent':UA,

}

# HTTPS_PROXY = "https://127.0.0.1:1080"
# PDICT = {
# 	"https":HTTPS_PROXY,
# }

login_url = 'https://www.tumblr.com/login'
dash_url = 'https://www.tumblr.com/dashboard'









def get_formkey(r):
	soup = BeautifulSoup(r.text,'lxml')
	formkey = soup.find('meta',attrs={'name':'tumblr-form-key'})['content']
	# print(formkey)
	return formkey

def get_vurls(s, likes_num):
	nums =  likes_num//11 + 1
	links_toget = ['https://www.tumblr.com/likes/page/' + str(num) for num in range(1,nums)]
	
	vurls = []
	for link in links_toget:
		r = s.get(link)
		soup = BeautifulSoup(r.text,'lxml')
		for source in soup.find_all('source'):
			vurls.append(source['src'])
	return vurls


def download_video(vurls, _dir):
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

if __name__ == '__main__':
	default_dir = 'C:\\Users\\jms29\\Downloads\\video\\tumblr'
	_dir = input('where to store videos(press enter to set to %s):	' % default_dir) 	or default_dir
	username = input('your username:	')
	password = input('your password:	')
	likes_num = int(input('likes number of your account:	'))
	# visit loginurl to get form key
	s = requests.Session()

	r = s.post(login_url, headers=HEADERS)
	formkey = get_formkey(r)
	payload = {
		'user[email]':username,	
		'user[password]':password,
		'form_key':formkey,
	}
	# successfully login
	s.post(login_url, headers=HEADERS, data=payload)
	# get vulrs
	vurls = get_vurls(s,likes_num)
	print(vurls)
	# download
	download_video(vurls, _dir)




































# url = 'https://stackoverflow.com/questions/8287628/proxies-with-python-requests-module'
# s = requests.Session()
# res = s.get(url, proxies=pdict)
# print(res.text,res.status_code)
