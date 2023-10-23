from faker import Faker
fake = Faker('pl_PL')
from faker.generator import random
fake.random
fake.random.getstate()

class Card:
   def __init__(self, simple_profile):
      self.simple_profile = simple_profile

for _ in range(5):
    print(fake.simple_profile())

       
  


