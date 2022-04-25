# Salaried children class

from PP2.classes.parent.Employee import Employee


class Salaried(Employee):
    def addSales(self, ide, data):
        pass

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

    def calculateSalary(self, ide):
        pass

    def addClient(self, ide, data):
        pass
