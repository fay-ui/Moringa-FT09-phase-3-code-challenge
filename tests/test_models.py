import unittest
from models.author import Author
from models.article import Article
from models.magazine import Magazine

class TestModels(unittest.TestCase):
    def test_author_creation(self):
        # Author creation should only take the name as parameter.
        author = Author("John Doe")  # Only pass the name, not an ID.
        self.assertEqual(author.name, "John Doe")

    def test_article_creation(self):
        # Assuming that Article expects the fields as shown in the model.
        article = Article(1, "Test Title", "Test Content", 1, 1)
        self.assertEqual(article.title, "Test Title")

    def test_magazine_creation(self):
        # Magazine creation should only take name and category.
        magazine = Magazine("Tech Weekly", "Technology")  # Pass name and category, not an ID.
        self.assertEqual(magazine.name, "Tech Weekly")

if __name__ == "__main__":
    unittest.main()
