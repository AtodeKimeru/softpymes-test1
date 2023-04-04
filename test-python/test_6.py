"""
  6) ordernar las compañias por nombre y dentro de cada compañia, crear un objecto 
  llamado thirds el cual va a tener todos los terceros que pertenezcan a esa compañia
"""
from data import get_companies, get_thirds


def sort_companies():
    names = list()
    for company in get_companies:
        name = company.get('name')
        names.append(name)

    


def run() -> None:
    print('a' < 'b')


if __name__ == '__main__':
    run()