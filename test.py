import requests
import urllib
import os


url = 'https://kongxianglunba.tumblr.com/video_file/t:vh_wu0IPj02kXHw1ztBGFQ/137956884927/tumblr_nhfwe8mxnp1qdt9cn'
_dir = r'C:\Users\jms29\Downloads\video'
filename = url.split('/')[-1] + '.mp4'
file_path = os.path.join(_dir, filename)
with open (file_path,'wb') as f:
    f.write(requests.get(url).content)

