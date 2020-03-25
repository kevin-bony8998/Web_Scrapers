from bs4 import BeautifulSoup
import requests

def search():
	query="Coronavirus"
	f1 = open("C:/Users/KEVINBONYTHEKKANATH-/Desktop/Projects/G_News.txt","r")
	print()
	print()
	print()
	print(query+" news contained in:")
	new=f1.readlines()
	for i in new:
		if query.lower() in i.lower():
			print(i)

headers = ({'User-Agent':
            'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2228.0 Safari/537.36'})

count = 0

f = open("C:/Users/KEVINBONYTHEKKANATH-/Desktop/Projects/G_News.txt","w+")


url_main = "https://news.google.com/?hl=en-IN&gl=IN&ceid=IN:en"
response_main = requests.get(url_main,timeout=20000)
content_main = BeautifulSoup(response_main.content,"html.parser")

news=[]
check=0
reps=0
for out in content_main.find_all('main',attrs = {"jsname": "fjw8sb"}):
	for tweet in out.find_all('article',attrs = {"jscontroller": "mhFxVb"}):
		word=""
		for q in tweet.find('a', attrs={'class': 'DY5T1d'}).text:
			if ((ord(q)>=32) and (ord(q)<=127)):
				word = word+q
		#print("Tweet "+str(tweet))
		if word not in news:
			news.append(word)
			print(word)
			link = tweet.find('a', attrs={'class': 'DY5T1d'})['href']
			temp=link
			link = "news.google.com"+(str(temp))[1:]
			time_date = tweet.find('time', attrs={'class':'WW6dff uQIVzc Sksgp'})['datetime']
			date=time_date[0:10]
			time=time_date[11:(len(time_date)-1)]
			print()
			f.write(word)
			f.write("\n")
			f.write(link)
			f.write("\n")
			f.write(date)
			f.write("\n")
			f.write(time)
			f.write("\n")
		else:
			reps=reps+1
			if reps>len(news):
				check=1
		if check==1:
			break
		f.write("\n")
		f.write("\n")

f.close()
search()


