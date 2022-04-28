import sys

from PyQt5 import uic
from PyQt5.QtWidgets import *
import model

from classes.children.Commission import Commission
from classes.children.Salaried import Salaried

from controllers.SalaryController import setStaticSalary, setSalary
from controllers.PayrollController import calculatePayroll


class Root(QMainWindow):

    def __init__(self):
        super().__init__()
        self.comboItems = {}
        self.dataClients = []
        self.radioClicked = ''

        uic.loadUi("main.ui", self)

        self.loadData()

        # BAR ACTIONS
        self.actionEmployeeView.triggered.connect(lambda: self.changeView('employee'))
        self.actionInfoView.triggered.connect(lambda: self.changeView('info'))

        # LABELS
        self.message.setStyleSheet("color: #E52B2B")
        self.cant_client.setText('')

        # BUTTONS FORM
        self.addEmployeeBT.clicked.connect(self.createEmployee)
        self.addClientBT.clicked.connect(self.createClient)

        # BUTTONS TABLE
        self.employeeMoreClientBT.clicked.connect(self.employeeMoreClients)
        self.employeeMoreSalaryBT.clicked.connect(self.employeeMoreSalary)
        self.searchBT.clicked.connect(self.search)
        self.deleteBT.clicked.connect(self.delete)
        self.showAllBT.clicked.connect(self.loadData)

        # RADIO BUTTONS
        self.radioSalaried.toggled.connect(self.onClickedRadioButtom)
        self.radioCommision.toggled.connect(self.onClickedRadioButtom)
        self.radioPayrollSalaried.toggled.connect(self.onClickedRadioButtom)
        self.radioPayrollComission.toggled.connect(self.onClickedRadioButtom)

    def changeView(self, view):
        if view == 'employee':
            self.tabWidget.setCurrentIndex(0)
        else:
            self.tabWidget.setCurrentIndex(1)

    def onClickedRadioButtom(self):
        radioBt = self.sender()
        self.totalPayrollInput.setText("")
        if radioBt.text() == 'Asalariado' and radioBt.isChecked():
            self.e_entryInput.setEnabled(True)
            self.comboNumOfYear.setEnabled(True)
            self.radioClicked = radioBt.text()
        elif radioBt.text() == 'Comision' and radioBt.isChecked():
            self.e_entryInput.setEnabled(False)
            self.comboNumOfYear.setEnabled(False)
            self.radioClicked = radioBt.text()
        elif radioBt.text() == 'Nomina Asalariado':
            self.totalPayrollInput.setText(f"${employeeSalaried.calculatePayroll()}")
        elif radioBt.text() == 'Nomina Comision':
            self.totalPayrollInput.setText(f"${employeeComission.calculatePayroll()}")

    def comboBoxItems(self):
        self.comboItems = {}
        for i in range(len(model.employees) + 1):
            self.comboNameEmployee.removeItem(1)

        for employee in model.employees:
            self.comboNameEmployee.addItem(employee['name'])
            self.comboItems[employee['name']] = employee['id']

    def clearFields(self):
        self.e_idInput.setText("")
        self.e_nameInput.setText("")
        self.e_entryInput.setText("")
        self.e_lastnameInput.setText("")
        self.e_birthInput.setText("")
        self.c_idInput.setText("")
        self.c_amountInput.setText("")
        self.c_nameInput.setText("")

    def loadData(self):
        setSalary()
        self.comboBoxItems()
        self.printTable(model.employees)

        for i in range(len(self.dataClients) + 1):
            self.clientTable.removeRow(0)
        self.dataClients = []

    def search(self):
        data = []
        try:
            ide = int(self.searchInput.text())
            data.append(employeeComission.search(ide))  # [{}]
            if data[0]:
                self.printTable(data)
                self.printTableClient(data[0]['clients'])
        except ValueError as e:
            print(f"Error {e}")

    def delete(self):
        try:
            ide = int(self.searchInput.text())
            model.employees = employeeComission.deleteEmployee(ide)
            self.printTable(model.employees)
            self.comboBoxItems()
        except ValueError as e:
            print(f"Error {e}")

    def printTable(self, data):
        for i in range(len(model.employees) + 1):
            self.EmployeeTable.removeRow(0)
        row = 0

        for employee in data:  # Gestiona filas
            column = 0
            self.EmployeeTable.insertRow(row)
            for field in employee:  # Gestiona Columnas
                if field == 'clients':
                    dato = len(employee[field])
                else:
                    dato = (employee[field])

                dato = QTableWidgetItem(str(dato))
                self.EmployeeTable.setItem(row, column, dato)
                column += 1
            row += 1

    def printTableClient(self, data):
        for i in range(len(self.dataClients) + 1):
            self.clientTable.removeRow(0)
        row = 0

        self.dataClients = []
        for client in data:  # Gestiona filas
            self.dataClients.append(client)
            column = 0
            self.clientTable.insertRow(row)
            for field in client:  # Gestiona Columnas
                dato = QTableWidgetItem(str(client[field]))
                self.clientTable.setItem(row, column, dato)
                column += 1
            row += 1

    def createEmployee(self):
        self.message.setStyleSheet("color: #E52B2B")
        data = {}
        try:
            ide = int(self.e_idInput.text())
            name = self.e_nameInput.text()

            if self.radioClicked != '' and name != '':
                if self.radioClicked == 'Asalariado':
                    entry = int(self.e_entryInput.text())
                    if entry:
                        data = {
                            'id': ide,
                            'name': name,
                            'lastname': self.e_lastnameInput.text(),
                            'birth': self.e_birthInput.text(),
                            'entry': entry,
                            'category': self.radioClicked,
                            'salary': setStaticSalary(entry)
                        }
                    else:
                        self.message.setText("Aún hay campos obligatorios sin completar")
                else:
                    data = {
                        'id': ide,
                        'name': name,
                        'lastName': self.e_lastnameInput.text(),
                        'birth': self.e_birthInput.text(),
                        'entry': '',
                        'category': self.radioClicked,
                    }
            else:
                self.message.setText("Aún hay campos obligatorios sin completar")
        except:
            pass

        if data:
            try:
                if self.radioClicked == 'Comision':
                    model.employees = employeeComission.addEmployee(data)
                else:
                    model.employees = employeeSalaried.addEmployee(data)
                self.message.setStyleSheet("color: #27CF22")
                self.message.setText("Se agregó correctamente")
                self.clearFields()

            except:
                self.message.setStyleSheet("color: #E52B2B")
                self.message.setText("Ocurrió un error al momento de guardar")

        self.loadData()

    def createClient(self):
        self.message.setStyleSheet("color: #E52B2B")
        data = {}
        try:
            ideClient = int(self.c_idInput.text())
            amount = int(self.c_amountInput.text())

            if self.comboNameEmployee.currentIndex() != 0:
                ideEmployee = self.comboItems[self.comboNameEmployee.currentText()]
                data = {
                    'id': ideClient,
                    'name': self.c_nameInput.text(),
                    'amount': amount
                }

                model.employees = employeeComission.addClient(ideEmployee, data)
                self.message.setStyleSheet("color: #27CF22")
                self.message.setText("Se agregó correctamente")
                self.clearFields()

            else:
                self.message.setText("Aún hay campos obligatorios sin completar")

        except ValueError as e:
            self.message.setStyleSheet("color: #E52B2B")
            self.message.setText("Ocurrió un error al momento de guardar")

        self.loadData()

    def employeeMoreSalary(self):
        data = [employeeComission.employeeMoreSalary()]
        if data:
            self.printTable(data)
            self.printTableClient(data[0]['clients'])

    def employeeMoreClients(self):
        data = [employeeComission.employeeMoreClient()]

        if data:
            self.printTable(data)
            self.printTableClient(data[0]['clients'])


if __name__ == "__main__":
    employeeComission = Commission()
    employeeSalaried = Salaried()
    app = QApplication(sys.argv)
    gui = Root()
    gui.show()

    sys.exit(app.exec_())
