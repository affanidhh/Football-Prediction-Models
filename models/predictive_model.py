import numpy as np
import pandas as pd
from keras.models import Sequential
from keras.layers import LSTM, Dense

# Charger les données
data = pd.read_csv('data/historical_data.csv')

# Prétraitement des données
def preprocess_data(data):
    # Convertir les dates en format datetime
    data['Date'] = pd.to_datetime(data['Date'])
    # Sélectionner les colonnes nécessaires
    data = data[['HomeTeam', 'AwayTeam', 'HomeGoals', 'AwayGoals']]
    # Encoder les équipes
    teams = pd.concat([data['HomeTeam'], data['AwayTeam']]).unique()
    team_encoder = {team: idx for idx, team in enumerate(teams)}
    data['HomeTeam'] = data['HomeTeam'].map(team_encoder)
    data['AwayTeam'] = data['AwayTeam'].map(team_encoder)
    return data, team_encoder

data, team_encoder = preprocess_data(data)

# Diviser les données en ensembles d'entraînement et de test
train_size = int(len(data) * 0.8)
train_data = data[:train_size]
test_data = data[train_size:]

# Préparer les ensembles d'entrée et de sortie
X_train = train_data[['HomeTeam', 'AwayTeam']].values
y_train_home = train_data['HomeGoals'].values
y_train_away = train_data['AwayGoals'].values

X_test = test_data[['HomeTeam', 'AwayTeam']].values
y_test_home = test_data['HomeGoals'].values
y_test_away = test_data['AwayGoals'].values

# Redimensionner les ensembles pour LSTM
X_train = X_train.reshape((X_train.shape[0], 1, X_train.shape[1]))
X_test = X_test.reshape((X_test.shape[0], 1, X_test.shape[1]))

# Construire le modèle LSTM
model = Sequential()
model.add(LSTM(50, input_shape=(X_train.shape[1], X_train.shape[2])))
model.add(Dense(1))
model.compile(optimizer='adam', loss='mean_squared_error')

# Entraîner le modèle
model.fit(X_train, y_train_home, epochs=50, batch_size=32, validation_data=(X_test, y_test_home), verbose=2, shuffle=False)

# Fonction de prédiction
def predict_score(home_team, away_team):
    home_team_encoded = team_encoder.get(home_team, None)
    away_team_encoded = team_encoder.get(away_team, None)
    if home_team_encoded is None or away_team_encoded is None:
        return "Équipe inconnue"
    input_data = np.array([[home_team_encoded, away_team_encoded]])
    input_data = input_data.reshape((input_data.shape[0], 1, input_data.shape[1]))
    home_goal_pred = model.predict(input_data)
    return int(home_goal_pred[0][0])

# Exemple de prédiction
print(predict_score('PSG', 'Lyon'))
