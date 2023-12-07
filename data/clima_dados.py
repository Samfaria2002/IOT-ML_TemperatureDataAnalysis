import requests
import sys
from datetime import datetime
import matplotlib.pyplot as plt

response = requests.request("GET", "https://weather.visualcrossing.com/VisualCrossingWebServices/rest/services/timeline/Contagem?unitGroup=metric&key=8DKJ8N6LN6VZFT72DRL689RFB&contentType=json")

if response.status_code != 200:
    print('Unexpected Status code: ', response.status_code)
    sys.exit()  

tempoJson = response.json()
cidade = tempoJson['resolvedAddress']
dias = tempoJson['days']

datas_formatadas = []
temperaturas = []

for dia in dias:
    data = dia['datetime']
    data_formatada = datetime.strptime(data, '%Y-%m-%d').strftime('%d/%m/%Y')
    temperatura = dia['temp']
    
    datas_formatadas.append(data_formatada)
    temperaturas.append(temperatura)

plt.figure(figsize=(10, 6))
plt.plot(datas_formatadas, temperaturas, marker='o', linestyle='-')
plt.title(f'Temperaturas em {cidade}')
plt.xlabel('Data')
plt.ylabel('Temperatura (°C)')
plt.xticks(rotation=45)
plt.tight_layout()

plt.show()
