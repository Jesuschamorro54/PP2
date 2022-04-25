#  Commission children class

from parent.Employee import Employee
from PP2.config import *


class Commission(Employee):

    def search(self, ide):
        return super(Commission, self).search(ide)

    def deleteEmployee(self, ide):
        pass

    def addEmployee(self, data):
        if verifyData('employee', data):
            super(Commission, self).addEmployee(data)

    def addClient(self, ide, data):
        if verifyData('client', data):
            super(Commission, self).addClient(ide, data)

    def addSales(self, ide, data):
        if verifyData('sales', data):
            super(Commission, self).addSales(ide, data)

    def employeeMoreClient(self):
        pass

    def employeeMoreSalary(self):
        pass

    def calculateSalary(self, ide):
        pass


test = Commission()
data = {}
test.addEmployee(data)