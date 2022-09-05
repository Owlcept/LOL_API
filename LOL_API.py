import requests
import os
import json
from dotenv import load_dotenv
load_dotenv()
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
r = requests.get(f'{base}{acc}{"owlcept"}', headers = headers)
r = r.json()
ac_id = r['accountId']
puid = r['puuid']
z = requests.get(f'{base_m}{m_id}{puid}/ids', headers = headers)
z = z.json()
for _ in z:
    x = requests.get(f'{base_m}{game}{_}', headers = headers)
    x = x.json()
    for x in x['info']['participants']:
        #print(x['summonerName'])
        if x['summonerName'] == 'Owlcept':
            #print(json.dumps(x,indent = 4))
            champ = x['championName']
            deaths = x['deaths']
            kills = x['kills']
            assists = x['assists']
            dmg_champ = x['totalDamageDealtToChampions']
    print(f'{kills}/{deaths}/{assists} - {champ}')
#print(json.dumps(x['info']['participants'][0],indent = 4))

