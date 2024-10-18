class Telefons:
    def __init__(self,zime, modelis,cena):
        self.zime=zime
        self.modelis=modelis
        self.cena=cena

        
    def atlaide1(self,atlaide):
        self.atlaide=atlaide
        if int(self.cena)>200:
            beigucena=self.cena-(self.cena*self.atlaide/100)
            print(f'Cena ir lielāka par200. tāpēc ir piemērota atlaide 20 procenti. Beigu cena {beigucena}')
        else:
            print('Atlaides nav')

    

    def paradit_info(self):
        print(f'Telefons {self.zime} modelis{self.modelis} cena{self.cena}')
    def iestatit_tonu(self,jauns_tonis):
        self.jauns_tonis=jauns_tonis
        print(f"Telefons jaunais tonis ir {self.jauns_tonis}")
    

telefons1=Telefons('Samsung','A4',250)
telefons1.paradit_info()
telefons1.iestatit_tonu('pink')
telefons1.atlaide1(20)