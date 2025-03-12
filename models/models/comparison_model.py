import pandas as pd

# Charger les données
data = pd.read_csv('data/historical_data.csv')

# Fonction de comparaison pour plusieurs équipes
def compare_multiple_teams(*teams):
    team_stats = {}
    
    for team in teams:
        team_home = data[data['HomeTeam'] == team]
        team_away = data[data['AwayTeam'] == team]
        stats = {
            'matches_played': len(team_home) + len(team_away),
            'wins': len(team_home[team_home['HomeGoals'] > team_home['AwayGoals']]) +
                    len(team_away[team_away['AwayGoals'] > team_away['HomeGoals']]),
            'draws': len(team_home[team_home['HomeGoals'] == team_home['AwayGoals']]) +
                     len(team_away[team_away['AwayGoals'] == team_away['HomeGoals']]),
            'losses': len(team_home[team_home['HomeGoals'] < team_home['AwayGoals']]) +
                      len(team_away[team_away['AwayGoals'] < team_away['HomeGoals']]),
            'goals_scored': team_home['HomeGoals'].sum() + team_away['AwayGoals'].sum(),
            'goals_conceded': team_home['AwayGoals'].sum() + team_away['HomeGoals'].sum()
        }
        team_stats[team] = stats
    
    # Confrontations directes entre toutes les équipes
    head_to_head = data[data['HomeTeam'].isin(teams) & data['AwayTeam'].isin(teams)]
    
    comparison = {
        'team_stats': team_stats,
        'head_to_head': head_to_head
    }
    
    return comparison

# Exemple de comparaison de plusieurs équipes
comparison_result = compare_multiple_teams('PSG', 'Lyon', 'Marseille')
print(comparison_result)
