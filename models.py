from abc import ABC, abstractmethod


class ClothingItem(ABC):
    def __init__(self, product_id, product_code, product_name, color, size, price_eur, stock):
        self._product_id = product_id
        self._product_code = product_code
        self._product_name = product_name
        self._color = color
        self._size = size
        self._price_eur = price_eur
        self._stock = stock

    # Encapsulation : getters
    def get_product_id(self):
        return self._product_id

    def get_product_code(self):
        return self._product_code

    def get_product_name(self):
        return self._product_name

    def get_color(self):
        return self._color

    def get_size(self):
        return self._size

    def get_price_eur(self):
        return self._price_eur

    def get_stock(self):
        return self._stock

    # Encapsulation : setters
    def set_price_eur(self, new_price):
        if new_price > 0:
            self._price_eur = new_price

    def set_stock(self, new_stock):
        if new_stock >= 0:
            self._stock = new_stock

    # Méthode métier
    def decrease_stock(self, quantity):
        if quantity > 0 and quantity <= self._stock:
            self._stock -= quantity
            return True
        return False

    # Abstraction
    @abstractmethod
    def get_category(self):
        pass

    def to_dict(self):
        return {
            "product_id": self._product_id,
            "product_code": self._product_code,
            "product_name": self._product_name,
            "category": self.get_category(),
            "color": self._color,
            "size": self._size,
            "price_eur": self._price_eur,
            "stock": self._stock
        }


class TShirt(ClothingItem):
    def get_category(self):
        return "T-shirt"


class Hoodie(ClothingItem):
    def get_category(self):
        return "Sweat à capuche"


class Jogging(ClothingItem):
    def get_category(self):
        return "Jogging"


class Cap(ClothingItem):
    def get_category(self):
        return "Casquette"


def create_item_from_row(row):
    product_name = row["product_name"].lower()

    if "t-shirt" in product_name:
        return TShirt(
            row["product_id"],
            row["product_code"],
            row["product_name"],
            row["color"],
            row["size"],
            row["price_eur"],
            row["stock"]
        )

    elif "sweat" in product_name:
        return Hoodie(
            row["product_id"],
            row["product_code"],
            row["product_name"],
            row["color"],
            row["size"],
            row["price_eur"],
            row["stock"]
        )

    elif "jogging" in product_name:
        return Jogging(
            row["product_id"],
            row["product_code"],
            row["product_name"],
            row["color"],
            row["size"],
            row["price_eur"],
            row["stock"]
        )

    elif "casquette" in product_name:
        return Cap(
            row["product_id"],
            row["product_code"],
            row["product_name"],
            row["color"],
            row["size"],
            row["price_eur"],
            row["stock"]
        )

    return None

