import pandas as pd

# Charger les données
data = pd.read_csv('data/historical_data.csv')

# Fonction de comparaison de plusieurs équipes
def compare_multiple_teams(*teams):
    comparison_data = {}
    for team in teams:
        matches = data[(data['HomeTeam'] == team) | (data['AwayTeam'] == team)]
        total_matches = len(matches)
        total_goals = matches['HomeGoals'].sum() + matches['AwayGoals'].sum()
        comparison_data[team] = {
            'Total Matches': total_matches,
            'Total Goals': total_goals
        }
    return comparison_data

# Exemple de comparaison de plusieurs équipes
comparison_result = compare_multiple_teams('PSG', 'Lyon', 'Marseille')
print(comparison_result)
