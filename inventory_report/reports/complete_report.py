from inventory_report.reports.simple_report import SimpleReport


class CompleteReport(SimpleReport):
    @staticmethod
    def generate(data_list):
        report = SimpleReport.generate(data_list)

        companies = {}
        for item in data_list:
            company = item["nome_da_empresa"]
            if company in companies:
                companies[company] += 1
            else:
                companies[company] = 1

        product_counts = "\n".join([
            f"- {company}: {count}\n" for company, count in companies.items()])

        return (
            f"{report}\n"
            f"Produtos estocados por empresa:\n"
            f"{product_counts}"
        )
