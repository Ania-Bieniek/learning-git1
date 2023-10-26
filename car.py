
class Card:
    def __init__(self, first_name, last_name, company_name, worksite, e_mail):
        self.first_name = first_name,
        self.last_name = last_name
        self.company_name = company_name
        self.e_mail = e_mail
        self.worksite = worksite



card_1 = Card(first_name="Zosia", last_name="Samosia", company_name="'Zrób to sam'", worksite= "menager", e_mail="zosia@wp.pl")
card_2 = Card(first_name="Kasia", last_name="Kowalska", company_name="'Model&Model'", worksite="Modelka", e_mail="Kasia@com")
card_3 = Card(first_name="Jasiu", last_name="Mądry", company_name="'Spółka Mądry'", worksite="Malarz", e_mail="Jas@com")
card_4 = Card(first_name="Czesiu", last_name="Szybki", company_name="Fast&c.o", worksite="Tech. grzewcza", e_mail="Tech.com@wp.pl")                 

cards = [card_1, card_2, card_3, card_4]
by_first_name = sorted(cards, key=lambda card: card.first_name)
by_company_name = sorted(cards, key=lambda card: card.company_name)
print(by_company_name())



