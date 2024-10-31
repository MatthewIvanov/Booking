from cmath import inf
from datetime import datetime



def decorator(func):     
    def wrapper(*args,**kwargs):
        start =datetime.now()
        func(*args)
        end=datetime.now()
        print(end-start)
    return  wrapper      

 
@decorator
def sum (a:int,b:int):
    return a+b


class Person:
    def __init__(self,id,name):
        self.id=id
        self.name=name


person = Person(1,'Ava')
print(hash(person))



d={
    'a':1,
    'b':24,
    'c':73,
    'd':444,
}


def max_2_keys(d:dict):
    first,second=None,None
    num1,num2=-inf,-inf
    for i in d:
        if(d[i]>num1):
            num2=num1
            second=first

            first = i
            num1=d[i]

        elif(d[i]>num2):
                num2=d[i]
                second=i

    return first,second

print(max_2_keys(d))