default_dir = 'C:\\Users\\jms29\\Downloads\\video\\tumblr'
_dir = input('where to store videos(press enter to set to %s):' % default_dir) 	or default_dir
username = input('your username:')
password = input('your password:')

print(_dir,username,password)