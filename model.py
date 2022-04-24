# App Model 
employees = [
    {
        'id': 0,
        'name': '',
        'lastName': '',
        'birth': '',
        'entry': '',
        'category': '',  # Asalariado o fijo
        'salary': 0,
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
            {'id': 0, 'name': ""}
        ]
    },
]

products = [
    {'id': 0, 'name': "", 'stock': 0, 'price': 0}
]
