from faker import Faker
fake = Faker('pl_PL')
from faker.generator import random
fake.random
fake.random.getstate()


class Card:
   def __init__(self, contact, name, company, city, phone_number):
       self.contact = contact
       self.name = name
       self.city = city
       self.company = company
       self.phone_number = phone_number
       
for _ in range(5):
   print(fake.name(), fake.company(), fake.city(), fake.phone_number(),sep=" /")

list_card = Card(contact="Kontaktuje się z:", name="Zosia Samosia", phone_number=56787073, company="Matr&", city="Los A")

def __str__(self):
   return f'{self.name} {self.phone_number}'
print(list_card)









