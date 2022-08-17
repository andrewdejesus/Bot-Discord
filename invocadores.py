from http.client import ResponseNotReady
import requests
import json

INVOCADOR = []
def pegar_invoc_crip(invocador):
    respostas = requests.get("https://br1.api.riotgames.com/lol/summoner/v4/summoners/by-name/{}?api_key=RGAPI-423e0642-cd88-440b-a65b-45ef85b7309c".format(invocador))
    return respostas.text
    

def parsing(text):
    try:
        return json.loads(text)

    except Exception as e:
        print(e)


def pegar_id(invoc):
    resultados = parsing(pegar_invoc_crip(invoc))

    resultado = resultados['id']
    return resultado
    
def pegar_invoc(invoc):

    resposta = requests.get("https://br1.api.riotgames.com/lol/league/v4/entries/by-summoner/{}?api_key=RGAPI-423e0642-cd88-440b-a65b-45ef85b7309c".format(pegar_id(invoc)))
    return resposta.text


#inicio das funções de fato

def pegar_tier_flex(invocador):

    ranks = parsing(pegar_invoc(invocador))

    return "{}:{}\n{} PDL\nwins: {}\nlosses: {}".format(ranks[0]['tier'], ranks[0]['rank'], ranks[0]['leaguePoints'], ranks[0]['wins'], ranks[0]['losses'])
    


def pegar_tier_solo(invocador):

    ranks = parsing(pegar_invoc(invocador))
    
    return "{}:{}\n{} PDL\nwins: {}\nlosses: {}".format(ranks[1]['tier'], ranks[1]['rank'], ranks[1]['leaguePoints'], ranks[1]['wins'], ranks[1]['losses'])





    




    
        
   

    

