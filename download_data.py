import requests
import csv
from datetime import datetime

API_KEY = 'bda4bb55c18044238ceb9a5694f97b9f'  # Clé API intégrée
BASE_URL = 'https://api.football-data.org/v2/competitions/FL1/matches'

headers = {
    'X-Auth-Token': API_KEY
}

response = requests.get(BASE_URL, headers=headers)

if response.status_code == 200:
    data = response.json()
    matches = data['matches']

    # Écrire les données dans un fichier CSV
    with open('data/historical_data.csv', mode='w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(['Date', 'HomeTeam', 'AwayTeam', 'HomeGoals', 'AwayGoals'])

        for match in matches:
            date = datetime.strptime(match['utcDate'], '%Y-%m-%dT%H:%M:%SZ').strftime('%Y-%m-%d')
            home_team = match['homeTeam']['name']
            away_team = match['awayTeam']['name']
            home_goals = match['score']['fullTime']['homeTeam']
            away_goals = match['score']['fullTime']['awayTeam']
            writer.writerow([date, home_team, away_team, home_goals, away_goals])

    print('Données écrites dans data/historical_data.csv')

    # Analyser les dates
    dates = [datetime.strptime(match['utcDate'], '%Y-%m-%dT%H:%M:%SZ').date() for match in matches]
    first_date = min(dates)
    last_date = max(dates)

    print(f"Première date de match disponible : {first_date}")
    print(f"Dernière date de match disponible : {last_date}")
else:
    print(f"Erreur lors de la récupération des données : {response.status_code}")
