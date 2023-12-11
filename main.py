from menu import products
from management.product_handler import (
    get_product_by_id,
    get_products_by_type,
    add_product,
    menu_report,
)
from management.tab_handler import calculate_tab

if __name__ == "__main__":
    product_id = 28
    print(get_product_by_id(product_id))
    product_id_invalid = 999
    print(get_product_by_id(product_id_invalid))

    product_type = "drink"
    print(get_products_by_type(product_type))
    product_type_invalid = "invalid_type"
    print(get_products_by_type(product_type_invalid))

    new_product = {
        "title": "X-Python",
        "price": 5.0,
        "rating": 5,
        "description": "Sanduiche de Python",
        "type": "fast-food",
    }
    print(add_product(products, **new_product))
    print(add_product([], **new_product))

    table_1 = [{"_id": 1, "amount": 5}, {"_id": 19, "amount": 5}]
    table_2 = [
        {"_id": 10, "amount": 3},
        {"_id": 20, "amount": 2},
        {"_id": 21, "amount": 5},
    ]
    print(calculate_tab(table_1))
    print(calculate_tab(table_2))

    report = menu_report()
    print(report)
