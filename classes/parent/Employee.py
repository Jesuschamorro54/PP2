# Employee parent classes

from abc import ABC, abstractmethod
from PP2 import model
from PP2.errors.consoleErrors import *

from PP2.controllers.SalaryController import setSalary


class Employee(ABC):

    # Return employee data
    @abstractmethod
    def search(self, ide):
        setSalary()
        for employee in model.employees:
            if ide == employee['id']:
                return employee
        return False

    # Return remove status
    @abstractmethod
    def deleteEmployee(self, ide):
        index = 0
        for employee in model.employees:
            if ide == employee['id']:
                model.employees.pop(index)
            index += 1
        return model.employees

    # Return add status
    @abstractmethod
    def addEmployee(self, data):

        try:

            model.employees.append(data)
            return model.employees

        except:
            mError('ProcessError', method='Class Employee -> addEmployee()')
            return False

    # Return add status
    @abstractmethod
    def addClient(self, ide, data):
        try:

            for employee in model.employees:
                if ide == employee['id']:

                    print("se encontro el empleado")
                    employee['clients'].append(data)

            return model.employees

        except ValueError as e:
            mError('ProcessError', method='Class Employee -> addClient()')

    # Returns employee' name and id with more clients
    @abstractmethod
    def employeeMoreClient(self):
        result = model.employees[0]
        ide = model.employees[0]['id']
        for employee in model.employees:
            if len(employee['clients']) > len(result['clients']):
                ide = employee['id']
                result = employee
        return ide

    # Returns employee' name and id with more salary
    @abstractmethod
    def employeeMoreSalary(self):
        setSalary()
        result = model.employees[0]
        ide = model.employees[0]['id']
        for employee in model.employees:
            if employee['salary'] > result['salary']:
                ide = employee['id']
                result = employee
        return ide

    @abstractmethod
    def addSales(self, ide, data):

        try:

            for employee in model.employees:
                if ide == employee['id']:
                    employee['sales'].append(data)
                    return True

        except:
            mError('ProcessError', method='Class Employee -> addSales()')
            return False
