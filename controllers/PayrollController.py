from PP2 import model
from PP2.config import *


def calculatePayroll(category):
    payroll = 0

    for employee in model.employees:
        if employee['category'] == category:
            payroll += employee['salary']

    return payroll
