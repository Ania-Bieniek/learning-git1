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
   def __init__(self,  first_name, last_name, phone_number, email, occupation, company, biz_number):
      super().__init__( first_name, last_name, phone_number, email)
      self.occupation = occupation
      self.biz_number = biz_number
      self.company = company
      

   @property
   def label_lenght():
        return len(fake.last_name  + " " + fake.first_name)


   def __str__(self):
      r = super().__str__()
      r += f"Pracuje w: {self.company}"
      return r
   
   def contact(self):
      print("Kontaktuje się z {self.first_name} {self.last_name} i dzwonię pod nr: {self.biz_number}")

   
   def create_contacts():
      kind_contact = input("Wybierz rodzaj wizytówki: 1 - BaseContact, 2 - BusinessContact:")
      quantity = input("Wpisz liczbę wizytówek:")  
      result = kind_contact + quantity
      print(result)  
    
cards = [] 

for c, c1 in cards:
   print(c)
   print(c1)

c = BaseContact(first_name=fake.first_name(), last_name=fake.last_name(), phone_number=fake.phone_number(), email=fake.email())
cards.append(c)

c1 = BusinessContact(first_name=fake.first_name(), last_name=fake.last_name(), biz_number=fake.phone_number, phone_number=fake.phone_number, email=fake.email, occupation=fake.occupation, company=fake.company)
cards.append(c1)


if __name__ == "__main__":
  c.create_contacts()
  c.contact()
  c1.create_contacts()
  c1.contact()
  BaseContact.label_lenght
  BusinessContact.label_lenght







