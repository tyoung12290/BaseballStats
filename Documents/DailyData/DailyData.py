from selenium import webdriver
import pandas as pd
import psycopg2
from pandas.io.html import read_html
from pandas import DataFrame
from bs4 import BeautifulSoup
import platform
import time
from sqlalchemy import create_engine
import time

username = 'tyoung1229'
password = 'Tjytjy90'
ts = time.time()*1000
stats = DataFrame()
baseUrl = "http://mlb.mlb.com/stats/sortable.jsp#elem=%5Bobject+Object%5D&tab_level=child&click_text=Sortable+Player+hitting&game_type='R'&season=2018&season_type=ANY&league_code='MLB'&sectionType=sp&statType=hitting&"
variableUrl = "page=All&ts={}&timeframe=d1&split=&last_x_days=1".format(ts)
Url = baseUrl + variableUrl
print(Url)
#"https://www.baseball-reference.com/leagues/MLB/2017-standard-batting.shtml"

driver = webdriver.PhantomJS()
driver.set_window_size(1024, 768) # optional
driver.get(Url)
time.sleep(1)
stats_list = pd.read_html(driver.page_source,attrs={'class': 'stats_table'} )
#stats_list = pd.read_html(driver.page_source,attrs={'id': 'players_standard_batting'} )
print("html to table")
print(stats_list)
stats = stats_list[0]
cols = [0,18,19,20,21,22,23,24,25,26,27,28,29,30,31]
stats.drop(stats.columns[[cols]],inplace=True,axis=1)
print(stats)
stats.columns=['Player','Team','Pos','G','AB','R','H','2B','3B','HR','RBI','BB',
				'SO','SB','CS','AVG','OBP']

engine = create_engine('postgresql://tyoung12290:Tjytjy90@mlb.ck81qylct4si.us-east-2.rds.amazonaws.com:5432/MLB')

stats.to_sql("player_game_data",engine,if_exists='replace')
#print("table to database")
