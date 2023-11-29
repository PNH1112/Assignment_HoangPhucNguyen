
class Publication():
    def __init__(self,name):
        self.name = name

    def print_information(self):
        print(f"name: {self.name}")

class Book(Publication):
    def __init__(self,name, author, page_count):
        super().__init__(name)
        self.author = author
        self.page_count = page_count

    def print_information(self):
       print(f"${self.name} (author: {self.author}, ${self.page_count} pages)")

class Magazine(Publication):
    def __init__(self,name,chief_editor):
        super().__init__(name)
        self.chief_editor = chief_editor

    def print_information(self):
        print(f"{self.name} (chief editor {self.chief_editor})")

##initialize

publication1 = Magazine("Donald Duck","Aki Hyyppä")
publication2 = Book ("Compartment No. 6","Rosa Liksom", 192)

publication1.print_information()
publication2.print_information()