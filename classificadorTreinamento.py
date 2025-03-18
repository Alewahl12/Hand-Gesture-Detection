#Treinar o modelo
import pickle
import numpy as np
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score

#Abrir arquivo pickle
dados_dict = pickle.load(open('./data.pickle', 'rb'))

#Converter os dados para um array numpy
data = np.asarray(dados_dict['data'])
labels = np.asarray(dados_dict['labels'])

#Data split | treinamento e teste

#Divide dados para treino e dados para teste | Divide labels para treino e labels para teste | Porcentagem de dados para teste | Misturar os dados | Pegar 1/3 de cada label
x_train, x_test, y_train, y_test = train_test_split(data, labels, test_size= 0.2, shuffle= True, stratify= labels)

#Modelo de treinamento
model = RandomForestClassifier()

#Treinamento do modelo com os dados x e y (data e labels)
model.fit(x_train, y_train)

#Testar eficacia do modelo para dados de teste
y_predict = model.predict(x_test)

#Obter a precisão do modelo em classificar novos dados
score = accuracy_score(y_predict, y_test)
print(f"{score*100}% das amostras foram classificadas corretamente!")

#Salvar modelo com pickle
f = open('model.pickle','wb')
pickle.dump({'model': model}, f)
f.close()