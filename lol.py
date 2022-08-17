from platform import architecture
import re
import requests
import json
from pyparsing import Regex
from threading import *

URL = "https://ddragon.leagueoflegends.com/cdn/12.14.1/data/pt_BR/champion.json"
URLCHAMP = "http://ddragon.leagueoflegends.com/cdn/12.14.1/data/pt_BR/champion/"

SKINS = []
ROUPAS = []



def busca(site):
    try:
        resposta = requests.get(site)
        return resposta.text
        

    except Exception as e:
        print(e)

def parsing(texto):
    try:
        return json.loads(texto)

    except Exception as e:
        print(e)



def buscar_champs(champs):
    
    try:
        resultado = parsing(busca(URLCHAMP + champs +".json"))
    except:
        print("Campeão não existe")
    if resultado:
        bonecos = resultado['data']['{}'.format(champs)]['skins']

        SKINS.append(bonecos)
        del(bonecos[0])


        for boneco in bonecos:

            s = boneco['name']
            
            ROUPAS.append(s)
            
        return ROUPAS

      



ROUPAS.clear()






        
                
           
            

            

    



    
        
        
        


         








    
    
    


    


        
