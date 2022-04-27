#  Commission children class

from PP2.classes.parent.Employee import Employee
from PP2.config import *


class Commission(Employee):

    def search(self, ide):
        return super(Commission, self).search(ide)

    def deleteEmployee(self, ide):
        return super(Commission, self).deleteEmployee(ide)

    def addEmployee(self, data):
        status, data = verifyData('employee', data)
        if status:
            return super(Commission, self).addEmployee(data)

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

