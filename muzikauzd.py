from random import*
summa=0
class Instrument:
   def __init__(self,name,tip,cost=150):
      self.cost=cost
      self.tip=tip
      self.name=name
    
      if cost > 100:
        summa=cost*0,2+cost
            
       


inst1=Instrument('klavieres','taustiņinstruments',150)
print(f'{inst1.name} {inst1.tip} {inst1.cost}')
print(f'cena ir {summa} ')


   
   