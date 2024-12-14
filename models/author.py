import sqlite3

class Author:
    def __init__(self, name):
        self._id = None  # ID will be set once the author is saved to DB
        self.name = name  # This will also call the setter for name, which validates it
        self._create_author()  # Create the author record in the database

    def _create_author(self):
        try:
            # Connect to the database and insert the author record
            connection = sqlite3.connect('magazine.db')
            cursor = connection.cursor()
            
            # Ensure the name is valid before inserting
            cursor.execute('INSERT INTO authors (name) VALUES (?)', (self.name,))
            connection.commit()
            
            self._id = cursor.lastrowid  # Get the ID of the newly created author
            print(f"Author created with ID: {self._id}")  # Debugging output

        except sqlite3.Error as e:
            print(f"Database error: {e}")
            connection.rollback()  # Rollback in case of an error
        finally:
            connection.close()

    @property
    def id(self):
        return self._id

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        # Name cannot be changed once it's set
        if hasattr(self, '_name'):
            raise AttributeError("Name cannot be changed once set.")
        if not value:
            raise ValueError("Name must not be empty.")
        if len(value) < 2 or len(value) > 16:
            raise ValueError("Name must be between 2 and 16 characters.")
        self._name = value

    def __repr__(self):
        return f'<Author id={self.id}, name={self.name}>'
