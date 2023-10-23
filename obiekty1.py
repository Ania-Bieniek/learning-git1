from faker import Faker
fake = Faker()
from faker.generator import random
fake.random
fake.random.getstate()

class Card:
   def __init__(self, contact, name, company, city, phone_number, mail):
       self.contact = contact
       self.name = name
       self.city = city
       self.company = company
       self.phone_number = phone_number
       self.mail = mail

for method in dir(Faker()):
    print(method)

for _ in range(5):
    print(fake.name(), fake.company(), fake.city(), fake.phone_number(), fake.mail(),sep=" /")
    
