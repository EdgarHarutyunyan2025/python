class Car:
    def __init__(self,num):
        self.num=num

    def __add__(self,num):
        if isinstance(num,Car):
            return self.num+num.num
        return self.num+num
    
    def __radd__(self,num):
        return self+num
    
    def __sub__(self,num):
        if isinstance(num,Car):
            return self.num-num.num
        return self.num-num
    
    def __rsub__(self,num):
        return num-self.num
    
    def __mul__(self,num):
        if isinstance(num,Car):
            return self.num*num.num
        return self.num*num
    
    def __rmul__(self,num):
        return self*num
    

b=Car(5)
a=Car(9)

print(a+b)
        
class Humen:
    def __init__(self,name,age,city):
        self.__name=name
        self.__age=age
        self.__city=city


    def get_name(self):
        return self.__name
    
    def set_name(self,new_name):
        self.__name=new_name

    def get_age(self):
        return self.__age
    
    def set_age(self,new_age):
        self.__age=new_age

    def get_city(self):
        return self.__city
    
    def set_city(self,new_city):
        self.__city=new_city
    
    
    
    age=property(get_age,set_age)
    name=property(get_name,set_name)
    city=property(get_city,set_city)
 

h1=Humen('Jain',88,'USA')
h2=Humen('Jain',88,'USA')

h2.name='bob'



print(h1.age+h2.age)