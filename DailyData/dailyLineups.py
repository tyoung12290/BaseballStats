import pandas as pd
from pandas.io.html import read_html
from pandas import DataFrame, Series
from bs4 import BeautifulSoup
import platform
from sqlalchemy import create_engine
import psycopg2
from selenium import webdriver
import time

#config section need to get rid of password
username = 'tyoung12290'
password = 'Tjytjy90'
Url = "http://m.mlb.com/schedule/2018/07/19/"

#Render webpage with PhantonJS and selenium
#Phantom is the headless browser
#Selenium is the driver
driver = webdriver.PhantomJS()
driver.set_window_size(1024, 768) # optional
driver.get(Url)
time.sleep(1)

#pandas read_html to find attribute indicating table and loads a list of DataFrames one per html table on page
stats_list = pd.read_html(driver.page_source,attrs={'class': 'data schedule-list'} )
stats = stats_list[1]

#cleanup table to get desired info
cols = [1,2,3,4]
stats.drop(stats.columns[[cols]],inplace=True,axis=1)
#name columns something meaningful
stats.columns=['Teams']
#strips spaces
stats['Teams'] = stats['Teams'].str.replace(' ','')
#splits on @ sign and makes new rows per record
#building team list to filter player table for active players for the day
teams = stats['Teams'].str.split('@').apply(Series, 1).stack()
teams.index = teams.index.droplevel(-1) # to line up with df's index
teams.name = 'Teams' # needs a name to join

#retrieve list of players
#gather 1 player per position
#retrieve there previous day scores
#multiply by fanduel scoring

# engine = create_engine('postgresql://tyoung12290:Tjytjy90@mlb.ck81qylct4si.us-east-2.rds.amazonaws.com:5432/MLB')
#
# stats.to_sql("player_game_data",engine,if_exists='replace')
#print("table to database")
