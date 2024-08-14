import requests
import numpy as np
import json

url = 'http://localhost:5000/predict'

image = np.zeros((28, 28), dtype=np.float32)  # Exemplo de imagem

image = np.expand_dims(image, axis=-1)  # (28, 28, 1)
image = np.expand_dims(image, axis=0)   # (1, 28, 28, 1)

image_list = image.tolist()

data = {
    "data": image_list
}

response = requests.post(url, json=data)

if response.status_code == 200:
    print("Resposta do servidor:", response.json())
else:
    print("Erro:", response.status_code, response.text)