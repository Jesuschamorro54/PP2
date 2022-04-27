# Salaried children class

from PP2.classes.parent.Employee import Employee
from PP2.config import *
from PP2.controllers.SalaryController import *


class Salaried(Employee):
    def search(self, ide):
        return super(Salaried, self).search(ide)

    def deleteEmployee(self, ide):
        return super(Salaried, self).deleteEmployee(ide)

    def addEmployee(self, data):
        status, data = verifyData('employee', data)
        if status:
            return super(Salaried, self).addEmployee(data)

    def addClient(self, ide, data):
        if verifyData('client', data):
            super(Salaried, self).addClient(ide, data)

    def addSales(self, ide, data):
        if verifyData('sales', data):
            super(Salaried, self).addSales(ide, data)

    def employeeMoreClient(self):
        ide = super(Salaried, self).employeeMoreClient()
        return super(Salaried, self).search(ide)

    def employeeMoreSalary(self):
        ide = super(Salaried, self).employeeMoreSalary()
        return super(Salaried, self).search(ide)

    # Employee with static salary
    def calculateSalary(self):
        pass
