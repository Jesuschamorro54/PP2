# Class Prodcuts

from abc import ABC, abstractmethod


class Products(ABC):

    # Return Product data
    @abstractmethod
    def searchProducts(self, ide):
        pass

    # Add Product
    @abstractmethod
    def addProduct(self, data):
        pass

    # Delete Product
    @abstractmethod
    def deleteProduct(self, ide):
        pass
