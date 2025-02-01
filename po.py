import json
import requests

sr_str_pc_list = []
sr_str_mob_list = []
# for j in range(8):
#     res = requests.get('http://api.quotable.io/quotes/random?minLength=35', verify=False)
#     resp = res.json()
#     sr_str_pc = resp[0]['content']
#     sr_str_pc_list.append(sr_str_pc)
# print(sr_str_pc_list)
      

# for k in range(8):
#     res = requests.get('http://api.quotable.io/quotes/random?minLength=25', verify=False)
#     resp = res.json()
#     sr_str_mob = resp[0]['content']
#     sr_str_mob_list.append(sr_str_mob)
# print(sr_str_mob_list)

for j in range(8):
    res = requests.get('https://catfact.ninja/fact?minLength=50')
    resp = res.json()
    sr_str_pc = resp['fact']
    sr_str_pc_text = sr_str_pc[0:50]
    sr_str_pc_list.append(sr_str_pc_text)
print(sr_str_pc_list)
      

for k in range(8):
    res = requests.get('https://catfact.ninja/fact?minLength=40')
    resp = res.json()
    sr_str_mob = resp['fact']
    sr_str_mob_text = sr_str_mob[0:40]
    sr_str_mob_list.append(sr_str_mob_text)
print(sr_str_mob_list)

with open('list_pc.json', 'w') as file:
    json.dump(sr_str_pc_list, file)
with open('list_mob.json', 'w') as file:
    json.dump(sr_str_mob_list, file)