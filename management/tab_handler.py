from . import product_handler


def calculate_tab(table):
    subtotal = 0.0

    for item in table:
        if '_id' in item and 'amount' in item:
            product = product_handler.get_product_by_id(item['_id'])
            if product:
                subtotal += product['price'] * item['amount']

    formatted_subtotal = f"${round(subtotal, 2):.2f}"
    return {'subtotal': formatted_subtotal}
