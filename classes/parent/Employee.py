# Employee parent classes

from abc import ABC, abstractmethod
from parcial_II.model import employees
from parcial_II.errors.consoleErrors import *


class Employee(ABC):

    # Return employee data
    @abstractmethod
    def search(self, ide):
        for employee in employees:
            if ide == employee['id']:
                return employee

    # Return remove status
    @abstractmethod
    def deleteEmployee(self, ide):
        pass

    # Return add status
    @abstractmethod
    def addEmployee(self, data):

        try:

            employees.append(data, 1)
            return True

        except:
            mError('ProcessError', method='Class Employee -> addEmployee()')
            return False

    # Return add status
    @abstractmethod
    def addClient(self, ide, data):

        try:

            for employee in employees:
                if ide == employee['id']:
                    employee['client'].append(data)
                    return True

        except:
            mError('ProcessError', method='Class Employee -> addClient()')
            return False

    # Returns employee' name and id with more clients
    @abstractmethod
    def employeeMoreClient(self):
        pass

    # Returns employee' name and id with more salary
    @abstractmethod
    def employeeMoreSalary(self, ide):
        pass

    @abstractmethod
    def addSales(self, ide, data):

        try:

            for employee in employees:
                if ide == employee['id']:
                    employee['sales'].append(data)
                    return True

        except:
            mError('ProcessError', method='Class Employee -> addSales()')
            return False
