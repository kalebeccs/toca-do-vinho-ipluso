TABLES = {
    "Users": {
        "id": "INTEGER PRIMARY KEY AUTOINCREMENT",
        "name": "TEXT NOT NULL",
        "dob": "DATE",
        "vat_number": "TEXT",
        "address_1": "TEXT NOT NULL",
        "address_2": "TEXT",
        "email": "TEXT UNIQUE NOT NULL",
        "password_hash": "TEXT NOT NULL",
        "role": "TEXT CHECK(role IN ('user', 'admin')) NOT NULL",
        "created_at": "DATETIME DEFAULT CURRENT_TIMESTAMP"
    },
    "Wines": {
        "id": "INTEGER PRIMARY KEY AUTOINCREMENT",
        "name": "TEXT NOT NULL",
        "type": "TEXT NOT NULL",
        "alcohol": "REAL",
        "year": "INTEGER NOT NULL",
        "country_of_origin": "TEXT NOT NULL",
        "price": "REAL NOT NULL",
        "stock": "INTEGER NOT NULL",
        "description": "TEXT",
        "added_at": "DATETIME DEFAULT CURRENT_TIMESTAMP"
    },
    "Purchases": {
        "id": "INTEGER PRIMARY KEY AUTOINCREMENT",
        "user_id": "INTEGER NOT NULL",
        "purchase_date": "DATETIME DEFAULT CURRENT_TIMESTAMP",
        "total_value": "REAL NOT NULL",
        "FOREIGN_KEY": "user_id REFERENCES Users(id)"
    },
    "Purchase_Items": {
        "id": "INTEGER PRIMARY KEY AUTOINCREMENT",
        "purchase_id": "INTEGER NOT NULL",
        "wine_id": "INTEGER NOT NULL",
        "quantity": "INTEGER NOT NULL",
        "unit_price": "REAL NOT NULL",
        "FOREIGN_KEYS": [
            "purchase_id REFERENCES Purchases(id)",
            "wine_id REFERENCES Wines(id)"
        ]
    }
}
