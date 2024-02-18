BOOKS_DATABASE = [
    {
        "id_": 1,
        "name": "test_name_1",
        "pages": 200,
    },
    {
        "id_": 2,
        "name": "test_name_2",
        "pages": 400,
    }
]
#
# class Book:
#     def __init__(self, id_, name, pages):
#         self.id_ = id_
#         self.name = name
#         self.pages = pages
# #
# class Library:
#     def __init__(self, books=[]):
#         self.books = books
#
#     def get_next_book_id(self):
#         if len(self.books) == 0:
#             return 1
#         else:
#             return self.books[-1].id_ + 1
#
#     def get_index_by_book_id(self, id_):
#         for i in range(len(self.books)):
#             if self.books[i].id_ == id_:
#                 return i
#         raise ValueError("Книги с запрашиваемым id не существует")
#
# if __name__ == '__main__':
#     empty_library = Library()
#     print(empty_library.get_next_book_id())
#
#     # Пример использования класса Book и добавление новых книг в библиотеку
#     b1 = Book(1, "Book 1", 100)
#     b2 = Book(2, "Book 2", 200)
#     library = Library([b1, b2])
#     print(library.get_next_book_id_())
#     print(library.get_index_by_book_id_(1))

# version № 2

class Library:
    def __init__(self, books=None):
        if books is None:
            books = []
        self.books = books

    def get_next_book_id(self):
        if len(self.books) == 0:
            return 1
        else:
            return self.books[-1]['id'] + 1

    def get_index_by_book_id(self, id_):
        for i, book in enumerate(self.books):
            if book['id'] == id_:
                return i
        raise ValueError("Книги с запрашиваемым id не существует")


if __name__ == '__main__':
    empty_library = Library()
    print(empty_library.get_next_book_id())

    # Пример использования класса Library
    books_database = [
        {
            "id": 1,
            "name": "Book 1",
            "author": "Author 1"
        },
        {
            "id": 2,
            "name": "Book 2",
            "author": "Author 2"
        }
    ]

    library = Library(books_database)
    print(library.get_next_book_id())
    print(library.get_index_by_book_id(2))
