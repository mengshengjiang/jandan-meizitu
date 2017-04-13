import urllib.request
from bs4 import BeautifulSoup
import os



def get_html(url):
	#请求
	req = urllib.request.Request(url)
	#响应
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





def download(start,end):
	#创建 photo 文件夹
	if not os.path.exists('photo'):
		os.makedirs('photo')

	for x in range(start,end+1):
		#创建文件夹
		if not os.path.exists('photo\\meizitu'+str(x)):
			os.makedirs('photo\\meizitu'+str(x))
		
		url = 'http://jandan.net/ooxx/page-'+ str(x)+ '#comments'
		html = get_html(url)
		links = get_links(html)
		
		i=0
		for link in links:
			filename ='photo\\meizitu'+str(x)+'\\'+str(i)+ '.png'
			with open(filename,'w'):
				try:
					urllib.request.urlretrieve(link,filename)
				except:
					print("获取图片%s失败！"%filename)
			i += 1

if __name__ == '__main__':
	start = int(input('请输入开始页面(1-2400):  '))
	end = int(input('请输入结束页面(1-2400):  '))
	assert 1 < start < end < 2400
	download(start,end)









