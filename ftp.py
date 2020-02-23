import os
import ftplib

path = '/home/ubuntu/'
filename = 'nginx.tar'

ftp = ftplib.FTP("172.31.48.17") 
ftp.login("ubuntu", "ubuntu1234") 
ftp.cwd(path)
ftp.retrbinary("RETR " + filename, open(filename, 'wb').write)
ftp.quit()
