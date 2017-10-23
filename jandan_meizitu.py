import urllib.request
from bs4 import BeautifulSoup
import os
import re



def get_html(url):
	req = urllib.request.Request(url)
	res = urllib.request.urlopen(req)
	html = res.read()
	return html


def get_links(html):
	tag = 'img'
	attribute = 'src'

	soup = BeautifulSoup(html,'lxml')
	result = soup.find_all(tag)

	links=[]
	for x in result:
		links.append('http:'+x.get(attribute))
	return links


def download(start, end):
	pattern = re.compile('\d+')
	_dir = r"C:\Users\jms29\Pictures\jandan-meizitu"
	if not os.path.exists(_dir):
		os.makedirs(_dir)


	urls = ["https://jandan.net/ooxx/page-" + str(n) + "#comments" 
									for n in range(start, end+1)]
	for url in urls:
		num = re.findall(pattern, url)[0]	
		if not os.path.exists(_dir + '\\page' + num):
			os.makedirs(_dir + '\\page' + num)

		links = get_links(get_html(url))

		i = 0
		for link in links:
			filename = _dir + '\\page' + num + '\\' + str(i)+ '.png'
			with open(filename,'w'):
				try:
					print("downloading %s.."%filename)
					urllib.request.urlretrieve(link,filename)
				except IOError:
					print("download img%s failed！"%filename)
			i += 1

if __name__ == '__main__':
	start = int(input('start page ? (1-220): '))
	end = int(input('end page ? (1-220): '))
	assert 1 < start < end < 2400
	download(start,end)
	print("download ended!")









