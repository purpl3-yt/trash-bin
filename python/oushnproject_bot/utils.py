import requests
from time import sleep as wait
url = 'https://oushnproject.com/app/modules/module_block_main_servers_monitoring/includes/js_controller.php'
def ugetdata(server, raw=False):
    response = requests.post(url,
    {
        "data[0][0][ip]": "91.200.42.8:27017",
        "data[0][0][fakeip]": "91.200.42.8:27017",
        "data[0][1][ip]": "91.211.118.109:27015",
        "data[0][1][fakeip]": "91.211.118.109:27015",
        "data[0][2][ip]": "91.211.118.113:27015",
        "data[0][2][fakeip]": "91.211.118.113:27015",
        "my": "yes"
    }
    )
    print(response.json())
    data = []
    for i in response.json()[server]['players']:
        data.append(i['Name'])
    if raw==False:
        return ['Игроки на сервере: '+'```'+', '.join(data)+'```','Название сервера: '+'```'+response.json()[server]['HostName']+'```','Айпи: '+response.json()[server]['ip'],'Карта: '+response.json()[server]['Map']]
    elif raw==True:
        return response.json()[server]

def getplayers(server: int):
    json_data = ugetdata(server,True)#data
    players_info = {}
    players_server_convert = {}
    players_names = []

    for i in json_data['players']:#for every player
        if not i['Name'] in ['oushnproject','oushnproject.com']:#remove bots from array
            players_info[i['Name']] = f'Имя: {i["Name"]}\nФрагов: {i["Frags"]}\nВремя игры: {i["TimeF"]}\nСервер: {json_data["HostName"]}'
    for i in json_data['players']:#array with players names
        players_names.append(i['Name'])
        players_server_convert[i['Name']] = json_data['HostName']
    return [players_info,players_names,players_server_convert]#return 2 objects