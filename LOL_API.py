import requests
import sqlite3
import os
import time
from dotenv import load_dotenv
load_dotenv()

with sqlite3.connect('./LOL_API/database.db') as db:
    cursor = db.cursor()
    with open('./LOL_API/build.sql','r') as f:
        cursor.executescript(f.read())
        db.commit()
        print("executed script")
db = sqlite3.connect('./LOL_API/database.db')
cursor = db.cursor()
q = {
    440: "Flex 5v5",
    420: "Ranked Solo/Duo",
    430: "Normal",
    0: "Custom",
}
base = 'https://na1.api.riotgames.com'
base_m = 'https://americas.api.riotgames.com'
acc = '/lol/summoner/v4/summoners/by-name/'
m_id = '/lol/match/v5/matches/by-puuid/'
game = '/lol/match/v5/matches/'
headers = {
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10.15; rv:103.0) Gecko/20100101 Firefox/103.0",
    "Accept-Language": "en-US,en;q=0.5",
    "Accept-Charset": "application/x-www-form-urlencoded; charset=UTF-8",
    "Origin": "https://developer.riotgames.com",
    "X-Riot-Token": os.getenv("API")
}
r = requests.get(f'{base}{acc}{"TD Pandorum"}', headers = headers)
r = r.json()
ac_id = r['accountId']
puid = r['puuid']
z = requests.get(f'{base_m}{m_id}{puid}/ids?count=100', headers = headers)
z = z.json()
for _ in z:
    time.sleep(10)
    x = requests.get(f'{base_m}{game}{_}', headers = headers)
    x = x.json()
    #print(x['info']['gameMode'])
    #print(x['info']['gameType'])
    matchid = _ 
    print(q.get(x['info']['queueId']))
    for _ in x['info']['participants']:
        #print(x['summonerName'])
        if _['summonerName'] == 'TD Pandorum':
            #print(json.dumps(x,indent = 4))
            name = _['summonerName']
            champ = _['championName']
            deaths = _['deaths']
            kills = _['kills']
            assists = _['assists']
            dmg_champ = _['totalDamageDealtToChampions']
            win = _['win']
            pos = _['teamPosition']
    print(f'{kills}/{deaths}/{assists} - {champ} - {dmg_champ} - {"Win" if win else "Loss"} {pos}')
    for x in x['info']['participants']:
        if x['summonerName'] != 'TD Pandorum' and x['teamPosition'] == pos:
            cursor.execute("""INSERT INTO games VALUES (?,?,?,?,?,?,?,?,?)""",
            (name,champ,pos,x['teamPosition'],kills,deaths,assists,win,matchid))
            print(f'{x["kills"]}/{x["deaths"]}/{x["assists"]} - {x["championName"]} - {x["totalDamageDealtToChampions"]} - {x["teamPosition"]}')
            db.commit()
#print(json.dumps(x['info']['participants'][0],indent = 4))

