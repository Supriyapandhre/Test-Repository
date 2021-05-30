"""
A(Father)  -> C (Son)
B(Mother)  -> C (Son)
"""

class father:

    def __init__(self, job, property):
        self.job = job
        self.property = property

    def  shows_father_details(self):
        print("Father Job :", self.job)

class mother:

    def __init__(self, Business):
        self.business = Business

    def shows_mother_details(self):
        print("Mother Business :", self.business)

# Method Resolution Order (MRO)
class Son(father, mother):

    def __init__(self, name, job, property, business):
        self.name = name
        super().__init__(job, property)
        #super().__init__(business)
        self.mom = mother(business)

        #self.dad = father(job, property)

    def show_name(self):
        print("Name : ",self.name)

obj = Son('Harry', 'IPS', '25cr', 'Garment')

obj.shows_father_details()
obj.show_name()
obj.mom.shows_mother_details()
#obj.dad.shows_father_details()

