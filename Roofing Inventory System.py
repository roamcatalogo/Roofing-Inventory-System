names = []
quantities = []
prices = []
minimums = []

while True:
    print("\n==============================")
    print("         STORETRACK")
    print("   Small Store Inventory")
    print("==============================")
    print("1. Add Product")
    print("2. View Inventory")
    print("3. Stock In")
    print("4. Stock Out")
    print("5. Low-Stock Report")
    print("6. Exit")

    choice = input("Choose an option (1-6): ")

    if choice == "1":
        name = input("Enter product name: ").lower()

        if name in names:
            print("Product already exists.")
        else:
            quantity = int(input("Enter starting quantity: "))
            price = float(input("Enter unit price: "))
            minimum = int(input("Enter minimum stock level: "))

            names.append(name)
            quantities.append(quantity)
            prices.append(price)
            minimums.append(minimum)
            print("Product added successfully!")

    elif choice == "2":
        if len(names) == 0:
            print("No products recorded.")
        else:
            print("\n===== INVENTORY LIST =====")
            for i in range(len(names)):
                print("Product:", names[i])
                print("Quantity:", quantities[i])
                print("Unit Price: PHP", prices[i])
                print("Minimum Stock:", minimums[i])
                print("-------------------------")

    elif choice == "3":
        name = input("Enter product name: ").lower()

        if name in names:
            i = names.index(name)
            quantity = int(input("Enter quantity received: "))
            quantities[i] = quantities[i] + quantity
            print("Stock added successfully!")
        else:
            print("Product not found.")

    elif choice == "4":
        name = input("Enter product name: ").lower()

        if name in names:
            i = names.index(name)
            quantity = int(input("Enter quantity released: "))

            if quantity > quantities[i]:
                print("Not enough stock available.")
            else:
                quantities[i] = quantities[i] - quantity
                print("Stock released successfully!")
        else:
            print("Product not found.")

    elif choice == "5":
        print("\n===== LOW-STOCK REPORT =====")
        found = False

        for i in range(len(names)):
            if quantities[i] <= minimums[i]:
                print(names[i], "- Remaining quantity:", quantities[i])
                found = True

        if found == False:
            print("No low-stock products found.")

    elif choice == "6":
        print("Thank you for using StoreTrack!")
        break

    else:
        print("Invalid choice. Please choose 1-6.") 
