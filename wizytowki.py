from faker import Faker
fake = Faker('pl_PL')
from faker.generator import random
fake.random
fake.random.getstate()


class BaseContact:
   def __init__(self, first_name, last_name, phone_number, email):
       self.first_name = first_name
       self.last_name = last_name
       self.phone_number = phone_number
       self.email = email
       

   @property
   def label_lenght(self):
       return len(self.last_name  + " " + self.first_name)

   def __str__(self):
      return f'{self.first_name} {self.last_name} {self.phone_number}'
   
   def contact(self):
      print(f"Kontaktuje się z {self.first_name} {self.last_name} i dzwonię pod nr: {self.phone_number}")


class BusinessContact(BaseContact):
   def __init__(self,  first_name, last_name, phone_number, email, job, company, biz_number):
      super().__init__( first_name, last_name, phone_number, email)
      self.job = job
      self.biz_number = biz_number
      self.company = company
   
   @property
   def label_lenght():
       return len(fake.last_name  + " " + fake.first_name)

   def __str__(self):
      r = super().__str__()
      r += f"Pracuje w: {self.company} {self.job} {self.biz_number}"
      return r
   
   def contact(self):
      return ("Kontaktuje się z {self.first_name} {self.job} i dzwonię : {self.biz_number}")  

def create_contacts(kind, quantity):
   cards = []
   for _ in range(quantity):
      name = fake.first_name()
      last_name = fake.last_name()
      phone = fake.phone_number()
      email = fake.email()

      if kind == "private":
         c = BaseContact(first_name=name, last_name=last_name, phone_number=phone, email=email)
         cards.append(c)
      elif kind == "business":
         cards.append(
            BusinessContact(
               first_name=name, last_name=last_name, phone_number=phone, email=email,
               biz_number=fake.phone(), job=fake.job(), company=fake.company()
            )
         )
   return cards   


cards = [] 

for c, c1 in cards:
   print(c)
   print(c1)

c = BaseContact(first_name=fake.first_name(), last_name=fake.last_name(), phone_number=fake.phone_number(), email=fake.email())
cards.append(c)

c1 = BusinessContact(first_name=fake.first_name(), last_name=fake.last_name(), phone_number=fake.phone_number, email=fake.email, biz_number=fake.phone_number, job=fake.job, company=fake.company)


if __name__ == "__main__":
   c.create_contacts()
   c.contact()
   
   c1.contact()
   
   BaseContact.label_lenght
   BusinessContact.label_lenght







