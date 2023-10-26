class Card:
    def __init__(self, first_name, last_name, company_name, worksite, e_mail):
        
        self.first_name = first_name
        self.last_name = last_name
        self.company_name = company_name
        self.e_mail = e_mail
        self.worksite = worksite

    @property
    def label_lenght(self):
        return len(self.last_name  + " " + self.first_name)

    def __str__(self) -> str:
        return f"{self.first_name} {self.last_name} {self.e_mail}"    

list_business_card = [
  Card(first_name="Zosia", last_name="Samosia", company_name="'Zrób to sam'", worksite= "menager", e_mail="zosia@wp.pl"),
  Card(first_name="Kasia", last_name="Kowalska", company_name="'Model&Model'", worksite="Modelka", e_mail="Kasia@com"),
  Card(first_name="Jasiu", last_name="Mądry", company_name="'Spółka Mądry'", worksite="Malarz", e_mail="Jas@com"),
  Card(first_name="Czesiu", last_name="Szybki", company_name="Fast&c.o", worksite="Tech. grzewcza", e_mail="Tech.com@wp.pl")                 
  ]

for business_card in list_business_card:
  print(business_card)
card = Card(first_name="Zosia", last_name="Samosia", company_name="'Zrób to sam'", worksite= "menager", e_mail="zosia@wp.pl")
card.label_lenght


