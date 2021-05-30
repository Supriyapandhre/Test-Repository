"""
A(father) -> B(child)

"""

class father:
    def __init__(self, wealth, house, skill):
        self.wealth = wealth
        self.house = house
        self.skill = skill

    def shows_father_wealth(self):
        print("Father Wealth is :", self.wealth)

    def show_father_house(self):
        print("Father House :", self.house)

    def father_skill(self):
        print("Father skill is :", self.skill)


class child(father):
    def __init__(self, job, salary, skill, wealth, house):
        super().__init__(wealth, house, skill)
        self.job = job
        self.salary = salary

    def show_child_job(self):
        print("Child Job :",self.job)

    def show_child_salary(self):
        print("Child Salary :", self.salary)

    def shows_child_skill(self):
        print("Child Skill :", self.skill)

obj = child('IT', 5000, 'Tenis', '5cr', 'Banglow')
obj.show_child_job()
obj.show_father_house()


obj.father_skill()
obj.shows_child_skill()