import pytest


@pytest.fixture
def clear_book_database():
    print("FIXTURE: clearing book database")

@pytest.fixture
def fill_books_database():
    print("FIXTURE: filling books database")

@pytest.mark.usefixtures("clear_book_database, fill_books_database")
class TestLibrary:

    def test_read_book_from_library(self):
        ...
    def test_delete_book_from_library(self):
        ...