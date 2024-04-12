class Bookstore:
    def __init__(self) -> None:
        self.inventory = {}
        self.sales_data = []

    def rem(self, isbn: int):
        if isbn not in self.inventory:
            print("Book is already not exist in the inventory")
            return

        self.inventory.pop(isbn)
        print("Remove Successfully!!!")

    def display_sales_data(self):
        print(self.sales_data)

    def display_inventory(self):
        print(self.inventory)

    def revenue(self):
        total_revenue = sum([i["Total_Bill"] for i in self.sales_data])
        total_sold = sum([i["quantity"] for i in self.sales_data])
        print("---------Revenue Data of the Year---------")
        print(f"Total revenue : {total_revenue}")
        print(f"Total sold : {total_sold}")

    def order(self, isbn, customer, quantity):
        if isbn not in self.inventory:
            print("Not in Stock")
            return
        elif quantity > self.inventory[isbn]["quantity"]:
            print("Not sufficient quantity")
            return
        elif quantity < 0:
            print("Invalid syntax")
            return

        total_price = self.inventory[isbn]["price"] * quantity
        print(f"Bill of the customer : {total_price}")
        self.inventory[isbn]["quantity"] -= quantity
        data = {
            "quantity": quantity,
            "ISBN": isbn,
            "Customer_name": customer,
            "Total_Bill": total_price,
        }
        self.sales_data.append(data)
        print("Order successfully placed!!")

    def update_quantity(self, isbn, new_quantity):
        if isbn not in self.inventory:
            print("There is no book of given ISBN number")
            return
        if new_quantity <= 0:
            print("Invalid quantity")
            return

        self.inventory[isbn]["quantity"] = new_quantity
        print("Successfully Updated!")

    def search_book(self, query):
        found_books_ids = []
        for isbn, details in self.inventory.items():
            if query.lower() in [
                str(isbn),
                details["name"].lower(),
                details["author"].lower(),
            ]:
                found_books_ids.append(isbn)

        if len(found_books_ids) == 0:
            print("There is no book to this ISBN number")
            return

        for ids in found_books_ids:
            print(f"ISBN : {ids},{self.inventory[ids]}")

    def AddBook(self, isbn, name, author, price, quantity):
        if isbn in self.inventory:
            print("Same ISBN number book already exit")
            return

        self.inventory[isbn] = {
            "name": name,
            "author": author,
            "price": price,
            "quantity": quantity,
        }


obj = Bookstore()
print("Modern Bookstore with all features!!")
while True:
    print("\n1. Add Book")
    print("2. Search Book")
    print("3. Update Quantity")
    print("4. Process Order")
    print("5. Generate Sales Report")
    print("6. Display Inventory")
    print("7. Display Sales Data")
    print("8. Remove book from inventory")
    print("9. Exit\n")
    try:
        choice: int = int(input("Enter your choice : "))
        if choice > 0:
            if choice == 1:
                isbn: int = int(input("Enter the ISBN number : "))
                name: str = str(input("Enter the name of the book : ")).title()
                author: str = str(input("Enter the author of the book : ")).title()
                price: float = float(input("Enter the price of the book : $"))
                quantity: int = int(input("Enter the quantity of the book : "))
                obj.AddBook(
                    isbn=isbn, name=name, author=author, price=price, quantity=quantity
                )
                print("Successfully Added!")

            elif choice == 2:
                q = input("Search by ISBN/name/Author : ")
                obj.search_book(q)

            elif choice == 3:
                isbn: int = int(input("Enter the ISBN number : "))
                new_quantity: int = int(input("Enter the new Quantity of the Book : "))
                obj.update_quantity(isbn, new_quantity)

            elif choice == 4:
                isbn: int = int(input("Enter the ISBN number : "))
                customer_name: str = str(input("Enter the customer name : ")).title()
                quantity: int = int(input("Enter the quantity you want : "))
                obj.order(isbn, customer_name, quantity)

            elif choice == 5:
                obj.revenue()

            elif choice == 6:
                obj.display_inventory()

            elif choice == 7:
                obj.display_sales_data()

            elif choice == 8:
                isbn: int = int(input("Enter the ISBN number : "))
                obj.rem(isbn)

            elif choice == 9:
                print("Thank You!!")
                break
        else:
            print("Invalid Choice!!!!")
            print("Please give the positive value that is greater than Zero.")

    except ValueError:
        print("There is a ValueError!!!!")
        print("Give only integer value.")
    except KeyError:
        print("There is a KeyError!!!!")
    except ZeroDivisionError:
        print("There is a ZeroDivisionError")
    except:
        print("Any other error occured")
