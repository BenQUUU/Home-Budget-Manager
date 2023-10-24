class Repository:
    def __init__(self, connection):
        self.connection = connection

    def add_item(self, name: str, category: str, date: str, value: float):
        category_id = self.get_or_create_category(category)
        sql = 'INSERT INTO items VALUES(null, ?, ?, ?, ?)'
        db_cursor = self.connection.cursor()
        db_cursor.execute(sql, (name, category_id, value, date))
        self.connection.commit()

    def get_or_create_category(self, name: str) -> int:
        db_cursor = self.connection.cursor()
        db_cursor.execute('SELECT id FROM categories WHERE name=?', (name,))
        result = db_cursor.fetchone()
        if result is None:
            db_cursor.execute('INSERT INTO categories VALUES(null, ?)', (name,))
            self.connection.commit()
            category_id = db_cursor.lastrowid
        else:
            category_id = result[0]

        return category_id

    def delete_item(self, item_id):
        db_cursor = self.connection.cursor()
        db_cursor.execute('DELETE FROM items WHERE id=?', (item_id,))
        self.connection.commit()

    def get_items(self) -> tuple:
        db_cursor = self.connection.cursor()
        return db_cursor.execute('SELECT * FROM items')

    def get_stats(self) -> tuple:
        db_cursor = self.connection.cursor()
        return db_cursor.execute('''SELECT strftime('%m', date) as month, SUM(amount) as total
        FROM items
        GROUP BY month, category_id''')
