# Employee parent classes

from abc import ABC, abstractmethod
from PP2.model import employees
from PP2.errors.consoleErrors import *


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
        index = 0
        for employee in employees:
            if ide == employee['id']:
                employees.pop(index)
                return employees
            index += 1

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
        result = employees[0]
        ide = employees[0]['id']
        for employee in employees:
            if len(employee['clients']) > len(result['clients']):
                ide = employee['id']
        return ide

    # Returns employee' name and id with more salary
    @abstractmethod
    def employeeMoreSalary(self):
        result = employees[0]
        ide = employees[0]['id']
        for employee in employees:
            if employee['salary'] > result['salary']:
                ide = employee['id']
        return ide

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
