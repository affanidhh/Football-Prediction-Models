import pandas as pd

# Charger les données
data = pd.read_csv('data/historical_data.csv')

# Fonction de recherche
def search_team(team_name):
    # Rechercher des matchs impliquant l'équipe spécifiée
    matches = data[(data['HomeTeam'] == team_name) | (data['AwayTeam'] == team_name)]
    return matches

# Exemple de recherche
print(search_team('PSG'))
