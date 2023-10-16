for year in range(2020, 2024):
    for month in range(1, 13):
        print("Rok "  + str( year))
        print("Miesiąc " + str( month))
        break

for i in range(0, 6):
    print("*" * (i + 1))

for i in range(2, 10, 2):
    print("*" * (i))
    print("*" * (i))
# lub tak:
for i in range(1, 8, 2):
    print("*" * (i + 1))
    print("*" * (i + 1))

print("-----------------")

for i in range(1, 10, 2):
    print("*" * 10)
    print(" **********")

for i in range(5, -1, -1):
    print("*" * (i + 1))


for i in range(1, 10):
    print(i)
    if i > 3:
        continue
    print("widzę mniej niż 3")

for i in range(0, 8):
    print(i)




        












        
