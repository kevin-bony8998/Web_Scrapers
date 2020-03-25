from bs4 import BeautifulSoup
import requests
import xlwt
from xlwt import Workbook
import time
import xlrd

headers = ({'User-Agent':
            'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2228.0 Safari/537.36'})

def alert():
	if (abs(value-change)>2.0):
		print((sheet.cell_value(count,0))+" shows a difference of 2%!")


book = xlwt.Workbook(encoding="utf-8")
sheet1 = book.add_sheet("Data",cell_overwrite_ok=True)

url_main = "https://www.moneycontrol.com/stocks/marketstats/indexcomp.php?optex=NSE&opttopic=indexcomp&index=9"
response_main = requests.get(url_main,timeout=20000, headers=headers)
content_main = BeautifulSoup(response_main.content,"html.parser")
value=0
change=0
t=0

def data_collect(sec):
	count = 0
	col=0
	word=[]
	for line in content_main.find_all('tr'):
		col=0
		wb = xlrd.open_workbook("C:/Users/KEVINBONYTHEKKANATH-/Desktop/Zelish/Codes/Stock data.xls")
		sheet = wb.sheet_by_index(0)
		for dat in line.find_all('td',attrs = {"class":"brdrgtgry"}):
			temp=dat.text.strip()
			dat=""
			for i in temp:
				if i!='\n':
					dat = dat+i
				if i=='\n':
					break
			if ((dat!="") and (dat not in word)):
				if col==0:
					word.append(dat)
				if t!=0:
					if col==4:
						value = float(sheet.cell_value(count,col))
						change = float(dat)
				sheet1.write(count,col,dat)
				col = col+1
		if col==6:
			count= count+1
		book.save("Stock data.xls")

t_end=time.time()+(60*20)
while(time.time()<t_end):
	data_collect(time.time())
	t = t+1
	if (time.time()%120==0):
		print("Calling alert function")
		alert()
	time.sleep(30)
