import tensorflow as tf
from tensorflow import keras
import numpy as np
from data.weather_data import *
import random

tempo_data = []
for i in tempo_plot:
    tempo_data.append(i)
print(tempo_data)
'''
tempo_format = np.array(float[temp] for temp in tempo_data)
model = keras.models.Sequential([
    keras.layers.Input(1,),
    keras.layers.Dense(8, activation='relu'),
    keras.layers.Dense(1)
])

model.compile(optimizer='adam', loss='binary_crossentropy', metrics=['accuracy'])

treino = model.fit(tempo_format, epochs= 5)

amostras = 10
tempo_valida = np.random.randint(19, 24, amostras)
model.evaluate(tempo_valida, verbose=2)
'''

def prepare_sequence_data(seq, steps):
    X, y = [], []
    for i in range(len(seq)):
        end_ix = i + steps
        if end_ix > len(seq) - 1:
            break
        seq_x, seq_y = seq[i:end_ix], seq[end_ix]
        X.append(seq_x)
        y.append(seq_y)
    return np.array(X), np.array(y)

steps = 3
tempo_seq, saida_seq = prepare_sequence_data(tempo_data, steps)

tempo_seq = tempo_seq.reshape((tempo_seq.shape[0], tempo_seq.shape[1], 1))

model = keras.models.Sequential([
    keras.layers.LSTM(50, activation='relu', input_shape=(steps, 1)),
    keras.layers.Dense(1)
])

model.compile(optimizer='adam', loss='mse')

treino = model.fit(tempo_seq, saida_seq, epochs=50)

dados_predicao = np.array(tempo_data[-steps:])
for _ in range(10):
    entrada_predicao = dados_predicao[-steps:]
    entrada_predicao = entrada_predicao.reshape((1, steps, 1))
    predicao = model.predict(entrada_predicao, verbose=0)
    dados_predicao = np.append(dados_predicao, predicao)

print("Previsão para os próximos 10 valores:", dados_predicao[-10:])

