
class Movie:
   def __init__(self, title, year, kind):
       self.title = title
       self.year = year
       self.kind = kind
       self.play_counter = 0

   def pley(self):
       self.play_counter += 1

   def __repr__(self) -> str:
       return f'{self.title}{self.year}' 
   

def search(library):
    x = input("Wybierz tytuł:")
    for i in list:
        if x == i.title:
            print("Tytuł jest w biblitece")
            return
    print("Nie mam takiego tytułu w bibiliotece")


class Serie(Movie):
    def __init__(self, title, year, kind, number_seasons, number_episode):
        super().__init__(title, year, kind)
        self.number_episode = number_episode
        self.number_seasons = number_seasons

    def __repr__(self) -> str:
        return f'{self.title} S{self.number_seasons:02}E{self.number_episode:02}'
    
     
library =[]

m = Movie(title="Kong", year=2017, kind="fantasy")
m2 = Movie(title="Megalodon", year=2018, kind="horror")

s = Serie(title="Dr House", year=2004, kind="medyczny", number_seasons=1, number_episode=1) 
s2 = Serie(title="Szpital Amsterdam", year=2018, kind="medyczny", number_seasons=1, number_episode=1)  

library.append(m)
library.append(s)
library.append(m2)
library.append(s2)

print(library)


def get_movies(library):
    r = []
    for el in library:
        if type(el) == Movie:
            r.append(el)
        
    return r

print(get_movies(library))

def get_series(library):
    r = []
    for el in library:
        if type(el) == Serie:
            r.append(el)
    return r

print(get_series(library))
        

def search(library):
    a = input("Wybierz tytuł:")
    for i in library:
        if a == i.title:
            print("Tytuł jest w biblitece")
            return
    print("Nie mam takiego tytułu w bibliotece")


print(search(library))

