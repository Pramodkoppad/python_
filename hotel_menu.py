menu={"Pizza": 100,
      "Burger": 80, 
      "Coffee": 50, 
      "Tea": 15, 
      "sandwich": 60, 
      "Pasta": 60,
}
print("Welcome to the Restro")
print("Pizza: 100\nBurger: 80\nCoffee: 50\nTea:15\nsandwich: 60\nPasta: 60")
order_total =0
item_1 = input("Enter the first item: ").capitalize()
if item_1 in menu:
    order_total +=menu[item_1]
    print(f"Your item{item_1} has been added to the order.")
else:
    print(f"Sorry, {item_1} is not available in the menu.")
another_order=input("Do you want to add another item? (Yes/No): ")
if another_order == "yes":
    item_2 = input("Enter the second item: ").capitalize()
    if item_2 in menu:
        order_total +=menu[item_2]
        print(f"Your item{item_2} has been added to the order.")
    else:
        print(f"Sorry, {item_2} is not available in the menu.") 
print(f"Your total order amount is: {order_total}")



