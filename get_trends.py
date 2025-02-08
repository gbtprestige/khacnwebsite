from pytrends.request import TrendReq
import json

# Configurer PyTrends
pytrends = TrendReq(hl='fr-FR')

# Pays à surveiller
countries = ['france', 'united_states', 'canada', 'singapore']

# Liste des mots-clés à surveiller, y compris les tendances actuelles
crypto_keywords = ['buy crypto', 'sell crypto', 'crypto trends', 'cryptocurrency']

# Dictionnaire pour stocker tous les mots-clés
all_trending_keywords = {}

# Extraire les tendances pour chaque pays
for country in countries:
    trending_searches = pytrends.trending_searches(pn=country)
    trending_keywords = trending_searches[0].tolist()
    
    # Ajouter les mots-clés de cryptomonnaie et les tendances du jour
    trending_keywords += crypto_keywords
    all_trending_keywords[country] = trending_keywords

# Enregistrer tous les mots-clés dans un fichier JSON
with open('trending_keywords.json', 'w', encoding='utf-8') as f:
    json.dump(all_trending_keywords, f, ensure_ascii=False, indent=4)

print("Mots-clés tendances pour tous les pays sauvegardés avec succès.")
