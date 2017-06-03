import requests
import re
import time
import os
import pickle
from bs4 import BeautifulSoup


def create_urls(start,end):
	urls = []
	for i in range(start,end+1):
		urls.append('http://jandan.net/duan/page-'+str(i)+'#comments')
	return urls

def get_text(urls):
	texts = {}
	for url in urls:
		html = requests.get(url).content
		soup = BeautifulSoup(html,'lxml')

		text_tags = soup.find_all('div',attrs={'class':'text'})
		vote_tags = soup.find_all('div',attrs={'class':'jandan-vote'})
		for tag in text_tags:
			text_id = tag.find('a',attrs={'href':re.compile(r'http://jandan.net/duan/page-\d*#comment-\d*')}).text
			text = []
			for n in tag.find_all('p'):
				text.append(n.text)
			if text_id not in texts.keys():
				texts[text_id] = [text,0,0]
		for tag in vote_tags:
			a = tag.find('a')
			text_id = a.attrs['data-id']
			sup = tag.find_all('span')[0].text
			unsup = tag.find_all('span')[1].text
			texts[text_id][1] = sup
			texts[text_id][2] = unsup

			
	return texts

def wash_text(texts,sup_cond,unsup_cond):
	washed_texts = {}
	for key,values in texts.items():
		if int(values[1]) > sup_cond and int(values[2]) < unsup_cond :
			washed_texts[key] = texts[key]
		else:
			pass
	return washed_texts

def save_washed_text(washed_texts, start, end):
	#构建文件夹
	directory = 'jandan_text'
	if not os.path.exists(directory):
		os.makedirs(directory)
	filename = directory + '\\page' + str(start) + '-page' + str(end) + '.pkl'
	
	with open(filename,'wb') as f:
		pickle.dump(washed_texts,f,pickle.HIGHEST_PROTOCOL)

def display_text(start,end):
	filename = 'jandan_text\\page' + str(start) + '-page' + str(end) + '.pkl'
	with open(filename,'rb') as f:
		data = pickle.load(f)

	for key,values in data.items():
		print("段子:{} 内容:{} 赞数:{} 踩数:{} \n".format(key,values[0],values[1],values[2]))


if __name__ == '__main__':
	start = int(input('起始页面:    '))
	end = int(input('结束页面:    '))
	sup_cond = int(input('赞数应多于:    '))
	unsup_cond = int(input('踩数应少于:    '))
	print('信息已接受，正在处理……')
	urls = create_urls(start,end)
	print('Urls创建完成!')
	print('开始获取初始数据……')
	texts = get_text(urls)
	print('已获得初始数据!')
	print('开始清洗初始数据……')
	washed_texts = wash_text(texts,sup_cond,unsup_cond)
	print('清洗初始数据完成')
	print('正在存入本地……')
	save_washed_text(washed_texts,start,end)
	print('已存至本地，正在读取并打印……')
	display_text(start,end)
	print('打印完成！')
