from bs4 import BeautifulSoup as soup
from urllib.request import urlopen as req

my_url='https://timesofindia.indiatimes.com/'

uClient=req(my_url)
page_html=uClient.read()
uClient.close()
page_soup=soup(page_html,"lxml")

cont1=page_soup.find("div",{"id":"lateststories"})

#latest
header1=cont1.findAll("div",{"class":"sechead"})
print(header1[0].text+"\n")

ul=cont1.find("ul",{"data-vr-zone":"latest"})
lis=ul.findAll("li")
li=lis[0]

for li in lis:
    item=li.find('a')
    print(item.text+"\n"+item['href']+"\n")


#city
cont2=cont1.find("div",{"class":"toicity toi-widgets"})

header2=cont2.find("h2")
print("\n"+header2.text+"\n")

ul=page_soup.find("ul",{"class":"list2"})
lis=ul.findAll("li")
li=lis[0]

for li in lis:
    item=li.find('a')
    print(item.text+"\n"+item['href']+"\n")


#across india
print("\n"+header1[1].text+"\n")

ul=cont1.find("ul",{"data-vr-zone":"across_toi"})
lis=ul.findAll("li")
li=lis[0]

for li in lis:
    item=li.find('a')
    print(item.text+"\n"+item['href']+"\n")
