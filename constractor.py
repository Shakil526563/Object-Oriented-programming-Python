"""constractor is a special type of contractor
here we pass the value between the object

it's keyword init;
value  pass between the object
"""
import pandas as pn
class student:
    name=""
    id=""
    def __init__(self,name,id):
        self.name=name
        self.id=id
    def display(self):
        print(f"Name {self.name} ,ID {self.id}")



shakil=student("shakil",3816)
shakil.display()
