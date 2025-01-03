import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

from db.database import initialize_db
from seed_data import USERS, WINES, STOCK, PRICES, PURCHASES,PURCHASE_ITEMS
from src.models.users import insert_users

def seed_db():
    """
    Seed the database with initial data.
    :return: None
    """
    try:
        insert_users(USERS)
        
        logging.info("Database seeded with initial data")
    except Exception as e:
        logging.error(f"Error inserting users: {e}")
        raise
    
if __name__ == '__main__':
    logging.info("Initializing database...")
    initialize_db()
    
    logging.info("Seeding database...")
    seed_db()
