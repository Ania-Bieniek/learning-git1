shopping_dict = {}
shopping_dict["piekarnia"] = ["bułka", "pączek"]
shopping_dict["warzywniak"] = ["jabłbko", "marchew"]

raport = ""
for shop in shopping_dict:
    raport += f"Idę do {shop.capitalize()} kupuję tam: {str(shopping_dict[shop]).title()}\n"
print(raport)


shopping_dict = {}
shopping_dict["piekarnia"] = ["bułka", "pączek"]
shopping_dict["warzywniak"] = ["jabłbko", "marchew"]
for shop in shopping_dict:
    print(f"Idę do {shop.capitalize()} kupuję tam: {str(shopping_dict[shop]).title()}")

    
