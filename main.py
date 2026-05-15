class Cafe:
    city = "Samarqand"

    def __init__(self, name, tables):
        self.name = name
        self.tables = tables

    def show_info(self):
        print(f"Kafe: {self.name}")
        print(f"Stollar: {self.tables}")


c1 = Cafe("Coffee House", 15)
c2 = Cafe("Milliy Taomlar", 20)

c1.show_info()
print("----------")
c2.show_info()
