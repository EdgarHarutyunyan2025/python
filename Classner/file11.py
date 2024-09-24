class Goods:

    def __init__(self,name,weight,price):
        super().__init__()
        print('info Goods')
        self.name=name
        self.weight=weight
        self.price=price

    def print_info(self):
        return f'{self.name},{self.weight},{self.price}'


class Mixinlog:            
    ID=0

    def __init__(self):
        print('info Mixinlog')
        self.ID+=1
        self.id=self.ID

    
    

    def seve_sell_log(self):
        print(f'{self.id}:Товар продан')


class  Mixinlog_2:
    ID=5

    def __init__(self):
        print('info Mixinlog 2')
        self.ID+=1
        self.id=self.ID
        
 

    def seve_sell_log(self):
        print(f'{self.id}:Товар продан')



class NootBook(Goods,Mixinlog,Mixinlog_2):
    pass



n=NootBook('Acer',1.5,300000)
p=Mixinlog_2()
print(n.print_info())
print(n.ID)

#n.seve_sell_log()
print(NootBook.__mro__)
