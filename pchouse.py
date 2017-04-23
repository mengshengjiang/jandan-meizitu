from urllib.request import urlopen
from urllib.request import urlretrieve
from bs4 import BeautifulSoup
import re
import os
'''
这是打开了一个有关碧玉盆栽的介绍的网站，里面的图片分为碧玉图片和广告图片，根据性质的不同，

将他们下载下来，自动保存到两个不同的文件夹里
'''




html = urlopen("http://www.pchouse.com.cn/baike/shenghuo/2745/")
bsObj = BeautifulSoup(html,"html.parser")

#获取网站中所有碧玉的图片
Biyus = bsObj.findAll("p",{"style":re.compile("^text-align")})
links = [] 

for x in Biyus:
#for i,x in enumerate(Biyus):
    #print(x.find("img").attrs["src"])
    links.append(x.find('img').attrs['src'])

#print(links)

# #directory=os.path.dirname("C:\\image\\mqq"+str[i]+".jpg")
directory = "C:\\image\\mqq"
if not os.path.exists(directory):
    os.makedirs(directory)

i = 0
for link in links:
    filename = "C:\\image\\mqq\\" + str(i) +'.jpg'
    try:
        urlretrieve(link,filename)
    except:
        print("获取{}失败".format(link))
    i = i + 1


#获取所有广告类图片
Ads=bsObj.findAll("img",{"width":{"120","310"}})
#print(Ads)
ad_links = []
for n in Ads:
    ad_links.append(n.attrs['src'])
print(ad_links)
# for i,ad in enumerate(Ads):
#     print(ad.attrs["src"])

directory = "C:\\image\\ads"
if not os.path.exists(directory):
    os.makedirs(directory)

i = 0
for link in ad_links:
    filename = "C:\\image\\ads\\" + str(i) +'.jpg'
    urlretrieve(link,filename)
    i = i + 1
# urlretrieve(ad.attrs["src"],directory)
















