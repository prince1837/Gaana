import requests,webbrowser
from pprint import pprint
from bs4 import BeautifulSoup
from pprint import pprint
u="https://gaana.com/"
url=requests.get(u)
soup=BeautifulSoup(url.text,"html.parser")
chart=soup.find("div",{"class":"carousel","id":"topchartsCarousel"})
top_one=chart.find("h2",{"id":"themechange","class":"themechange"})
link=top_one.find("a").get("href")
add_link='https://gaana.com%26/#39;+(link)+''
new_url=requests.get(add_link)
new_soup=BeautifulSoup(new_url.text,"html.parser")
top_chart=new_soup.find("ul",class_="content-container artworkload clearfix a-list")
all_div=top_chart.find_all("div",class_="hover-events-parent")
all_top_gaana=[]
def top_list_gaana(div):
	count=1
	for i in div:
		com=i.find("a").get("href")
		all_top_gaana.append("https://gaana.com%26quot%3B+com%29/
		cut=com[19:]
		print(count,cut)
		count+=1
	return(all_top_gaana)

top_list_gaana(all_div)


def one_gaana(gaana):
	append_song=[]
	user=int(input("aap konsa gaana suna chahte ho\n"))
	o_open=gaana[user-1]
	# print(o_open)
	user_get=requests.get(o_open)
	b_soup=BeautifulSoup(user_get.text,"html.parser")
	data_div=b_soup.find("div",class_="s_c")
	ul_id=data_div.findAll("div",class_="playlist_thumb_det") 
	num=1
	append_song=[]
	for i in ul_id:
		name=i.find("a").get_text()
		print(num,name)
		num+=1
		f_data=i.find("a").get("href")
		append_song.append(f_data)
	return(append_song)
playlist=one_gaana(all_top_gaana)

def play_music(alist):
	user=int(input("enter one "))
	play=webbrowser.open(alist[user-1])
	print(play)
	
play_music(playlist)
