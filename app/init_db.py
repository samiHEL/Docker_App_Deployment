import mysql.connector
from mysql.connector import Error

def create_connection():
    try:
        connection = mysql.connector.connect(
            host='db',
            user='root',
            password='root',
            database='devopsroles',
            port='3306'
        )
        return connection
    except Error as e:
        print(f"Error: {e}")
        return None

def execute_query(connection, query):
    try:
        cursor = connection.cursor()
        cursor.execute(query)
        connection.commit()
        cursor.close()
    except Error as e:
        print(f"Error: {e}")

def main():
    create_table_query = """
    CREATE TABLE IF NOT EXISTS test_table (
        login VARCHAR(20),
        mdp VARCHAR(20)
    );

    INSERT INTO test_table (login, mdp) VALUES ('admin', 'admin'), ('user', 'user');
    """

    connection = create_connection()
    if connection:
        execute_query(connection, create_table_query)
        connection.close()

if __name__ == '__main__':
    main()