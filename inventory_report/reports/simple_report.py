from datetime import datetime


class SimpleReport:
    @staticmethod
    def generate(data_list):
        manufacture_dates = [data["data_de_fabricacao"] for data in data_list]
        expiration_dates = [
            data["data_de_validade"]
            for data in data_list
            if data["data_de_validade"] > datetime.now().strftime("%Y-%m-%d")
        ]

        oldest_manufacture_date = min(manufacture_dates)
        closest_expiration_date = min(expiration_dates)

        companies = {}
        for item in data_list:
            company = item["nome_da_empresa"]
            if company in companies:
                companies[company] += 1
            else:
                companies[company] = 1
            company_with_most_products = max(companies, key=companies.get)
        return (
            f"Data de fabricação mais antiga: {oldest_manufacture_date}\n"
            f"Data de validade mais próxima: {closest_expiration_date}\n"
            f"Empresa com mais produtos: {company_with_most_products}"
        )
