import json
import os

file_path = "books.json"


class Book:
    def __init__(self, title, author, year):
        self.id = self.generate_unique_id()
        self.title = title
        self.author = author
        self.year = year
        self.status = "в наличии"

    def generate_unique_id(self):
        if os.path.exists(file_path):
            with open(file_path, 'r', encoding='utf-8') as file:
                books = json.load(file)
                return max([book['id'] for book in books]) + 1
        return 1  
    
    def to_dict(self):
        return {
            'id': self.id,
            'title': self.title,
            'author': self.author,
            'year': self.year,
            'status': self.status
        }
    

class LibraryManager:
    def __init__(self):
        self.file_path = file_path

    def load_books(self):
        if os.path.exists(self.file_path):
            with open(self.file_path, 'r', encoding='utf-8') as file:
                books = json.load(file)
                return books
        return []
        
    def save_books(self, books):
        with open(self.file_path, 'w', encoding='utf-8') as file:
            json.dump(books, file, ensure_ascii=False, indent=4)

    def add_book(self, title, author, year):
        books = self.load_books()
        new_book = Book(title, author, year)
        books.append(new_book.to_dict())
        self.save_books(books)        

    def delete_books(self, book_id):
        books = self.load_books()
        updated_books = [book for book in books if str(book['id']) != book_id]
        if len(books) == len(updated_books):
            return False
        self.save_books(updated_books)
        return True
    
    def search_books(self, field, query):
        books = self.load_books()
        return [book for book in books if str(book[field]).lower() == query.lower()]
    
    def display_books(self):
        books = self.load_books()
        for book in books:
                print(f"ID: {book['id']}, Название: {book['title']}, Автор: {book['author']}, Год издания: {book['year']}, Статус: {book['status']}")
        
        
    def change_status_book(self, book_id, new_status):
        books = self.load_books()
        for book in books:
            if book['id'] == book_id:
                book['status'] = new_status
                self.save_books(books)
                return True
        return False    
    
