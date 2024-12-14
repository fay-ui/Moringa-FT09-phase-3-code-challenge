from database.setup import create_tables
from database.connection import get_db_connection
from models.article import Article
from models.author import Author
from models.magazine import Magazine

def main():
    # Initialize the database and create tables
    try:
        create_tables()
        print("Tables created successfully.")
    except Exception as e:
        print(f"Error creating tables: {e}")
        return

    # Collect user input
    author_name = input("Enter author's name: ")
    magazine_name = input("Enter magazine name: ")
    magazine_category = input("Enter magazine category: ")
    article_title = input("Enter article title: ")
    article_content = input("Enter article content: ")

    # Connect to the database
    try:
        conn = get_db_connection()
        cursor = conn.cursor()
    except Exception as e:
        print(f"Error connecting to the database: {e}")
        return

    try:
        # Create an author
        cursor.execute('INSERT INTO authors (name) VALUES (?)', (author_name,))
        author_id = cursor.lastrowid  # Use this to fetch the id of the newly created author
        print(f"Author created with ID: {author_id}")

        # Create a magazine
        cursor.execute('INSERT INTO magazines (name, category) VALUES (?, ?)', (magazine_name, magazine_category))
        magazine_id = cursor.lastrowid  # Use this to fetch the id of the newly created magazine
        print(f"Magazine created with ID: {magazine_id}")

        # Create an article
        cursor.execute('INSERT INTO articles (title, content, author_id, magazine_id) VALUES (?, ?, ?, ?)',
                       (article_title, article_content, author_id, magazine_id))
        print("Article created successfully.")

        # Commit changes to the database
        conn.commit()

    except Exception as e:
        print(f"Error inserting data into database: {e}")
        conn.rollback()  # Rollback in case of an error
        return
    finally:
        conn.close()

    # Query the database for inserted records and print them
    try:
        conn = get_db_connection()
        cursor = conn.cursor()

        cursor.execute('SELECT * FROM magazines')
        magazines = cursor.fetchall()

        cursor.execute('SELECT * FROM authors')
        authors = cursor.fetchall()

        cursor.execute('SELECT * FROM articles')
        articles = cursor.fetchall()

        # Close the connection
        conn.close()

        # Display results
        print("\nMagazines:")
        for magazine in magazines:
            # Print Magazines with their respective IDs, names, and categories
            # Since `fetchall()` returns tuples, you need to reference by index or make it a dictionary
            print(Magazine(magazine[0], magazine[1], magazine[2]))  # Using indexes (id, name, category)

        print("\nAuthors:")
        for author in authors:
            # Display author information (id, name)
            print(Author(author[0], author[1]))  # Using indexes (id, name)

        print("\nArticles:")
        for article in articles:
            # Display article information (id, title, content, author_id, magazine_id)
            print(Article(article[0], article[1], article[2], article[3], article[4]))  # Using indexes

    except Exception as e:
        print(f"Error querying the database: {e}")


if __name__ == "__main__":
    main()
