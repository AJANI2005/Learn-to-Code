
class Log:
    @classmethod
    def Hello(cls):
        print("Hello World!")

class Book:
    def __init__(self):
        self.title = "Default"

    @property
    def Title(self):
        return self.title
    
    @Title.setter
    def Title(self, value):
        self.title = value

def main():
    Log.Hello()
    book = Book()
    book.Title = "Book"
    print(book.title)

if __name__ == "__main__":
    main()