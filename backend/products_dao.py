from sql_connection import get_sql_connection

def get_all_products(connection):
    cursor = connection.cursor()
    query = """
        SELECT products.product_id, products.name, products.uom_id, 
               products.price_per_unit, uom.uom_name 
        FROM products 
        INNER JOIN uom ON products.uom_id=uom.uom_id
    """
    cursor.execute(query)
    response = []
    for row in cursor:
        response.append({
            'product_id': row['product_id'],
            'name': row['name'],
            'uom_id': row['uom_id'],
            'price_per_unit': row['price_per_unit'],
            'uom_name': row['uom_name']
        })
    return response

def insert_new_product(connection, product):
    cursor = connection.cursor()
    query = """
        INSERT INTO products (name, uom_id, price_per_unit)
        VALUES (?, ?, ?)
    """
    data = (product['product_name'], product['uom_id'], product['price_per_unit'])
    
    cursor.execute(query, data)
    connection.commit()
    
    return cursor.lastrowid

def delete_product(connection, product_id):
    cursor = connection.cursor()
    query = "DELETE FROM products WHERE product_id=?"
    cursor.execute(query, (product_id,))
    connection.commit()
    
    return cursor.lastrowid

if __name__ == '__main__':
    connection = get_sql_connection()
    # print(get_all_products(connection))
    print(insert_new_product(connection, {
        'product_name': 'potatoes',
        'uom_id': '1',
        'price_per_unit': 10
    }))