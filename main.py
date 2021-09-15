import requests
hero_list = ["Hulk", "Thanos", "Captain America"]
intel = {}
name_hero = {}
def request_(name):
  url = "https://superheroapi.com/api/2619421814940190/search/"
  response = requests.get(url+name, timeout = 5)
  hero = response.json()
  hero_int = hero['results'][0]['powerstats']['intelligence']
  intel[name] = hero_int
  name_hero[hero_int] = name
  return intel
for hero in hero_list:
  request_(hero)
max_int = max(intel.values(), key=lambda i: int(i))
smart_hero = name_hero[max_int]

print(smart_hero, max_int)
