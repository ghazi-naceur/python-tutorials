class Sample():
    pass

class Book():
    def __init__(self, title, author, pages):
        self.title = title
        self.author = author
        self.pages = pages

    def __str__(self):
        return f"{self.title} by {self.author}. Nb pages is {self.pages}"

    def __len__(self):
        return self.pages

    def __del__(self):
        print(f"'{self.title}' book is deleted from the memory")


if __name__ == '__main__':
    new_list = [1,2,3]
    len(new_list)

    sample = Sample()

    book = Book("Type safety is essential", "Someone", 1)
    print(book)
    len(book)

    del book # delete the book from the memory
    # print(book) # Error because book is no longer defined
