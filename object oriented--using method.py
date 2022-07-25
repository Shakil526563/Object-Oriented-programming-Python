class student:
    name=""
    id=""
    def set_value(self,name,id):
        self.name=name
        self.id=id
    def display(self):
        print(f"Name {self.name} ,ID {self.id}")


shakil=student()
shakil.set_value("shakil",3816)
shakil.display()

injam=student()
injam.set_value("injam",3795)
injam.display()

munna=student()
munna.set_value("munna",3598)
munna.display()