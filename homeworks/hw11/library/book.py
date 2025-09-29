class Book:
    def __init__(self, book_name, author, num_pages, isbn):
        self.book_name = book_name
        self.author = author
        self.num_pages = num_pages
        self.isbn = isbn
        self.is_reserved = False
        self.is_borrowed = False
        self.borrowed_by = None

    def reserve(self, reader):
        if self.is_reserved or self.is_borrowed:
            print(f"Книга '{self.book_name}' недоступна для резервирования.")
            return False
        self.is_reserved = True
        self.borrowed_by = reader
        print(f"{reader.name} зарезервировал книгу '{self.book_name}'.")
        return True

    def cancel_reserve(self, reader):
        if not self.is_reserved or self.borrowed_by != reader:
            print(f"{reader.name} не может отменить резервирование книги '{self.book_name}'.")
            return False
        self.is_reserved = False
        self.borrowed_by = None
        print(f"{reader.name} отменил резервирование книги '{self.book_name}'.")
        return True

    def get_book(self, reader):
        if self.is_reserved and self.borrowed_by != reader:
            print(f"Книга '{self.book_name}' уже зарезервирована другим пользователем.")
            return False
        if self.is_borrowed:
            print(f"Книга '{self.book_name}' уже выдана.")
            return False
        self.is_borrowed = True
        self.is_reserved = False
        self.borrowed_by = reader
        print(f"{reader.name} получил книгу '{self.book_name}'.")
        return True

    def return_book(self, reader):
        if not self.is_borrowed or self.borrowed_by != reader:
            print(f"{reader.name} не может вернуть книгу '{self.book_name}', "
                  f"так как она не была выдана ему.")
            return False
        self.is_borrowed = False
        self.borrowed_by = None
        print(f"{reader.name} вернул книгу '{self.book_name}'.")
        return True
