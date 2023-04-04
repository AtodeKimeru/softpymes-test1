"""
  3) ordenar los terceros que se tienen en el archivo data.py 
  por nombre, para obtener el nombre correcto se debe tener en 
  cuenta la siguiente validación:
  
  si el tercero tiene un (tradename != '') entonces se muestra este valor, 
  en caso contrario se debe obtener concatenando los siguientes 
  campos: (firstname, lastname, maidenname) en el orden dado
"""

from data import get_thirds


def sort_thirds(print_names=False) -> list:
    """sort by names;
    if print_names is True, print the names sorted
    """
    thirds = get_thirds()
    names = list()
    for third in thirds:
        if third['tradename'] != '':
            names.append(third['tradename'])
        else:
            first = third.get('firstname')
            last = third.get('lastname')
            maiden = third.get('maidenname')
            names.append(first + ' ' + last + ' ' + maiden)

    thirds_with_names = {names[i]: thirds[i] for i in range(len(thirds))}
    
    sorted_thirds = list()
    names.sort()
    for name in names:
        third = thirds_with_names[name]
        sorted_thirds.append(third)

    if print_names == True:
        for name in names:
            print(name)

    return sorted_thirds


def run():
    also_names = bool(input('Si deseas imprimir también los nombres \
ordenados escribe "y": '))

    for third in sort_thirds(print_names=also_names):
        print('-'*50, '\n', third)


if __name__ == '__main__':
    run()