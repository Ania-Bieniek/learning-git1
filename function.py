schopping_items = [
    "jajka",
    "bułka",
    "ser",
    "masło",
    "pomidor",
    "chusteczki",
    "papier toaletowy"
]
def shopping(items):
    shopping_cart = "Koszyk zawiera:"
    for item in items:
        shopping_cart += item + '\n'
    return shopping_cart
bascet = shopping(schopping_items)
print(bascet)

