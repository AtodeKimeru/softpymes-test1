from dataclasses import dataclass
from data import get_companies, get_branches


""" 
	1) consulte la información del archivo data.py
	cree un objeto que contenga las empresas y dentro 
	las sucursales que corresponden para cada empresa
"""

@dataclass
class Companies:
	companies: list
	branches: list


def run():
	data_companies = get_companies()
	data_branches = get_branches()
	companies = Companies(data_companies, data_branches)


if __name__ == '__main__':
	run()