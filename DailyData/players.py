#scrape/call API to retrieve list of players to player table
#drop and recreate daily or update
#uses cases include trades singings minor league call ups
#disabled flag at this level?

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

username = 'tyoung12290'
password = 'Tjytjy90'
ts = time.time()*1000
stats = DataFrame()
baseUrl = "https://rotogrinders.com/pages/mlb-pitcher-hub-sp-salary-charts-260515"
Url = baseUrl
print(Url)

driver = webdriver.PhantomJS()
driver.set_window_size(1024, 768) # optional
driver.get(Url)
time.sleep(1)
stats_list = pd.read_html(driver.page_source,attrs={'class': 'tbl data-table dataTable no-footer'} )
stats_df =stats_list[1]
print(stats_list)
#stats_list = pd.read_html(driver.page_source,attrs={'id': 'players_standard_batting'} )
print("html to table")
#stats_df.columns = ['Num','Player', 'Pos', 'Bat', 'THW', 'AGE','HT', 'WT', 'BORN', 'SALARY' ]
#filteredTable = stats_df.loc[stats_df['Player'] !="NAME"]
#cleanTable = filteredTable[filteredTable.Player.notnull()])


#stats = stats_list[0]
#cols = [0,18,19,20,21,22,23,24,25,26,27,28,29,30,31]
#stats.drop(stats.columns[[cols]],inplace=True,axis=1)
#print(stats)
#stats.columns=['Player','Team','Pos','G','AB','R','H','2B','3B','HR','RBI','BB',
#				'SO','SB','CS','AVG','OBP']

#engine = create_engine('postgresql://tyoung12290:Tjytjy90@mlb.ck81qylct4si.us-east-2.rds.amazonaws.com:5432/MLB')

#stats.to_sql("player_game_data",engine,if_exists='replace')
#print("table to database")
