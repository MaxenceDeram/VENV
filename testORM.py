from ORM import ORM

orm = ORM(
    host="mysql-maxderam.alwaysdata.net",
    user="maxderam_prune",
    password="Prune59.",
    database="maxderam_projectclothingv1"
)

# Tout afficher
print(orm.select_all("catalog"))

# Afficher un élément par id
print(orm.select_by_id("catalog", "product_id", 1))

# Insérer un nouvel élément
new_product = {
    "product_name": "T-shirt test",
    "category": "T-shirts",
    "color": "Rose",
    "size" : "S",
    "price_eur":"29.99",
    "stock": 100
}
print(orm.insert("catalog", new_product))    

# Supprimer un élément
print(orm.delete("catalog", "product_id", 0))
    