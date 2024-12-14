import sqlite3

class Magazine:
    def __init__(self, name, category):
        self._id = None  # Will be set once saved to DB
        self.name = name  # Will call setter for name validation
        self.category = category  # Will call setter for category validation

    def _create_magazine(self):
        """Create the magazine record in the database"""
        connection = None
        try:
            # Connect to the database and insert the magazine record
            connection = sqlite3.connect('magazine.db')
            cursor = connection.cursor()

            cursor.execute('INSERT INTO magazines (name, category) VALUES (?, ?)', (self.name, self.category))
            connection.commit()
            self._id = cursor.lastrowid  # Get the ID of the newly created magazine

        except sqlite3.Error as e:
            print(f"Error inserting into database: {e}")
            if connection:
                connection.rollback()  # Ensure the transaction is rolled back in case of failure

        finally:
            if connection:
                connection.close()  # Close the connection in the finally block to ensure it's closed properly

    @property
    def id(self):
        return self._id

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        if hasattr(self, '_name'):  # Ensures name is immutable after being set
            raise AttributeError("Name cannot be changed once set.")
        if not value or len(value) < 2 or len(value) > 16:
            raise ValueError("Name must be between 2 and 16 characters.")
        self._name = value

    @property
    def category(self):
        return self._category

    @category.setter
    def category(self, value):
        if not value:
            raise ValueError("Category cannot be empty.")
        if hasattr(self, '_category'):  # Make category immutable after being set
            raise AttributeError("Category cannot be changed once set.")
        self._category = value

    def __repr__(self):
        return f'<Magazine {self.name}>'

    def save(self):
        """Call this method to insert the magazine into the database."""
        self._create_magazine()

