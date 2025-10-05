# Restaurant Ordering System using OOP

class MenuItem:
    def __init__(self, name, price):
        self.name = name
        self.price = price

    def __str__(self):
        return f"{self.name} - Rs.{self.price}"


class Menu:
    def __init__(self):
        self.items = []

    def add_item(self, item):
        self.items.append(item)

    def show_menu(self):
        print("\n----- MENU -----")
        for i, item in enumerate(self.items, 1):
            print(f"{i}. {item}")
        print("----------------")


class Order:
    def __init__(self):
        self.ordered_items = []

    def add_to_order(self, item):
        self.ordered_items.append(item)

    def show_order(self):
        print("\nYour Order:")
        for item in self.ordered_items:
            print(f"- {item.name} (Rs.{item.price})")

    def calculate_total(self):
        return sum(item.price for item in self.ordered_items)


class Restaurant:
    def __init__(self, name):
        self.name = name
        self.menu = Menu()

    def add_menu_item(self, name, price):
        self.menu.add_item(MenuItem(name, price))

    def take_order(self):
        order = Order()
        while True:
            self.menu.show_menu()
            choice = input("Enter item number to order (or 'done' to finish): ").lower()
            if choice == 'done':
                break
            try:
                index = int(choice) - 1
                if 0 <= index < len(self.menu.items):
                    order.add_to_order(self.menu.items[index])
                    print(f"✅ {self.menu.items[index].name} added to order.")
                else:
                    print("❌ Invalid choice.")
            except ValueError:
                print("❌ Please enter a number.")
        return order


# ---------- MAIN PROGRAM ----------
if __name__ == "__main__":
    restaurant = Restaurant("Zubair's Kitchen")

    # Add menu items
    restaurant.add_menu_item("Burger", 350)
    restaurant.add_menu_item("Pizza", 800)
    restaurant.add_menu_item("Fries", 200)
    restaurant.add_menu_item("Drink", 150)

    print(f"Welcome to {restaurant.name} 🍴")
    order = restaurant.take_order()

    # Display Order Summary
    order.show_order()
    total = order.calculate_total()
    print(f"\n💰 Total Bill: Rs.{total}")
    print("Thank you for visiting! 🙌")
