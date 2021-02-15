"""
Created on Wed Aug 19 22:15:25 2020

@author: senay
"""


import pandas as pd
import requests 
import pprint

col=['id']

player_ids=pd.read_csv(r'C:\Users\senay\OneDrive\MSA\PythonScripts\nhl\playerids.csv',names=col,skiprows=1)

ids=player_ids.id.tolist()


df=pd.DataFrame()




for id in ids:
    #URL= 'https://statsapi.web.nhl.com/api/v1/people/8476381?expand=person.stats&stats=yearByYear'
    

    URL= 'https://statsapi.web.nhl.com/api/v1/people/'+str(id)+'?expand=person.stats&stats=yearByYear'
    response = requests.get( URL ) 
    data = response.json()
    print(data['people'][0]['fullName'])

    for split in data['people'][0]['stats'][0]['splits']:
            
            list=[]        
        # if len(data['people'][0]['stats'][0]['splits'][split]['stat'])<3:
        #     pass
        # elif data['people'][0]['stats'][0]['splits'][split]['stat']['games']>0:
            # list.append(data['people'][0]['fullName'])
            # list.append(data['people'][0]['stats'][0]['splits']['season'])
            # list.append(data['people'][0]['stats'][0]['splits'][split]['stat']['games'])
            # list.append(data['people'][0]['stats'][0]['splits'][split]['stat']['points'])  
            # list.append(data['people'][0]['stats'][0]['splits'][split]['stat']['goals'])
            # list.append(data['people'][0]['stats'][0]['splits'][split]['stat']['assists'])  
            
            try:
                list.append(data['people'][0]['fullName'])
                list.append(split['league']['name'])
                list.append(split['team']['name'])
                list.append(split['season'])
                list.append(split['stat']['games'])
                list.append(split['stat']['points'])  
                list.append(split['stat']['goals'])
                list.append(split['stat']['assists']) 
                col=pd.DataFrame(list)   #store mins and max into a dataframe
                col2=col.transpose() 
                df=df.append(col2)
            except:
                pass
    else:
        pass
        # pts=data['people'][0]['stats'][0]['splits'][1]['stat']['points']
        # goals=data['people'][0]['stats'][0]['splits'][1]['stat']['goals']
        # assists=data['people'][0]['stats'][0]['splits'][1]['stat']['assists']
print(df)
df=df.rename(columns={0:'name',1:'league',2:'team',3:'season',4:'games',5:'points',6:'goals',7:'assists'})    
print(df)
df.to_pickle('C:/Users/senay/OneDrive/MSA/PythonScripts/nhlpickle')
    # print(data)
    # name=data['people'][0]['fullName']
    # points=data['stats']
    
    # print(points)

df.to_csv(r'nhl.csv',index=False) #create csv in current working directory



