import logging
from db.database import execute_query, fetch_all_from_table, fetch_query
from src.utils import hash_password

def insert_user(user):
    """
    Insert a user into the database
    :param user: user dictionary
    :return: None
    """
    password_hash = hash_password(user['password'])
    execute_query("""
                INSERT INTO Users (name, email, password_hash, dob, role)
                VALUES (?, ?, ?, ?, ?)
                """, 
                (user['name'], 
                 user['email'], 
                 password_hash, 
                 user['dob'], 
                 user['role']))
    logging.info(f"User {user['name']} inserted into the database")

def insert_users(users):
    """
    Insert users into the database
    :param users: list of users
    :return: None
    """
    for user in users:
        password_hash = hash_password(user['password'])
        execute_query("INSERT INTO Users (name, email, password_hash, dob,vat_number, address_1, role) VALUES (?, ?, ?, ?, ?, ?, ?)", 
                    (user['name'], 
                     user['email'], 
                     password_hash, 
                     user['dob'], 
                     user['vat_number'],
                     user['address_1'],
                     user['role']))
    logging.info(f"{len(users)} users inserted into the database")

def get_users():
    """
    Get all users from the database
    :return: list of users
    """
    return fetch_all_from_table('Users')

def get_user_by_email(email):
    """
    Get a user by email
    :param email: user email
    :return: user dictionary
    """
    return fetch_query("""
                    SELECT * FROM Users
                    WHERE email = ?
                    """, 
                    (email,), 
                    fetch_one=True)
    
def get_user_by_id(user_id):
    """
    Get a user by id
    :param user_id: user id
    :return: user dictionary
    """
    return fetch_query("""
                    SELECT * FROM Users
                    WHERE pk_user = ?
                    """, 
                    (user_id,), 
                    fetch_one=True)
    
def update_user(user_id, user):
    """
    Update a user
    :param user_id: user id
    :param user: user dictionary
    :return: None
    """
    execute_query("""
                UPDATE Users
                SET name = ?, email = ?, dob = ?, vat_number = ?, address_1 = ?, address_2 = ?
                WHERE pk_user = ?
                """, 
                (user['name'], 
                 user['email'], 
                 user['dob'], 
                 user['vat_number'],
                 user['address_1'],
                 user['address_2'], 
                 user_id))
    logging.info(f"User {user['name']} updated")
    
def delete_user(user_id):
    """
    Delete a user
    :param user_id: user id
    :return: None
    """
    execute_query("""
                DELETE FROM Users
                WHERE pk_user = ?
                """, 
                (user_id,))
    logging.info(f"User {user_id} deleted")
