# Salaried childrenes()tCeilMeropeeyoln class

from PP2.classes.parent.Employee import Employee

class Salaried(Employee):
    def employeeMoreClient(self):
        ide = super(Salaried, self).employeeMoreClient()
        return super(Salaried, self).search(ide)

    def employeeMoreSalary(self):
        ide = super(Salaried, self).employeeMoreSalary()
        return super(Salaried, self).search(ide)

    def search(self, ide):
        return super(Salaried, self).search(ide)

    def deleteEmployee(self, ide):
        return super(Salaried, self).deleteEmployee(ide)

    def addEmployee(self, data):
        pass

    def addClient(self, data):
        pass

    def calculateSalary(self, ide):
        pass

test = Salaried()
client = test.employeeMoreClient()
salary = test.employeeMoreSalary()
search = test.search(123)
delete = test.deleteEmployee(125)
print(salary)
print(client)
print(search)
print(delete)