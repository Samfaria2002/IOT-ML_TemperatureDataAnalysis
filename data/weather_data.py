import matplotlib.pyplot as plt
import numpy as np
from datetime import datetime
import requests
import sys

response = requests.request("GET", "https://weather.visualcrossing.com/VisualCrossingWebServices/rest/services/timeline/Contagem?unitGroup=metric&key=8DKJ8N6LN6VZFT72DRL689RFB&contentType=json")

if response.status_code != 200:
    print('Unexpected status code: ' + response.status_code)
    sys.exit()

tempo = response.json()
cidade = tempo['resolvedAddress']
dias = tempo['days']

dia_plot = []
tempo_plot = []

for dia in dias:
    data = dia['datetime']
    temperatura = dia['temp']
    data_format = datetime.strptime(data, '%Y-%m-%d').strftime('%d/%m/%Y')
    dia_plot.append(data_format)
    tempo_plot.append(temperatura)

plt.figure(figsize=(12, 6))
plt.plot(dia_plot, tempo_plot, marker='o', linestyle=':')
plt.title(f'Tempo em {cidade}')
plt.xlabel('Data')
plt.ylabel('Temperatura')
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()