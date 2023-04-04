"""
  5) ordenar los terceros que se tienen en el archivo data.py por nombre y 
  agregar dentro de cada tercero una propiedad que muestre la compañia a la que pertenece
"""

from data import get_companies
from test_3 import sort_thirds


def add_property(data: dict, property: str, value: str='') -> None:
    """modify dictionary original adding one property in what his default value is ''"""
    aux = dict()
    aux[property] = value
    data.update(**aux)


def company_name(third: dict) -> str:
    companies = get_companies()
    id = int(third.get('companyid'))
    try:
        name = companies[id - 1].get('name')
    except IndexError:
        raise IndexError('company id not found')

    return name


def run() -> None:
    thirds = sort_thirds()

    for third in thirds:
        try:
            company = company_name(third)
            add_property(third, 'company', value=company)
        except IndexError:
            add_property(third, 'company')
        print(third)


if __name__ == '__main__':
    run()