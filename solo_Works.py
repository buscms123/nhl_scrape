# -*- coding: utf-8 -*-
"""
Created on Tue Aug  4 18:43:55 2020

@author: senay
"""
import time
import requests
from bs4 import BeautifulSoup 
import re
import pandas as pd
pd.set_option('display.max_columns', None)
start_time = time.time()
dict={}
frame=pd.DataFrame()
year=2010
for year in range(2017,2020):
    year=str(year)
    print(year)
    source=requests.get('https://www.hockey-reference.com/leagues/NHL_'+year+'_skaters.html').text
    soup=BeautifulSoup(source,features='lxml')
             
    data_stats=["player","age","team_id","pos","games_played","goals","assists","points","plus_minus","pen_min","ps","goals_ev","goals_pp","goals_sh","goals_gw","assists_ev","assists_pp","assists_sh","shots","shot_pct","time_on_ice","time_on_ice_avg","blocks","hits","faceoff_wins","faceoff_losses","faceoff_percentage","year"]
    
    
    
    filter={"data-stat":"age"}
    data='age'
    table1=soup.find('table',id="stats")
    rows=table1.findAll('tr')
    
    k=2
    for k in range(2,20000):
        list=[]
        years=[]
        for data in data_stats:
                
                try:
                    cells=rows[k].findAll('td',attrs={'data-stat':data})
                    nameval=cells[0].string
                    
                  
                    list.append(nameval)
                    
                except: pass
        list.append(year)
        col=pd.DataFrame(list)
        col2=col.transpose()           
        frame=frame.append(col2)
        
   
    k=k+1           
        # df_new.loc[idx] = row.values.tolist() + [true_move, price_new]
    
        #     idx += 1
    
    year=int(year)
    year=year+1

frame.columns=(data_stats)
columns=["player","age","team_id","pos","games_played","goals","assists","points","plus_minus","pen_min","ps","goals_ev","goals_pp","goals_sh","goals_gw","assists_ev","assists_pp","assists_sh","shots","shot_pct","time_on_ice","time_on_ice_avg","blocks","hits","faceoff_wins","faceoff_losses","faceoff_percentage",'year']
# df=pd.DataFrame.from_dict(dict,orient='index',columns=columns)
cols=frame.columns.drop(['player','team_id','pos','year'])
frame[cols] = frame[cols].apply(pd.to_numeric, errors='coerce')
print(frame)

print(frame.dtypes)
frame.to_csv (r'C:\Users\senay\Documents\nhl6.csv',index = False, header=True)


print("--- %s seconds ---" % (time.time() - start_time))