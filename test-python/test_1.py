""" 
	1) consulte la información del archivo data.py
	cree un objeto que contenga las empresas y dentro 
	las sucursales que corresponden para cada empresa
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
			

def run() -> None:
	data_companies = get_companies()
	data_branches = get_branches()
	companies = Companies(data_companies, data_branches)

	print(companies)
	for company in companies.companies:
		print('-'*80 + '\n', company)


if __name__ == '__main__':
	run()