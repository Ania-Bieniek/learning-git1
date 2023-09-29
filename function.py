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

# ćwiczenie
def fun_default(positional_or_keyword_parameters):
     pass
fun_default(positional_or_keyword_parameters=1)

def fun_positonal(positional_only_parameters):
    pass
fun_positonal(positional_only_parameters=2)

def fun_keyword(keyword_only_parameters):
    pass
fun_keyword(keyword_only_parameters=3) 


#przykład: obliczamy ilość argumentów podanych do funkci z jedną *:
def count_them_all(*args):
    positional_args_count = len(args)
    print(f"I have received {positional_args_count} positional arguments")

count_them_all(1, 2, 3, 4, "A")

def count_them_all(*args, **kwargs):
    positional_args_count = len(args)
    print(f"I have received {positional_args_count} positional arguments")
    postional_kwars_count = len(kwargs)
    print(f"I have received {postional_kwars_count} keyword arguments")
count_them_all(1, 2, 3, "A", a=1, b=2)

#lista zakupów zadeklarowna jako lista krotek
schopping_items = [
    ("ziemniak", 2.5, 0.51),
    ("cebula", 3, 1.60),
    ("ser", 0.8, 15.50)
]    
#układanie elementów po cenie za kg 
def get_index_1_tuple_element(given_tuple):
    return given_tuple[1]

sorted_items = sorted(schopping_items, key=get_index_1_tuple_element)
print(sorted_items)
#lambda
sorted_items = sorted(schopping_items, key=lambda given_tuple: given_tuple[1])
print(sorted_items)



