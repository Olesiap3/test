class Car:
    
    def __init__(self, model=None, manufactur=None, year_of_issue=None, engine=None, color=None, price=None):
        self.model = model
        self.year_of_issue = year_of_issue
        self.manufactur = manufactur
        self.engine = engine
        self.color = color
        self.price = price
        
        
    def get_description(self):
        if self.model:
            return f"Your Car is {self.model} Model, start of use is {self.year_of_issue} "

    def get_features(self):
        if self.manufactur:
            return f" {self.model} manufacturer from {self.manufactur},\n it has {self.color} color and enginer is {self.engine}"
    
    def get_cost(self):
        currency = '$'
        return f" Price yours car is {self.price}" + currency


acura = Car("Acura MDX 3.5i VTEC", "Tokyo,Japan", 2015, "3.5(290k.s/213kVt","Black", 29900)
alfa_romeo =Car( "Alfa Romeo Stelvio", "Turin, Italy", 2019, "2L(280k.s/206kVt", "Black", 34900)
skoda = Car( "Skoda Kodiaq", "Mlada Boleslav, Czechia", 2021, "2l Diesel", "Blue", 38067 )
genesis = Car( "Hyundai Genesis", "Seoul, South Korea", 2014, "3.8L", "Brown", 22500 )



print(acura.get_description())
print(acura.get_features())
print(acura.get_cost())

print("---------------------")

print(alfa_romeo.get_description())
print(alfa_romeo.get_features())
print(alfa_romeo.get_cost())







print("-------------------------BOOK-----------------------------")

class Book:
    def  __init__(self, name=None, year=None, publish=None, genre=None, autor=None, price=None):
       self.name = name
       self.year = year
       self.publish = publish
       self.genre = genre
       self.autor = autor
       self.price = price

    def get_name (self):
        return f' {self.name} published in {self.year} year,\n this Book is written in the {self.genre} genre. '

    def get_autor(self):
        return f' Autor this Book {self.name} is {self.autor}'
    def get_price(self):
        return f' {self.name} was published {self.publish} and costs {self.price}$'
lord_the_rings = Book('"Lord of the Ring I"', 1954, 'Allen&Unwin', 'High Fantasy/Adventur', 'J.R.P.Tolkien', 14)
alchemist = Book('"The Alchemist"', 1993, 'Harper Torch', 'Quest/adventure/fantasy', 'Paulo Coelho', 20)

print(lord_the_rings.get_name())
print(lord_the_rings.get_autor())
print(lord_the_rings.get_price())

print("------------------")

print(alchemist.get_name())
print(alchemist.get_autor())
print(alchemist.get_price())

print("---------------------------------------------------")

class Stadium:
    def __init__(self, name, date, country, city, capacity):
        self.name = name
        self.date = date
        self.country = country
        self.city = city
        self.capacity = capacity
    def get_name(self):
        return f"The stadium {self.name} is located in {self.country} in city {self.city} and opened was in {self.date} year"
    def get_capacity(self):
        return f" Capacity { self.name} is {self.capacity} Thousand"

jakob = Stadium( '"St. Jakob-Park"', '15.March.2001', 'Swizerland', 'Basel', 40)
london = Stadium( '"London Stadium"', '6.Mai.2012', '', 'London', 80)

print(jakob.get_name())
print(jakob.get_capacity())

print("-----------------")

print(london.get_name())
print(london.get_capacity())


#========================RESULT========================
'''Acura MDX 3.5i VTEC manufacturer from Tokyo,Japan,
 it has Black color and enginer is 3.5(290k.s/213kVt
 Price yours car is 29900$
---------------------
Your Car is Alfa Romeo Stelvio Model, start of use is 2019 
 Alfa Romeo Stelvio manufacturer from Turin, Italy,
 it has Black color and enginer is 2L(280k.s/206kVt
 Price yours car is 34900$
-------------------------BOOK-----------------------------
 "Lord of the Ring I" published in 1954 year,
 this Book is written in the High Fantasy/Adventur genre. 
 Autor this Book "Lord of the Ring I" is J.R.P.Tolkien
 "Lord of the Ring I" was published Allen&Unwin and costs 14$
------------------
 "The Alchemist" published in 1993 year,
 this Book is written in the Quest/adventure/fantasy genre. 
 Autor this Book "The Alchemist" is Paulo Coelho
 "The Alchemist" was published Harper Torch and costs 20$
---------------------------------------------------
The stadium "St. Jakob-Park" is located in Swizerland in city Basel and opened was in 15.March.2001 year
 Capacity "St. Jakob-Park" is 40.0
-----------------
The stadium "London Stadium" is located in  in city London and opened was in 6.Mai.2012 year
 Capacity "London Stadium" is 80.0'''