import pandas as pd

# Charger les données
data = pd.read_csv('data/historical_data.csv')

# Fonction de recherche par équipe
def search_team(team_name):
    # Rechercher des matchs impliquant l'équipe spécifiée
    matches = data[(data['HomeTeam'] == team_name) | (data['AwayTeam'] == team_name)]
    return matches

# Fonction de recherche par année
def search_by_year(year):
    # Filtrer les matchs par l'année spécifiée
    matches = data[pd.to_datetime(data['Date']).dt.year == year]
    return matches

# Exemple de recherche par équipe
print(search_team('PSG'))

# Exemple de recherche par année
print(search_by_year(2023))
