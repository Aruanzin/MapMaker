import pandas as pd
import json
import numpy as np
from Principal import principal

def validar_coordenadas(latitude, longitude):
    if -90 <= latitude <= 90 and -180 <= longitude <= 180:
        return False
    else:
        return True

def write_data(data):
    with open('_data.json', 'w') as f:
    # Write the dictionary as a JSON object to the file
        json.dump(data, f)
    f.close()

def read_data():
    with open('_data.json', 'r', encoding='utf-8') as f:
    # Load the data from the file
        data = json.load(f)
    if not data:
        print('not data')
        data = {
            'localizacoes': [],
            'titulos': [],
            'descricao': [],
            'filePath': '/home/johnatas/Documentos/workspace/python/MapMaker/data.xlsx',
            'map': 'https://www.google.com/maps/d/u/0/edit?mid=19Af8BUv6WDvFGncBjN45gxDzWUKGeKI&ll=-26.81010219809132%2C-50.838401644747634&z=5'
        }
        write_data(data)
    f.close()
    return data


info = read_data()
df = pd.read_excel(info['filePath'])

#firstLine = df.columns
#tSigla = firstLine[0]



Sigla = info['titulos']
dados = info['descricao']
localizacao = info['localizacoes']


listaSigla = []
listaConteudo = []
listaLoc = []

for index, row in df.iterrows():
    if row[dados].isnull().values.any() or row[Sigla].isnull().values.any() or row[localizacao].isnull().values.any() :
        raise Exception(f"Valor vazio na linha {index+2}")
    elif validar_coordenadas(row[localizacao][0], row[localizacao][1]):
        raise Exception(f"Coordenada inválida na linha {index+2}")
    else:
        sigla = " ".join(row[Sigla]) if len(row[Sigla]) > 1 else row[Sigla]
        locationArray = [str (item) for item in row[localizacao]]
        # conteudoArray = row[dados]
        loc =  " ".join(locationArray) if len(locationArray) > 1 else locationArray[0]
        conteudo =  " ".join(row[dados]) if len(row[dados]) > 1 else row[dados]

        # conteudoSemNull = list(filter(lambda x: not math.isnan(x), conteudo))

        listaSigla.append(sigla)
        listaConteudo.append(conteudo)
        listaLoc.append(loc)

principal(listaSigla, listaConteudo, listaLoc, info['map'])    
    # print("SIGLAS: ", listaSigla,"CONTEUDOS: ", listaConteudo, "LOCALIZACOES: ",listaLoc)        

# if __name__ == '__main__':
#     print('principal')
#     leArquivo()