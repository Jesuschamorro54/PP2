from PP2.errors.consoleErrors import *

basic_salary = 1000282

mandatory_fields = {
    'employee': [
        'id',
        'name',
        'category',
    ],
    'client': [
        'id',
        'name',
        'amount',
    ],
    'sales': [
        'id',
        'client',
        'amount',
        'date',
        'details',
    ]

}

defaults_fields = {
    'employee': {
        'lastName': '',
        'birth': '',
        'salary': 0,
        'sales': [],
        'clients': [],
    },
}

RadioButtonsId = {
    'Asalariado': 'AS',
    'Comision': 'CM',
}


def verifyData(model, data):
    # Verify mandatory fields
    for field in mandatory_fields[model]:
        if field not in data.keys():
            mError('InsufficientParameters', model, field)

            return False

    # Add defaults fields
    if model in defaults_fields.keys():
        for key, value in defaults_fields[model].items():
            if key not in data:
                data[key] = value
    return True, data
