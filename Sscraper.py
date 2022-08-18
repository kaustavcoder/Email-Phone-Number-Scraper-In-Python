import re
import requests

url = input(str('Enter URL'))
r = requests.get(url)
c = r.content
fd = re.findall(r"[A-Za-z0-9_%+-.]+"
                 r"@[A-Za-z0-9.-]+"
                 r"\.[A-Za-z]{2,5}",c)

fs =str(fd)

fndph = re.findall(r'\+[-()\s\d]+?(?=\s*[+<])',c)
fstw = str(fndph)

def filecreate(fd):
    fo = open('emails.txt','wb')
    fw = fo.write(fd)
    print('file created')

filecreate(fs)


def phonelistcreate(ph):
    fi = open('phoneslist.txt','wb')
    fe = fi.write(ph)
    print('file created successfully')

phonelistcreate(fstw)
    




    







