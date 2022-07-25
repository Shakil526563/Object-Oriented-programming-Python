class Student:
    # Constructor
    def __init__(self, name, rollno, m1, m2):
        self.name = name
        self.rollno = rollno
        self.m1 = m1
        self.m2 = m2

    # Function to create and append new student
    def accept(self, Name, Rollno, marks1, marks2):
        # use  ' int(input()) ' method to take input from user
        ob = Student(Name, Rollno, marks1, marks2)
        ls.append(ob)

    # Function to display student details
    def display(self, ob):
        print("Name   : ", ob.name)
        print("RollNo : ", ob.rollno)
        print("Marks1 : ", ob.m1)
        print("Marks2 : ", ob.m2)
        print("\n")

        # Search Function

    def search(self, rn):
        for i in range(ls.__len__()):
            if (ls[i].rollno == rn):
                return i

ls = []
# an object of Student class
obj = Student('', 0, 0, 0)



# ch = int(input("Enter choice:"))
# if(ch == 1):
obj.accept("A", 1, 100, 100)
obj.accept("B", 2, 90, 90)
obj.accept("C", 3, 80, 80)

# elif(ch == 2):
print("\n")
print("\nList of Students\n")
for i in range(ls.__len__()):
    obj.display(ls[i])

# elif(ch == 3):
print("\n Student Found, ")
s = obj.search(2)
obj.display(ls[s])




# else:
print("Thank You !")