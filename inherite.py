class human:
    def name(self,name):
        self.name=name

    def age(self,age):
        self.age=age

class boy(human):
    def hobby(self,hobby):
        self.hobby=hobby
        print(self.hobby)

class girl(human):
    def makeup(self,makeup):
        self.makeup=makeup
        print(self.makeup)

b=boy()
b.hobby("garden")
b.name("shakil")
print(b.name)

g=girl()
g.name("nita")
print(g.name)
g.makeup("chuno")
