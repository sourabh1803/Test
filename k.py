
from pexpect import pxssh
s = pxssh.pxssh()
if not s.login ('10.90.73.181', 'ubuntu', 'ubuntu1234'):
    print ("SSH session failed on login.")
    print(str(s))
else:
    print ("SSH session login successful")
    s.sendline ('sudo docker load --input *.tar')
    s.prompt()         # match the prompt
    print(s.before)     # print everything before the prompt.
    s.logout()
