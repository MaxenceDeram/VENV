import pandas as pd
import mysql.connector
from sklearn.linear_model import LinearRegression

# 1. Connexion à la base, requête SQL pour récupérer les données nécessaires
conn = mysql.connector.connect(
    host="mysql-maxderam.alwaysdata.net",
    user="maxderam_prune",
    password="Prune59.",
    database="maxderam_projectclothingv1"
)
query = """
SELECT height_cm, weight_kg, size_code
FROM clients
WHERE height_cm IS NOT NULL
  AND weight_kg IS NOT NULL
  AND size_code IS NOT NULL
"""

# 2. Charger dans un DataFrame
df = pd.read_sql(query, conn)
conn.close()

print("Nombre de lignes utilisées :", len(df))

# 2. Choisir les colonnes d'entrée (X) et la colonne à prédire (y))
X = df[["height_cm", "weight_kg", "bmi", "age"]]
y = df["size_code"]

# 3. Créer le modèle
model = LinearRegression()

# 4. Entraîner le modèle
model.fit(X, y)

# 5. Demander les informations du client
height = float(input("Quelle est votre taille en cm ? : "))
weight = float(input("Quel est votre poids en kg ? : "))

fit_preference = int(input(
"De 0 à 10, préférez-vous une coupe serrée (0) ou large (10) ? : "
))
print("Merci pour ces informations. " \
"Nous allons vous recommander la taille la plus adaptée à votre morphologie. " \
"Ces recommandations sont basées sur les données de nos clients et peuvent ne pas être parfaites, mais elles devraient vous donner une bonne indication de la taille à choisir." \
"Nous accordons une grande importance à la confidentialité de vos données. Toutes les informations que vous avez fournies sont utilisées uniquement pour générer une recommandation de taille personnalisée et ne seront pas partagées avec des tiers. " \
"Nous nous engageons à protéger votre vie privée et à utiliser vos données de manière responsable. Si vous avez des questions ou des préoccupations concernant la confidentialité de vos données, n'hésitez pas à nous contacter.")

# 6. Faire la prédiction
predicted_code = model.predict([[height, weight]])[0]

# 7. Arrondir la valeur
predicted_code = round(predicted_code)

# 8. Ajuster selon la préférence de coupe
if fit_preference >= 7:
    predicted_code += 1
elif fit_preference <= 3:
    predicted_code -= 1

# 9. Limiter entre 1 et 5
if predicted_code < 1:
    predicted_code = 1
elif predicted_code > 5:
    predicted_code = 5

# 10. Transformer le code en taille
sizes = {
    1: "XS",
    2: "S",
    3: "M",
    4: "L",
    5: "XL"
}

size = sizes[predicted_code]

# 11. Afficher le résultat
print("Recommended size:", size)

# matplotlib pour visualiser les données
import matplotlib.pyplot as plt
plt.scatter(df["height_cm"], df["weight_kg"], c=df["size_code"], cmap="viridis")
plt.colorbar(label="Size Code")
plt.xlabel("Height (cm)")
plt.ylabel("Weight (kg)")
plt.title("Clothing Size Distribution")
plt.show()