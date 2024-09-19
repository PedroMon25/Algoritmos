'''
Programa que calcula la edad de un perro y un gato con respecto a los años humanos
'''


def human_years_cat_years_dog_years(humanYears):
    # Calcular los años de gatos y perros
    if humanYears == 1:
        catYears = 15
        dogYears = 15
    elif humanYears == 2:
        catYears = 15 + 9
        dogYears = 15 + 9
    else:
        catYears = 15 + 9 + (humanYears - 2) * 4
        dogYears = 15 + 9 + (humanYears - 2) * 5

    return {
        'humanYears': humanYears,
        'catYears': catYears,
        'dogYears': dogYears,
    }

