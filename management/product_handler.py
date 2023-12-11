import menu


def get_product_by_id(product_id):
    if type(product_id) is not int:
        raise TypeError("product id must be an int")

    for product in menu.products:
        if product.get('_id') == product_id:
            return product
    return {}


def get_products_by_type(product_type):
    if type(product_type) is not str:
        raise TypeError("product type must be a str")

    products_of_type = []
    for product in menu.products:
        if product['type'] == product_type:
            products_of_type.append(product)
    return products_of_type


def add_product(menu, **kwargs):
    new_product = kwargs
    if not menu:
        new_product['_id'] = 1
    else:
        max_id = max(menu, key=get_id)
        new_product['_id'] = max_id['_id'] + 1
    menu.append(new_product)
    return new_product


def get_id(product):
    return product['_id']


def menu_report():
    product_count = len(menu.products)

    if product_count == 0:
        average_price = 0.0
        most_common_type = "N/A"
    else:
        total_price = sum(product['price'] for product in menu.products)
        average_price = round(total_price / product_count, 2)
        product_type_counts = {}
        for product in menu.products:
            product_type = product['type']
            if product_type in product_type_counts:
                product_type_counts[product_type] += 1
            else:
                product_type_counts[product_type] = 1
        most_common_type = max(product_type_counts, key=product_type_counts.get)

    report = (
        f"Products Count: {product_count} - Average Price: ${average_price} "
        f"- Most Common Type: {most_common_type}"
    )
    return report
