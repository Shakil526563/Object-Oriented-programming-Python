class student:
    def name(self):
        name=input()
        print(name)

    def id(self):
        print(55)

class teacher(student):
    def faculty(self):
        print("cse")
    def Tname(self):
        print("Shakil")
    def age(self):
        print("young")


t=teacher()
t.name()
t.Tname()
t.id()
t.age()

"""akn teacher class ar modde student ar details chole asbe.akn just teacher ar object create
                          student ar teacher 2 jon ar method kei call dite parbo"""