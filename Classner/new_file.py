import sys
class  Human:
    gender=''
    
    def __init__(self,name,age):
        super().__init__()
        self.name=name
        self.age=age
    
    def info_human(self):
        return f'name-{self.name},age-{self.age},gender-{self.gender}'

class Humn_info:
    def __init__(self):
        if isinstance(self,Man):
            self.gender='Male'
        else:
            self.gender='Female'
             

class Man(Human,Humn_info):
    pass  

class Woman(Human,Humn_info):
    pass

       
mans=Man('Bob',29)
womans=Woman('An',37)
#print(mans.info_human())
#print(womans.info_human())

print(mans.__sizeof__())

w =[1, 2]
x =[4, 5, 7, 9]
y =[2, 8, 6, 56, 45, 89, 88]
z =[54, 45, 12, 23, 24, 90, 20, 40]
print(w.__sizeof__())
print(x.__sizeof__())
print(y.__sizeof__())
print(z.__sizeof__())