import itchat
import math
from PIL import Image
import os

itchat.auto_login(hotReload=True)
friends = itchat.get_friends(update=True)[0:]
user = friends[0]["UserName"]

num = 0
directory = 'wechat_image'
if not os.path.exists(directory):
    os.makedirs(directory)

for i in friends:
    filename = directory + '\\' + str(num) + '.jpg'
    with open(filename,'wb') as f:
        img = itchat.get_head_img(userName=i["UserName"])
        f.write(img)
    num += 1

ls = os.listdir(directory)

each_size = int(math.sqrt(float(640*640)/len(ls)))
lines = int(640/each_size)

image = Image.new('RGBA', (640, 640))
x = 0
y = 0
for i in range(0,len(ls)+1):
    try:
        img = Image.open(directory + "\\" + str(i) + ".jpg")
    except IOError:
        print("Error")
    else:
        img = img.resize((each_size, each_size), Image.ANTIALIAS)
        image.paste(img, (x * each_size, y * each_size))
        if x == lines:
            x = 0
            y += 1
        else:
            x += 1
image.save(directory + "\\" + "all.jpg")
itchat.send_image(directory + "\\" + "all.jpg", 'filehelper')