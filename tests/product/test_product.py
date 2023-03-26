from inventory_report.inventory.product import Product


def test_cria_produto():
    product = Product(
        id=1,
        nome_do_produto="Products test",
        nome_da_empresa="Company test",
        data_de_fabricacao="01/01/2023",
        data_de_validade="01/01/2024",
        numero_de_serie="FR48",
        instrucoes_de_armazenamento="Store in a dry place",
    )

    assert product.id == 1
    assert product.nome_do_produto == "Products test"
    assert product.nome_da_empresa == "Company test"
    assert product.data_de_fabricacao == "01/01/2023"
    assert product.data_de_validade == "01/01/2024"
    assert product.numero_de_serie == "FR48"
    assert product.instrucoes_de_armazenamento == "Store in a dry place"
