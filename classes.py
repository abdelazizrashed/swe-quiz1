class Publication:
    title: str
    price: float


class Book(Publication):
    page_count: int

    def put_data(self):
        print("Title: ", self.title)
        print("Price: ", self.price)
        print("Page count: ", self.page_count)

    def get_data(self):
        self.title = input("Enter title: ")
        self.price = float(input("Enter price: "))
        self.page_count = int(input("Enter page count: "))


class Tape(Publication):
    playing_time: float

    def put_data(self):
        print("Title: ", self.title)
        print("Price: ", self.price)
        print("Playing time: ", self.playing_time)

    def get_data(self):
        self.title = input("Enter title: ")
        self.price = float(input("Enter price: "))
        self.playing_time = float(input("Enter playing time: "))
