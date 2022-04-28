from PP2.config import basic_salary
from PP2 import model
import datetime


def setStaticSalary(entry):
    currentYear = int(datetime.date.today().strftime("%Y"))
    num_of_year = currentYear - entry
    percentage = 1.0

    if 2 <= num_of_year <= 3:
        percentage = 0.05
    elif 4 <= num_of_year <= 7:
        percentage = 0.10
    elif 8 <= num_of_year <= 15:
        percentage = 0.15
    elif 15 < num_of_year:
        percentage = 0.20

    return round((basic_salary + (basic_salary * percentage)), 2)


def setCommissionSalary(clients, sales=None):
    amount = 0
    for client in clients:
        amount += client['amount']

    return len(clients) * amount


def setSalary():
    for employee in model.employees:
        if employee['category'] == 'Comision':
            employee['salary'] = setCommissionSalary(employee['clients'])
