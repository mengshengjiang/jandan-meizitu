import requests
import re
from bs4 import BeautifulSoup
import time
import random
import os



def create_urls(start,end):
	urls = []
	for i in range(start,end+1):

		urls.append("https://www.pexels.com/search/water/?page="+str(i))
	return urls




def get_img_url(urls):
	user_agents=[		   'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:23.0) Gecko/20130406 Firefox/23.0',
              			   'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:18.0) Gecko/20100101 Firefox/18.0',
                           'Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US) AppleWebKit/533+ \(KHTML, like Gecko) Element Browser 5.0',
                           'IBM WebExplorer /v0.94', 'Galaxy/1.0 [en] (Mac OS X 10.5.6; U; en)',
                           'Mozilla/5.0 (compatible; MSIE 10.0; Windows NT 6.1; WOW64; Trident/6.0)',
                           'Opera/9.80 (Windows NT 6.0) Presto/2.12.388 Version/12.14',
                           'Mozilla/5.0 (iPad; CPU OS 6_0 like Mac OS X) AppleWebKit/536.26 (KHTML, like Gecko) \Version/6.0 Mobile/10A5355d Safari/8536.25',
                           'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) \Chrome/28.0.1468.0 Safari/537.36',
                           'Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.0; Trident/5.0; TheWorld)']
    
	#解析出图片地址
	img_urls = []
	pattern = re.compile(r'https://images.pexels.com/photos/(.*)auto=compress&cs=tinysrgb')
	for url in urls:
		index = random.randint(0, 9)
		user_agent = user_agents[index]
		headers = {'user_agent':user_agent}
		
		res = requests.get(url,headers=headers)
		if res.status_code == 200:
			html = res.text
			soup = BeautifulSoup(html,'lxml')
			for tag in soup.find_all('img',{'src':pattern}):
				img_urls.append(tag.attrs['src'])
		else:
			print('失败{}'.format(url))


	img_urls = [re.findall(r"(.*)\?",n)[0].replace('images','static') for n in img_urls]
	return img_urls




def download_img(img_urls):
	directory = 'pexel'
	if not os.path.exists(directory):
		os.makedirs(directory)

	
	for link in img_urls:
		if link[-4:] == 'jpeg':
			filename = 'pexel\\'+re.findall(r'photos/(\d*)',link)[0] + '.jpeg'
		else:
			filename = 'pexel\\'+re.findall(r'photos/(\d*)',link)[0] + '.jpg'

		with open(filename,'wb') as f:
			res = requests.get(link) 
			if res.status_code == 200:
				f.write(res.content)
			else:
				print("无法下载{}".format(link))

urls = create_urls(1,5)
img_urls = get_img_url(urls)
download_img(img_urls)

