from library_manager import LibraryManager


def main():
    library_manager = LibraryManager()

    while True:
        print("\nДобро пожаловать в Систему Управления Библиотекой. Ниже представлены команды, с помощью которых вы можете взаимодействовать с нашей библиотекой. Чтобы воспользоваться ими, укажите цифру нужной команды:")
        print("1.Добавить книгу", "2.Удалить книгу", "3.Найти книгу", "4.Отобразить все книги", "5.Поменять статус книги", "6.Выйти", sep='\n')

        answer = input("Выберите команду: ")

        if answer == '1':
            title = input("Введите название книги:")
            author = input("Введите автора книги:")
            year = input("Введите год издание книги:")
            library_manager.add_book(title, author, year)
            print("Книга была успешно добавлена!")

        elif answer == '2':
            book_id = input('Введите "ID" книги, который хотите удалить: ')
            if library_manager.delete_books(book_id):
                print("Книга была удалена успешно!")
            else:
                print("Данной книги нет у нас в библиотеке")

        elif answer == '3':
            field = input("Введите по какому критерию нужно найти книгу (Подсказка: по id, названию, году): ")
            query = input("Введие значение, по которому вы хотите найти книгу: ")
            result = library_manager.search_books(field, query)
            if result:
                for book in result:
                    print("Книга была найдена!")
                    print(f"ID: {book['id']}, Название: {book['author']}, Год: {book['year']}, Статус: {book['status']}")
            else:
                print("Книга не найдена!")

        elif answer == '4':
            library_manager.display_books()

        elif answer == '5':
            book_id = int(input("Введите ID книги: "))
            new_status = input("Введите новый статус книги(Подсказка: в наличии/выдана): ")
            if library_manager.change_status_book(book_id, new_status):
                print("Статус книги был успешно изменен!")
            else:
                print("Книга не найдена!")
        elif answer == '6':
            print("Спасибо, что воспользовались нашей системой!")
            break
        else:
            print("Была введена неверная команда! Попробуйте еще раз!")    

main()
