import os, socket

commands = ['cd', 'ls', 'nano', 'mkdir']
currentPath = '~'
user = '$'
login = os.getlogin()
hostname = socket.gethostname()
currentDirectory = '~'
start = login + '@' + hostname + ':' + currentDirectory + user + ' '
home = ['Desktop', 'Downloads', 'Pictures', 'snap', 'Videos', 'Documents', 'Music', 'Public', 'Templates']
nanopath = 'file://' + os.getcwd() + '/files/nano.html'