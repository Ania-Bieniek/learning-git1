def shopping(items, payment='card', shop='lokal'):
    result = ""
    result = result + "Idę na zakupy do %s.\n" % shop
    result = result + "Kupuję następujące rzeczy:\n"
    for item in items:
        result = result + " - %s\n" % item
    result = result + "By zapłacić, użwyam %s." % payment
    return result
items = ["cola", "whiskey", "lód"]
text = shopping(items, 'card', 'small local shop')
print(text)

print("Pokażę co wpiszesz!")
tekst = input("2 czekolady")

print("Proszę kup:  ***%s***" % tekst)

















