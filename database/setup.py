from .connection import get_db_connection

def create_tables():
    try:
        # Get the database connection
        conn = get_db_connection()
        cursor = conn.cursor()
        
        # Enable foreign key support in SQLite
        cursor.execute('PRAGMA foreign_keys = ON')

        # Create authors table
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS authors (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT NOT NULL
            )
        ''')

        # Create magazines table
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS magazines (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT NOT NULL,
                category TEXT NOT NULL
            )
        ''')

        # Create articles table with foreign key references
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS articles (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                title TEXT NOT NULL,
                content TEXT NOT NULL,
                author_id INTEGER,
                magazine_id INTEGER,
                FOREIGN KEY (author_id) REFERENCES authors (id),
                FOREIGN KEY (magazine_id) REFERENCES magazines (id)
            )
        ''')

        # Commit changes and close the connection
        conn.commit()
        print("Tables created successfully.")
        
    except Exception as e:
        print(f"Error creating tables: {e}")
    
    finally:
        # Ensure the connection is closed, even if an error occurs
        if conn:
            conn.close()
