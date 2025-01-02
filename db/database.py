import sqlite3
from db.db_schemas import TABLES

def create_tables(database_name="wine_store.db"):
    """Create tables in the SQLite database."""
    connection = sqlite3.connect(database_name)
    cursor = connection.cursor()

    for table_name, columns in TABLES.items():
        # Building the CREATE TABLE SQL statement
        columns_sql = []
        for column_name, column_type in columns.items():
            if column_name.startswith("FOREIGN_KEY"):
                columns_sql.append(f"FOREIGN KEY {column_type}")
            elif column_name == "FOREIGN_KEYS":
                columns_sql.extend([f"FOREIGN KEY {fk}" for fk in column_type])
            else:
                columns_sql.append(f"{column_name} {column_type}")
        
        create_table_sql = f"""
        CREATE TABLE IF NOT EXISTS {table_name} (
            {', '.join(columns_sql)}
        );
        """
        cursor.execute(create_table_sql)

    connection.commit()
    connection.close()

create_tables()