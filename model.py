# App Model 
employees = [
    {
        'id': 123,
        'name': 'Jesus',
        'lastName': 'Chamorro',
        'birth': '',
        'entry': '',
        'category': 'Aslariado',  # Asalariado o fijo
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
            {'id': 202, 'name': "Maria"},
            {'id': 203, 'name': "Raul"}
        ]
    },
    {
        'id': 124,
        'name': 'Juan',
        'lastName': 'Valdez',
        'birth': '',
        'entry': '',
        'category': 'Fijo',  # Asalariado o fijo
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
            {'id': 102, 'name': "Victor"},
            {'id': 103, 'name': "Victoria"},
            {'id': 104, 'name': "Kenny"}
        ]
    },
    {
        'id': 125,
        'name': 'Laura',
        'lastName': 'Rodrigez',
        'birth': '',
        'entry': '',
        'category': 'Asalariado',  # Asalariado o fijo
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
            {'id': 302, 'name': "Milagros"},
            {'id': 303, 'name': "Roberto"},
            {'id': 304, 'name': "Ane"},
            {'id': 305, 'name': "Hannah"}
        ]
    },
]

products = [
    {'id': 0, 'name': "", 'stock': 0, 'price': 0}
]