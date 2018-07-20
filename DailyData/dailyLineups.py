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
mlb_url = "http://m.mlb.com/schedule/2018/07/17/"
espn_url = "http://www.espn.com/mlb/schedule/_/date/20180719"

#Render webpage with PhantonJS and selenium
#Phantom is the headless browser
#Selenium is the driver
driver = webdriver.PhantomJS()
driver.set_window_size(1024, 768) # optional
# driver.get(mlb_url)
# time.sleep(1)
#
# #pandas read_html to find attribute indicating table and loads a list of DataFrames one per html table on page
# mlb_games_list = pd.read_html(driver.page_source,attrs={'class': 'data schedule-list'} )
# mlb_games = mlb_games_list[1]
# print ('mlb')
# print (mlb_games)
driver.get(espn_url)
time.sleep(1)
espn_games_list = pd.read_html(driver.page_source,attrs={'class': 'schedule has-team-logos align-left'} )
espn_games=espn_games_list[1]
print ('espn')

espn_games=espn_games.loc[:,'matchup':'Unnamed: 1']
espn_games.columns=['away','home']
espn_games['away']=espn_games['away'].str.split(' ')[-1]

print(type(espn_games['away']))
#cleanup table to get desired info
# cols = [1,2,3,4]
# mlb_games.drop(mlb_games.columns[[cols]],inplace=True,axis=1)
# #name columns something meaningful
# mlb_games.columns=['Teams']
# #strips spaces
# mlb_games['Teams'] = mlb_games['Teams'].str.replace(' ','')
# #splits on @ sign and makes new rows per record
# #building team list to filter player table for active players for the day
# mlb_teams = mlb_games['Teams'].str.split('@').apply(Series, 1).stack()
# mlb_teams.name = 'Teams' # needs a name to join
# print (teams)



#retrieve list of players
#gather 1 player per position
#retrieve there previous day scores
#multiply by fanduel scoring

engine = create_engine('postgresql://tyoung12290:Tjytjy90@mlb.ck81qylct4si.us-east-2.rds.amazonaws.com:5432/MLB')

player_table = pd.read_sql_query('select * from "player_data"',con=engine)

print (player_table)
# meta = MetaData(db)
# player_table = Table('films', meta,
#                        Column('title', String),
#                        Column('director', String),
#                        Column('year', String))
#
# with db.connect() as conn:
#     select_statement = film_table.select()
#     result_set = conn.execute(select_statement)
#     for r in result_set:
#         print(r)
# stats.to_sql("player_game_data",engine,if_exists='replace')
#print("table to database")
