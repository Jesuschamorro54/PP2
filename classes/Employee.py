# Employee parent classes

from abc import ABC, abstractmethod


class Employee(ABC):

    # Return employee data
    @abstractmethod
    def search(self, ide):
        pass

    # Return remove status
    @abstractmethod
    def deleteEmployee(self, ide):
        pass

    # Return add status
    @abstractmethod
    def addEmployee(self, data):
        pass

    # Return add status
    @abstractmethod
    def addClient(self):
        pass

    # Returns employee' name and id with more clients
    @abstractmethod
    def employeeMoreClient(self):
        pass

    # Returns employee' name and id with more salary
    @abstractmethod
    def employeeMoreSalary(self, ide):
        pass
