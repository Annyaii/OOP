import math
class Ball:
    def __init__(self,diameter):
      self.diameter=diameter
      self.diameter=diameter
      self.helth=120
      self.joy=80

    def volume(self):
       return(math.pi*self.diameter**3)/6
    
    def meeting(self,energy):
       energy.helth-=20

class Cube:
   def __init__(self,mala):
      self.mala=mala
      self.helth=120
      self.joy=80

   def meeting(self,energy):
       energy.helth-=20

   def volume(self):
       return self.mala**3
    
hero1=Ball(5)
print(round(hero1.volume(),2))

hero2=Cube(5)
print(hero2.volume())

print(hero1.helth)
hero1.meeting(hero2)
print(hero2.helth)