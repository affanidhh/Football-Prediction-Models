import numpy as np
import pandas as pd
from keras.models import Sequential
from keras.layers import Dense, LSTM
from sklearn.preprocessing import StandardScaler

# Charger les données
data = pd.read_csv('data/historical_data.csv')

# Préparer les données
scaler = StandardScaler()
data_scaled = scaler.fit_transform(data[['HomeGoals', 'AwayGoals', 'HomeTeam', 'AwayTeam']])

# Diviser les données en ensembles de formation et de test
train_size = int(len(data_scaled) * 0.8)
train, test = data_scaled[:train_size], data_scaled[train_size:]

# Reshape les données pour LSTM
X_train = train[:, :-1]
y_train = train[:, -1]
X_test = test[:, :-1]
y_test = test[:, -1]

X_train = np.reshape(X_train, (X_train.shape[0], 1, X_train.shape[1]))
X_test = np.reshape(X_test, (X_test.shape[0], 1, X_test.shape[1]))

# Construire le modèle LSTM
model = Sequential()
model.add(LSTM(units=50, return_sequences=True, input_shape=(1, X_train.shape[2])))
model.add(LSTM(units=50))
model.add(Dense(1))

model.compile(loss='mean_squared_error', optimizer='adam')
model.fit(X_train, y_train, epochs=100, batch_size=1, verbose=2)

# Faire des prédictions
train_predict = model.predict(X_train)
test_predict = model.predict(X_test)

# Inverser la normalisation pour interpréter les résultats
train_predict = scaler.inverse_transform(train_predict)
test_predict = scaler.inverse_transform(test_predict)

# Fonction pour prédire le score d'un match spécifique
def predict_score(home_team, away_team):
    home_encoded = [0] * len(pd.get_dummies(data['HomeTeam']).columns)
    away_encoded = [0] * len(pd.get_dummies(data['AwayTeam']).columns)
    
    home_encoded[data['HomeTeam'].unique().tolist().index(home_team)] = 1
    away_encoded[data['AwayTeam'].unique().tolist().index(away_team)] = 1
    
    match_data = np.array(home_encoded + away_encoded).reshape(1, 1, -1)
    home_goals = model.predict(match_data).flatten()[0]
    away_goals = model.predict(match_data).flatten()[1]
    
    return (home_goals, away_goals)

# Exemple de prédiction
print(predict_score('PSG', 'Lyon'))
