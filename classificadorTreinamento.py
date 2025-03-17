#Treinar o modelo
import pickle
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score

dados_dic = pickle.load(open('./data.pickle', 'rb'))

print(dados_dic.keys())
print(dados_dic)
