
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
   
   def __repr__(self) -> str:
       return f"Movies(title={self.title} year_edition={self.year_edition} kind={self.kind} number_pley={self.number_pley})"
   
   def get_movies(list):
        for i in list:
            if type(i) == Movies:
                list_movie.append(i)
        list_m1 = sorted(list_movie, key=lambda movie: movie.title)

   def search(list):
        x = input("Wybierz tytuł:")
        for i in list:
            if x == i.title:
                print("Tytuł jest w biblitece")
                return
        print("Nie mam takiego tytułu w bibiliotece")


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
    
    def __repr__(self) -> str:
       return f"Series(title={self.title} year_edition={self.year_edition} kind={self.kind} number_pley={self.number_pley})"
   
    def get_series(list):
        for i in list:
            if type(i) == Series:
                list_series.append(i)
        list_s1 = sorted(list_series, key=lambda series: series.title)

    def search(list):
        x = input("Wybierz tytuł:")
        for i in list:
            if x == i.title:
                print("Tytuł jest w biblitece")
                return
        print("Nie mam takiego tytułu w bibiliotece")

list_m1 = Movies(title="Kong", year_edition=2017, kind="fantasy", number_pley=0, )
list_m2 = Movies(title="Megalodon", year_edition=2018, kind="horror", number_pley=0)

list_s1 = Series(title="Dr House", year_edition=2004, kind="medyczny", number_episode=1, number_season=1, number_pley=0) 
list_s2 = Series(title="Szpital Amsterdam", year_edition=2018, kind="medyczny", number_episode=1, number_season=1, number_pley=0)  

list_movie = ["Megalodon", "Kong"]
list_series = ["Dr House", "Szpital Amsterdam"]

list = [f'{Series} + {Movies}']
#list_m1.get_movies()
list_m1.search()
list_m1.advance_pley
