"""
  4) Mostrar de los terceros que se tienen en el archivo data.py 
  los cuales no poseen ni email o no tengan cellPhone.
"""
from data import get_thirds


def incomplete_contact() -> list:
    thirds = get_thirds()
    incompletes = list()
    for third in thirds:
        if third['email'] == '':
            incompletes.append(third)
        elif third['cellPhone'] == '':
            incompletes.append(third)

    return incompletes


def run() -> None:
    for third in incomplete_contact():
        print(third)


if __name__ == '__main__':
    run()