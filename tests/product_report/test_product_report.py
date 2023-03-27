from inventory_report.inventory.product import Product


def test_relatorio_produto():
    product = Product(
        id=1,
        nome_do_produto="farinha",
        nome_da_empresa="Farinini",
        data_de_fabricacao="01-05-2021",
        data_de_validade="02-06-2023",
        numero_de_serie="ASBCD",
        instrucoes_de_armazenamento="ao abrigo de luz"

    )

    assert str(product) == (
        "O produto farinha fabricado em 01-05-2021 por Farinini com "
        "validade até 02-06-2023 precisa ser armazenado ao abrigo de luz."
    )
