from faker import Faker
fake = Faker()
from faker.generator import random
fake.random
fake.random.getstate()

class Movies:
   def __init__(self, title, year_edition, kind, number_pley):
       self.title = title
       self.year_edition = year_edition
       self.kind = kind
       self.number_pley = number_pley
       #Variables
       self.pley = 0

   def advance_pley(self, step = 0):
       self.pley += step

   def __str__(self) -> str:
       return f'{self.title}{self.year_edition}' 

class Series(Movies):
    def __init__(self, title, year_edition, kind, number_episode, number_season, number_pley):
        super().__init__(title, year_edition, kind, number_pley)
        self.number_episode = number_episode
        self.number_season = number_season
        #Variables
        self.pley = 0

    def advance_pley(self, step = 0):
        self.pley += step

    def __str__(self) -> str:
        return f'S{self.number_seasons:10}E{self.number_epizode:10}'
    
list_Movies_Series = [f'{Series(Movies)} , {Movies}']


    
