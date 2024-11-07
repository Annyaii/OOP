from math import*
from datetime import*
class Olimp:
    def __init__(self,vards,uzvards,klase,skola):
        self.vards=vards
        self.uzvards=uzvards
        self.klase=klase
        self.skola=skola
    def print_info(self):
         print(f'Skolēna vārds: {self.vards}; uzvārds: {self.uzvards}. Mācās {self.klase} klasē {self.skola}')

    def punkti(self,punktikopa):
        self.punktikopa=punktikopa
        punkti1=int(input("ievadiet punktu saitu pirmajā uzdevumā. Maksimālais punktu skaits uzdevumā 20!"))
        punkti2=int(input("ievadiet punktu saitu otrajā uzdevumā. Maksimālais punktu skaits uzdevumā 20!"))
        punkti3=int(input("ievadiet punktu saitu trešajā uzdevumā. Maksimālais punktu skaits uzdevumā 20!"))
        punkti4=int(input("ievadiet punktu saitu ceturtajā uzdevumā. Maksimālais punktu skaits uzdevumā 20!"))
        punkti5=int(input("ievadiet punktu saitu piektaja uzdevumā. Maksimālais punktu skaits uzdevumā 20!"))
        self.punktikopa=punkti1+punkti2+punkti3+punkti4+punkti5
        print(f'Skolēna vārds: {self.vards}; uzvārds: {self.uzvards} ieguva {self.punktikopa} punktus no 100')

    def vieta(self):
        if self.punktikopa>=90:

            print(f'Apsveicam {self.vards} {self.uzvards} ar iegūtiem {self.punktikopa} no 100 un iegūto 1 vietu')
        if self.punktikopa>=80 and self.punktikopa <90:

            print(f'Apsveicam {self.vards} {self.uzvards} ar iegūtiem {self.punktikopa} no 100 un iegūto 2 vietu')
        if self.punktikopa>=70 and self.punktikopa <80:

            print(f'Apsveicam {self.vards} {self.uzvards} ar iegūtiem {self.punktikopa} no 100 un iegūto 3 vietu')
        if self.punktikopa <70:
            print(f'Dimžēl {self.vards} {self.uzvards} ieguva {self.punktikopa} no 100 un šoreiz neiegūst vietu olimpiādē. Taču ceram uz tikšanos nākošgad!')

    def summa(self,nauda):
        self.nauda=nauda
        if self.punktikopa >=70:
            self.nauda=self.punktikopa*10/100 
            print(f'Tu ieguvi {self.nauda} eiro naudas balvu! Apsveicam!')
    def registration(self):
        now = datetime.now()
        dt_string= now.strftime('%d/%m/%Y %H:%M:%S')
        print(f'Olimpiādi {self.vards} {self.uzvards} rakstīja {dt_string}')


skolens1=Olimp('Aleksandrs','Lisicins', 9, 'Rēzeknes 1. ģimnāzija')
skolens1.print_info()
skolens1.punkti(5)
skolens1.vieta()
skolens1.summa(50)
skolens1.registration()
skolens2=Olimp('Alise','Lāce', 10, 'Maltas Vidusskola')
skolens2.print_info()
skolens2.punkti(5)
skolens2.vieta()
skolens2.summa(50)
skolens2.registration()
skolens3=Olimp('Marija','Sergejenko', 11, 'Viļānu Vidusskola')
skolens3.print_info()
skolens3.punkti(5)
skolens3.vieta()
skolens3.summa(50)
skolens3.registration()
skolens4=Olimp('Marks','Matvejevs', 12, 'Dricānu Vidusskola')
skolens4.print_info()
skolens4.punkti(5)
skolens4.vieta()
skolens4.summa(50)
skolens4.registration()
skolens5=Olimp('Viktors','Kancāns', 18, 'Rēzenkes Poļu vidusskola')
skolens5.print_info()
skolens5.punkti(5)
skolens5.vieta()
skolens5.summa(50)
skolens5.registration()