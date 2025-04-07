import psycopg2
from psycopg2 import sql

# Define connection parameters
connection_params = {
    'dbname': 'photon',
    'user': 'student',
    'password': 'student',  
    'host': 'localhost',    
    'port': '5432'         
}

try:
    # Connect to PostgreSQL
    conn = psycopg2.connect(**connection_params)
    cursor = conn.cursor()

    cursor.execute("SELECT version();")
    version = cursor.fetchone()
    print(f"Connected to - {version}")

    # Delete every player except for the one with id = 1 and codename = 'Opus'
    cursor.execute('''
        DELETE FROM players 
        WHERE NOT (id = 1 AND codename = 'Opus');
    ''')

    # Commit the changes
    conn.commit()
    print("All players except for 1:Opus have been deleted.")

    cursor.execute("SELECT * FROM players;")
    rows = cursor.fetchall()
    for row in rows:
        print(row)

except Exception as error:
    print(f"Error connecting to PostgreSQL database: {error}")

finally:
    # Close the cursor and connection
    if cursor:
        cursor.close()
    if conn:
        conn.close()
