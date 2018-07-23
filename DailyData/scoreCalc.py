import pandas as pd
from pandas.io.html import read_html
from pandas import DataFrame, Series
from bs4 import BeautifulSoup
import platform
from sqlalchemy import create_engine
#import psycopg2
from selenium import webdriver
import time
import psycopg2 as pg
import pandas.io.sql as psql


engine = create_engine('postgresql://tyoung12290:Tjytjy90@mlb.ck81qylct4si.us-east-2.rds.amazonaws.com:5432/MLB')

player_table = pd.read_sql_query('select * from player_game_data',con=engine)
scores_table = pd.read_sql('select * from fanduel.scoring', con=engine)
#selecting one at each position for now to calculate 1 scores
# next step would be to calculate scores for each permutation
catcher_first = player_table.loc[player_table['Pos'].isin(['C','1B'])]
catcher_first = catcher_first.iloc[[0]]
print (catcher_first.columns)

second_base = player_table.loc[player_table['Pos']=='2B']
second_base = second_base.iloc[[0]]

third_base = player_table.loc[player_table['Pos']=='3B']
third_base = third_base.iloc[[0]]

shortstop = player_table.loc[player_table['Pos']=='SS']
shortstop = shortstop.iloc[[0]]

#first scraped data is position specific but will need to be generic for any outfielder
leftField = player_table.loc[player_table['Pos']=='LF']
leftField = leftField.iloc[[0]]

centerField = player_table.loc[player_table['Pos']=='CF']
centerField = centerField.iloc[[0]]

rightField = player_table.loc[player_table['Pos']=='RF']
rightField = rightField.iloc[[0]]

#pitcher to be handled different
#pitcher = player_table.loc[player_table['Pos']=='2B']
#pitcher = pitcher.iloc[[0]]

# join results into new dataFrame
positions = [catcher_first,second_base,third_base, shortstop, leftField,centerField,rightField]
lineup_table = pd.concat(positions)
print (lineup_table)
print (second_base)
print (player_table)
print (scores_table)
