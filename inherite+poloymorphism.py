class vehicle:
    def __init__(self,name,color,price):
         self.name=name
         self.color=color
         self.price=price
    def dis(self):
        print(self.name,self.color,self.price)

    def speed(self,speed):
        self.speed=speed
        print(f'maximum speed {self.speed}')

    def geaur(self,geaur):
        self.geaur=geaur
        print(f'maximum geaur {self.geaur}')
class  car(vehicle):
    def speed(self,speed):
        self.speed=speed
        print(self.speed)

c=car("toyta","black",5555555)
c.dis()
c.speed(6)
c.geaur(8)
v=vehicle("car",'white',99999)
v.dis()
v.geaur(15)
