52
class Rectangle:
    def __init__(self,name,width=10,height=20,color='blue'):
    
        self.width=width
        self.height=height
        self.color=color
        self.name=name

        self.width=int(input("ievadiet platumu: "))
        self.height=int(input("ievadiet garumu: "))
       
rect1=Rectangle('Saquare',100,100,'Orange')
print(f'{rect1.name} {rect1.color} {rect1.width}x{rect1.height}')

rect2=Rectangle('Rect')
print(f'{rect2.name} {rect2.color} {rect2.width}x{rect2.height}')


rectangles=[]
for i in range(100):
    rectangles.append(Rectangle(f'Name{i+1}'))

for rect in rectangles:
    print(f'{rect.name} {rect.color} {rect.width}x{rect.height}')
