"""
  2) teniendo en cuenta el punto 1, cree una función que permita
  consultar las sucursales, debe hacerse el mismo procedimiento
  que se realizó en el punto 1, pero, utilizando la función creada
"""
from dataclasses import dataclass
from data import get_companies, get_branches


class Companies:
	@dataclass
	class Company:
		company: dict
		branches: list


	def __branches_by_company(self, companies: list, branches: list) -> list:
		companies_with_branches = list()

		for company in companies:
			branches_id = company.get('branches')
			company_branches = list()

			for id in branches_id:
				company_branches.append(branches[id - 1])
				
			company_with_branches = self.Company(company, company_branches)
			companies_with_branches.append(company_with_branches)

		return companies_with_branches


	def __init__(self, companies: list, branches: list) -> None:
		self.companies = self.__branches_by_company(companies, branches)
		self.branches = branches
			

	def get_branches(self, company_id: int = None, company_name: str = None) -> list:
		branches = self.branches

		if company_id != None:
			company = self.companies[company_id - 1]
			branches = company.branches
		
		elif company_name != None:
			for company in self.companies:
				name = company.company.get('name')
				if name.lower() == company_name.lower():
					branches = company.branches
					
		return branches


def run() -> None:
	data_companies = get_companies()
	data_branches = get_branches()
	companies = Companies(data_companies, data_branches)
	
	for branch in companies.get_branches():
		print(branch)


if __name__ == '__main__':
	run()