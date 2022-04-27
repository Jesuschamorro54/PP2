import sys

from PyQt5 import uic
from PyQt5.QtWidgets import *
import model


from classes.children.Commission import Commission
from classes.children.Salaried import Salaried


class Root(QMainWindow):

    def __init__(self):
        super().__init__()
        self.data = None
        self.radioClicked = ''

        uic.loadUi("main.ui", self)

        self.loadData()

        # LABELS
        self.message.setStyleSheet("color: #000000")
        self.cant_client.setText('')

        # BUTTONS FORM
        self.addEmployeeBT.clicked.connect(self.createEmployee)
        self.addClientBT.clicked.connect(self.createEmployee)

        # BUTTONS TABLE
        self.employeeMoreClientBT.clicked.connect(self.search)
        self.employeeMoreSalaryBT.clicked.connect(self.search)
        self.searchBT.clicked.connect(self.search)
        self.deleteBT.clicked.connect(self.delete)
        self.showAllBT.clicked.connect(self.loadData)

        # RADIO BUTTONS
        self.radioSalaried.toggled.connect(self.onClickedRadioButtom)
        self.radioCommision.toggled.connect(self.onClickedRadioButtom)

    def onClickedRadioButtom(self):
        radioBt = self.sender()
        if radioBt.text() == 'Asalariado':
            self.radioClicked = radioBt.text()
        elif radioBt.text() == 'Comision':
            self.radioClicked = radioBt.text()

    def loadData(self):
        self.printTable(model.employees)

    def search(self):
        try:
            data = []
            ide = int(self.searchInput.text())
            data.append(employeeComission.search(ide))  # [{}]
            self.printTable(data)
        except ValueError as e:
            print(f"Error {e}")

    def delete(self):
        try:
            ide = int(self.searchInput.text())
            model.employees = employeeComission.deleteEmployee(ide)
            self.printTable(model.employees)
            print(f"Eliminado {model.employees}")
        except ValueError as e:
            print(f"Error {e}")

    def printTable(self, data):
        for i in range(len(data) + 1):
            self.EmployeeTable.removeRow(0)
        row = 0

        for employee in data:  # Gestiona filas
            column = 0
            self.EmployeeTable.insertRow(row)
            for field in employee:  # Gestiona Columnas
                if field not in ['sales', 'clients']:
                    dato = QTableWidgetItem(str(employee[field]))

                    self.EmployeeTable.setItem(row, column, dato)
                    column += 1
            row += 1

    def createEmployee(self):
        data = {}
        ide = self.e_idInput.text()
        name = self.e_nameInput.text()
        entry = self.e_entryInput.text()

        if self.radioClicked != '':
            print("Armando data")
            data = {
                'id': ide,
                'name': name,
                'entry': entry,
                'category': self.radioClicked,
            }

            if self.e_lastnameInput.text() != '':
                data['lastname'] = self.e_lastnameInput.text()
            if self.e_birthInput.text() != '':
                data['birth'] = self.e_birthInput.text()
        else:
            print("Llena esa vaina")

        if data:
            print("Creando....")
            if self.radioClicked == 'Comision':
                print("Por comision")
                model.employees = employeeComission.addEmployee(data)
            else:
                print("Por salario")
                model.employees = employeeSalaried.addEmployee(data)

        self.loadData()


if __name__ == "__main__":
    employeeComission = Commission()
    employeeSalaried = Salaried()
    app = QApplication(sys.argv)
    gui = Root()
    gui.show()

    sys.exit(app.exec_())
