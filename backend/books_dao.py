from sql_connector import sql_connection


def get_books_details(connection):
    cursor = connection.cursor()
    query = "SELECT * FROM library_details.details;"
    cursor.execute(query)
    details = []

    for (book_id, book_name, pages, cost) in cursor:
        details.append(
            {
                'book_id': book_id,
                'book_name': book_name,
                'pages': pages,
                'cost': cost
            }
        )

    print(details)
    connection.close()


def insert_new_book(connection, book_name, pages, cost):
    cursor = connection.cursor()
    query = ("INSERT INTO details "
             "(book_name, pages, cost) "
             "VALUES (%s, %s, %s)")
    data = (book_name, str(pages), str(cost))
    cursor.execute(query, data)
    connection.commit()
    return cursor.lastrowid


def delete_product(connection, book_id):
    cursor = connection.cursor()
    query = ("DELETE FROM details where book_id=" + str(book_id))
    cursor.execute(query)
    connection.commit()
    return cursor.lastrowid


if __name__ == '__main__':
    connection = sql_connection()
    print(insert_new_book(connection, 'DBMS', '100', '99'))
    delete_product(connection, 6)
