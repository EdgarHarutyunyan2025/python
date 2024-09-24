class Stack:
    def __init__(self):
        self.stack=[]

    def add_obj(self,obj):
        self.stack.append(obj)

    def del_obj(self):
        self.stack.pop()
        
    def __str__(self):
        return f'element count:  {len(self.stack)}'
    
stack=Stack()
stack.add_obj(10)
stack.add_obj(20)
print(stack)
obj=stack.del_obj()
print(obj)
print(stack)

      

