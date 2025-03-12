# Football Prediction Models

Ce dépôt contient des modèles prédictifs, des outils de recherche et de comparaison pour les championnats de football européens. Les modèles sont basés sur des données historiques et utilisent des techniques avancées d'apprentissage automatique pour faire des prédictions et des analyses.

## Structure du Dépôt

```
football-prediction-models/
├── data/
│   └── historical_data.csv
├── models/
│   ├── predictive_model.py
│   ├── search_model.py
│   └── comparison_model.py
├── download_data.py
├── README.md
```

## Contenu des Fichiers

### `data/historical_data.csv`
Ce fichier CSV contient les données historiques des matchs. Utilisez le script `download_data.py` pour le générer.

### `models/predictive_model.py`
Ce fichier contient le modèle prédictif basé sur LSTM pour prédire les scores des matchs.

### `models/search_model.py`
Ce fichier contient une fonction de recherche pour trouver des matchs impliquant une équipe spécifique, ainsi qu'une fonction pour rechercher des matchs par année.

### `models/comparison_model.py`
Ce fichier contient une fonction de comparaison pour comparer les statistiques de plusieurs équipes.

### `download_data.py`
Ce script télécharge les données des matchs de Ligue 1 depuis l'API Football-Data.org et les enregistre dans un fichier CSV.

## Utilisation

### 1. Prédiction des Scores

Pour prédire le score d'un match spécifique, utilisez la fonction `predict_score` dans `predictive_model.py`.

```python
# Exemple de prédiction
print(predict_score('PSG', 'Lyon'))
```

### 2. Recherche de Matchs

Pour rechercher des matchs impliquant une équipe spécifique, utilisez la fonction `search_team` dans `search_model.py`.

```python
# Exemple de recherche par équipe
print(search_team('PSG'))
```

Pour rechercher des matchs par année, utilisez la fonction `search_by_year` dans `search_model.py`.

```python
# Exemple de recherche par année
print(search_by_year(2023))
```

### 3. Comparaison de Plusieurs Équipes

Pour comparer les statistiques de plusieurs équipes, utilisez la fonction `compare_multiple_teams` dans `comparison_model.py`.

```python
# Exemple de comparaison de plusieurs équipes
comparison_result = compare_multiple_teams('PSG', 'Lyon', 'Marseille')
print(comparison_result)
```

### 4. Téléchargement des Données Historiques

Pour télécharger les données historiques des matchs de Ligue 1 et les enregistrer dans un fichier CSV, exécutez le script `download_data.py`.

1. **Créer le Répertoire `data`** : Assurez-vous que le répertoire `data` existe dans votre dépôt. Si ce n'est pas le cas, créez-le.
   ```bash
   mkdir data
   ```

2. **Exécuter le Script** : Exécutez le script Python pour télécharger les données et les enregistrer dans le fichier CSV.
   ```bash
   python download_data.py
   ```

## Contribuer

Les contributions sont les bienvenues ! N'hésitez pas à ouvrir des issues ou des pull requests pour proposer des améliorations ou des ajouts.

## Licence

Ce projet est sous licence MIT.
