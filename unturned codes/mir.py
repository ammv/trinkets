import json

locations = {
            'easy': ['Kivgrad Harbor', 'Vladimir Farm', 'Chersky Farm', 'Camp Belaya',
                     'Camp Samara','Nordvik Farm', 'Camp Oleksandr', 'Camp Kazan',
                     'Novosibirsk', 'Moscow', 'Jhavesk', 'Vorkuta Junction',
                    'Yekativurg', 'Firewatch Base', 'Tomsk Farm', 'St. Petersburg'],
            'medium': ['Volk military Base', 'Krovi Estate', 'Shereyavo International',
                       'Keryev', 'Zavod'],
            'hard': ['Silo 22', 'Неизвестная локация', 'Нефтяная платформа']
            }

easy = locations['easy']
medium = locations['medium']
hard = locations['hard']


#easy
#easy-farms
farm = {
        'name': 'farm', 
        'C': [350, 336, 343, 348, 351, 352, 1033, 339, 1174, 344, 345, 341],
        'U': [242, 243, 244, 484, 485, 44, 347, 490, 332, 381],
        'E': [],
        'R': [1345],
        'L': [],
        }

#easy-camp
camp = {
        'name': 'camp', 
        'C': [141, 344, 345, 1033, 342, 139, 338, 1031, 288, 289, 337, 16, 64, 106, 276, 120, 83,91,92, 357],
        'U': [346, 347, 509, 510, 511, 484, 485, 333, 503, 460, 101, 103, 1175],
        'R': [1181, 113, 1179, 1180],
        'E': [],
        'L': [],
        }


#easy-city
city = {
        'name': 'city', 
        'C': [],
        'U': [],
        'R': [],
        'E': [],
        'L': [],
        }


#medium
#medium-base
base = {
        'name': 'base', 
        'C': [],
        'U': [],
        'R': [],
        'L': [],
        'E': [],
        }


#medium-krovi
krovi = {
        'name': 'krovi', 
        'C': [],
        'U': [],
        'R': [],
        'L': [],
        }


#medium-airport
airport={
        'name': 'airport', 
        'C': [],
        'U': [],
        'R': [],
        'L': [],
        'E': [],
        }

#medium-keryev
keryev = {
        'name': 'keryev', 
        'C': [],
        'U': [],
        'R': [],
        'L': [],
        'E': [],
        }


#medium-zavod
zavod = {
        'name': 'zavod', 
        'C': [],
        'U': [],
        'R': [],
        'L': [],
        'E': [],
        }


#hard
hard = {
        'name': 'hard', 
        'C': [],
        'U': [],
        'R': [],
        'L': [],
        'E': [],
        }
