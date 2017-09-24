from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from pandas.io.html import read_html
from pandas import DataFrame
from bs4 import BeautifulSoup
import platform
import time
from HTMLTableParser import HTMLTableParser
from sqlalchemy import create_engine

if platform.system() == 'Windows':
    PHANTOMJS_PATH = './phantomjs.exe'
else:
    PHANTOMJS_PATH = './phantomjs'

username = 'tyoung12290@gmail.com'
passord = 'Tjytjy90'
#    "cc_session_id": "<TOKEN>"

stats = DataFrame()

Url = "https://www.baseball-reference.com/leagues/MLB/2017-standard-batting.shtml"

driver = webdriver.PhantomJS(PHANTOMJS_PATH)
driver.set_window_size(1024, 768) # optional
driver.get(Url)
time.sleep(1)
stats_list = pandas.read_html(driver.page_source,attrs={'id': 'players_standard_batting'} )
print("html to table")
stats = stats_list[0]
stats.drop(stats.columns[[0,29]],inplace=True,axis=1)
stats.columns=['player','age','team','LG','G','PA','AB','R','H','2B','3B',
				'HR','RBI','SB','CS','BB','SO','BA','OBP','SLG',
				'OPS','OPS+','TB','GDP','HBP','SH','SF','IBB']
engine= create_engine('postgresql://postgres:postgres123@localhost:5432/espn_data')

stats.to_sql("player_data",engine,if_exists='replace')
print("table to database")
#soup = BeautifulSoup(driver.page_source,"html.parser")
#hp = HTMLTableParser()
#table = hp.parse_url(soup)[1][1]
#table.head()
#games = soup.find_all('meta')

#table = driver.find_element_by_xpath('//*[@id = "players_standard_batting"]')
#table_html = table.get_attribute('innerHTML')
#stats = read_html(table_html)[0]

#table = driver.find_elements_by_xpath('//*[@id = "players_standard_batting"]')
#for row in table.find_elements_by_xpath(".//tr"):
#	cell = row.find_elements_by_tag_name("td")[1]
#print(cell.text)

#driver.find_element_by_xpath('.//*[@name="email"]').send_keys('tyoung12290@gmail.com')
#driver.find_element_by_xpath('.//*[@name="password"]').send_keys('Tjytjy90')
#driver.find_element_by_xpath('.//*[@name="login"]').click()
#driver.get("https://www.fanduel.com/games")
#item=driver.find_element_by_class_name('sport-toggle-menu__item')
#print(item.text,item.tag_name)
