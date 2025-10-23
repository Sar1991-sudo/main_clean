Children = 3
Hometown = "Lahti"

# Lista
TownsInFinland = ["Lahts", "Helsinki", "Lappeenranta", "Oulu", "Tempere"] 

RandonInforsation = ["Hira", 48, True, Children, Hometown]

print(TownsInFinland[0])
TownsInFinland.append("Rovaniemi")
print(TownsInFinland)

NunOfTowns = len(TownsInFinland) 
print(TownsInFinland[NunOfTowns - 1])

Municipalities = ["Asikkala","Hollola", "Karvia", "Kempele"]
Towns = ["Laht!", "Helsinki", "Lappeenranta", "Oulu", "Tampere"]

MunicipalityAndTowns = [Municipalities, Towns]

print(MunicipalityAndTowns[1][2])

Towns.sort()
print(Towns)

Teacher = {
    "Name": "Juha",
    "Age": 50,
    "City": "Lahti",
}

print(Teacher["Name"])

Teacher["email"]: "juha.hyytainen@lab.fi"

print(Teacher)

for Key in Teacher:
    print(key, end= ' ')
    print(Teacher[Key])

    Student = [
        {'name': 'Miko', 'age': 25, 'city': 'Lahti'},
        {'name': 'Anna', 'age': 22, 'city': 'Helsinki'},
        {'name': 'Jussi', 'age': 23, 'city': 'Oulu'}
    ]
    print(Student[0])

    Cities = {
        'Finland': ['Helsinki', 'Espoo', 'Tampere'],
        'Sweden': ['Stockholm', 'Gothenburg', 'Malmö'],
    }
    print(Cities['Finland'][0])    