from dataclasses import dataclass
from data import get_companies, get_branches


"""
  2) teniendo en cuenta el punto 1, cree una función que permita
  consultar las sucursales, debe hacerse el mismo procedimiento
  que se realizó en el punto 1, pero, utilizando la función creada
"""


@dataclass
class Companies:
	companies: list
	branches: list


	def get_branches(self) -> list:
		return self.branches


def run():
	data_companies = get_companies()
	data_branches = get_branches()
	companies = Companies(data_companies, data_branches)
	for branch in companies.get_branches():
		print(branch)


if __name__ == '__main__':
	run()