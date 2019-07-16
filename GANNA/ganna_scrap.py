import requests
from bs4 import BeautifulSoup
import pprint
import webbrowser
url="https://gaana.com/topcharts"
req_=requests.get(url)
# print(req_)
soup=BeautifulSoup(req_.text,"html.parser")
main_div=soup.find('ul',class_="content-container artworkload clearfix a-list")


get_name=main_div.find_all('div',class_="arwtork_label")
# print(get_)
count=0
for i in get_name:
	a_=i.find('a').get_text()
	count+=1
	print(count,a_)
get_=main_div.find_all('div',class_="hover-events-parent")
list_=[]
for i in get_:
	link=(i.find('a').get('href'))
	# print(link)
	com_link=("https://gaana.com" + link)
	list_.append(str(com_link))
# pprint.pprint(list)
user=int(input('enter >'))
print(list_[user-1])
req_2=requests.get(list_[user-1])
print(req_2)
soup=BeautifulSoup(req_2.text,"html.parser")
# print(soup)......................................................................###
main_div=soup.find("div",class_="innercontainer")
# time=main_div.find_all("li",class_="s_duration")

div = main_div.find_all("div",class_="playlist_thumb_det")
# print(div)

## scrape all hindi song according the user input##..........................##
Url_list=[]
count=1
for i in div:
	url=(i.find('a').get('href'))
	# print(url)

	Url_list.append(url)
	name = (i.find('a').text)
	print(count,name)
	count+=1
user1=int(input("enter the number of song:"))
link = Url_list[user1-1]
# print(link)
webbrowser.open_new_tab(link)


