class Card:
    def __init__(self, contact, first_name, last_name, company_name, worksite, e_mail):
        self.contact = contact,
        self.first_name = first_name,
        self.last_name = last_name
        self.company_name = company_name
        self.e_mail = e_mail
        self.worksite = worksite
        @property
        def sum_name(self):
          return self.sum_name
        @sum_name.setter
        def sum_name(self, sum):
           if sum == len(last_name, " " ,first_name):
            self.sum_name = sum
           else: 
             raise ValueError

list_business_card = [
  Card(contact='Kontaktuje się z:', first_name="Zosia", last_name="Samosia", company_name="'Zrób to sam'", worksite= "menager", e_mail="zosia@wp.pl"),
  Card(contact="Kontaktuje się z:", first_name="Kasia", last_name="Kowalska", company_name="'Model&Model'", worksite="Modelka", e_mail="Kasia@com"),
  Card(contact="Kontaktuje się z:", first_name="Jasiu", last_name="Mądry", company_name="'Spółka Mądry'", worksite="Malarz", e_mail="Jas@com"),
  Card(contact="Kontaktuje się z:", first_name="Czesiu", last_name="Szybki", company_name="Fast&c.o", worksite="Tech. grzewcza", e_mail="Tech.com@wp.pl")                 
  ]

for business_card in list_business_card:
  print(business_card.contact, business_card.first_name, business_card.last_name, business_card.company_name, business_card.worksite, business_card.e_mail)
card = Card(contact='Kontaktuje się z:', first_name="Zosia", last_name="Samosia", company_name="'Zrób to sam'", worksite= "menager", e_mail="zosia@wp.pl"),
card.sum_name


