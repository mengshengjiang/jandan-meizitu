import requests
from bs4 import BeautifulSoup
import os
from multiprocessing.dummy import Pool as ThreadPool
import time

def get_html(url):
	return requests.get(url).text

def get_links(html):
	soup = BeautifulSoup(html,'lxml')
	img_tags = soup.find_all('img')
	links = []
	for x in img_tags:
		links.append('http:'+ x.get('src'))
	return links

def download(links):
	for link in links:
		filename = 'photo\\' + link[28:]
		try:
			with open(filename,'wb') as f:
				f.write(requests.get(link).content)
				f.close()
		except:
			print('下载失败')

def meizitu_thread(start_page,end_page):
	if not os.path.exists('photo'):
		os.makedirs('photo')
	#构造 url
	num = list(range(start_page,end_page+1))
	urls = []
	for x in num:
		url = 'http://jandan.net/ooxx/page-' + str(x) + '#comments'
		urls.append(url)
	
	pool = ThreadPool(4)
	time_start1 = time.time()

#获取html,解析出链接，下载图片
	htmls = map(get_html,urls)
	meizitu_links = map(get_links,htmls)
	for x in map(download,meizitu_links): 
		pass

	pool.close()
	pool.join()
	time_end1 = time.time()
	print('耗时',time_end1 - time_start1)

if __name__ == '__main__':
	start_page = int(input('请输入开始页面:  '))
	end_page = int(input('请输入结束页面:  '))
	meizitu_thread(start_page,end_page)
