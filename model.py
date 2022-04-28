# App Model
employees = [
    {
        'id': 123,
        'name': 'Jesus',
        'lastName': 'Chamorro',
        'birth': '',
        'entry': '',
        'category': 'AS',  # Asalariado o fijo
        'salary': 1000000,
        'sales': [
            {
                'id': 0,
                'client': 0,
                'amount': 0,
                'date': '00/00/00',
                'detail': [0, 0, 0]  # array of ids
            }
        ],
        'clients': [
            {'id': 0, 'name': "", 'amount': 0}
        ]
    },
    {
        'id': 124,
        'name': 'Juan',
        'lastName': 'Valdez',
        'birth': '',
        'entry': '',
        'category': 'CM',  # Asalariado o Comision
        'salary': 1500000,
        'sales': [
            {
                'id': 0,
                'client': 0,
                'amount': 0,
                'date': '00/00/00',
                'detail': [0, 0, 0]  # array of ids
            }
        ],
        'clients': [
            {'id': 0, 'name': "", 'amount': 0}
        ]
    },
]

products = [
    {'id': 0, 'name': "", 'stock': 0, 'price': 0}
]