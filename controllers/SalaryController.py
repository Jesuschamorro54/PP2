from ..config import basic_salary


def setStaticSalary(num_of_year):
    percentage = 1.0

    if 2 <= num_of_year <= 3:
        percentage = 0.05
    elif 4 <= num_of_year <= 7:
        percentage = 0.10
    elif 8 <= num_of_year <= 15:
        percentage = 0.15
    elif 15 < num_of_year:
        percentage = 0.20

    return basic_salary * percentage


def setCommissionSalary(clients, sales=None):
    amount = 0
    for client in clients:
        amount += client['amount']

    return len(clients) * amount
