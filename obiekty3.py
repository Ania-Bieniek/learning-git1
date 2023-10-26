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

#for _ in range(5):
#   c = BaseConact(first_name=fake.first_name(), last_name=fake.last_name(), phone_number=fake.phone_number(), email=fake.email())
#   cards.append(c)

#card = BaseConact(first_name="Zosia", last_name="Bldes", phone_number=56787073, email="zosia@wp.pl")

#for c in cards:
#   print(c)
#   c.contact()
 
  


