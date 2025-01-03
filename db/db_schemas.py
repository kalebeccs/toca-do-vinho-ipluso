TABLES = {
    "Users": """
        CREATE TABLE IF NOT EXISTS Users (
            pk_user INTEGER PRIMARY KEY,
            name TEXT NOT NULL,
            email TEXT NOT NULL,
            password_hash TEXT NOT NULL,
            dob DATE NOT NULL,
            vat_number TEXT,
            address_1 TEXT,
            address_2 TEXT,
            role TEXT CHECK(role IN ('user', 'admin')) NOT NULL,
            created_at DATETIME DEFAULT CURRENT_TIMESTAMP,
            updated_at DATETIME DEFAULT CURRENT_TIMESTAMP,
            UNIQUE(email)
        );
    """,
    "Wines": """
        CREATE TABLE IF NOT EXISTS Wines (
            pk_wine INTEGER PRIMARY KEY,
            brand TEXT NOT NULL, 
            name TEXT NOT NULL,
            type TEXT NOT NULL,
            alcohol REAL NOT NULL,
            year INTEGER NOT NULL,
            country_of_origin TEXT NOT NULL,
            region TEXT,
            description TEXT,
            added_at DATETIME DEFAULT CURRENT_TIMESTAMP,
            updated_at DATETIME DEFAULT CURRENT_TIMESTAMP,
            active BOOLEAN DEFAULT TRUE
        );
    """,
    "Stock": """
        CREATE TABLE IF NOT EXISTS Stock (
            pk_stock INTEGER PRIMARY KEY,
            fk_wine INTEGER NOT NULL,
            movement_date DATETIME DEFAULT CURRENT_TIMESTAMP,
            movement_type TEXT CHECK(movement_type IN ('purchase', 'sale', 'adjustment')) NOT NULL,
            quantity INTEGER NOT NULL,
            fk_user INTEGER,
            reason TEXT,
            FOREIGN KEY(fk_wine) REFERENCES Wine(pk_wine),
            FOREIGN KEY(fk_user) REFERENCES Users(pk_user)
        );
    """,
    "Prices": """
        CREATE TABLE IF NOT EXISTS Prices (
            pk_price INTEGER PRIMARY KEY,
            fk_wine INTEGER NOT NULL,
            price_type TEXT CHECK(price_type IN ('purchase', 'sale')) NOT NULL,
            price REAL NOT NULL,
            effective_date DATETIME DEFAULT CURRENT_TIMESTAMP,
            FOREIGN KEY(fk_wine) REFERENCES Wines(pk_wine)
        );
    """,
    "Purchases": """
        CREATE TABLE IF NOT EXISTS Purchases (
            pk_purchase INTEGER PRIMARY KEY,
            fk_user INTEGER NOT NULL,
            purchase_date DATETIME DEFAULT CURRENT_TIMESTAMP,
            total_value REAL NOT NULL,
            FOREIGN KEY(fk_user) REFERENCES Users(pk_user)
        );
    """,
    "Purchase_Items": """
        CREATE TABLE IF NOT EXISTS Purchase_Items (
            pk_item INTEGER PRIMARY KEY,
            fk_purchase INTEGER NOT NULL,
            fk_wine INTEGER NOT NULL,
            quantity INTEGER NOT NULL,
            unit_price REAL NOT NULL,
            FOREIGN KEY(fk_purchase) REFERENCES Purchases(pk_purchase),
            FOREIGN KEY(fk_wine) REFERENCES Wines(pk_wine)
        );
    """
}
