from inventory import add_medicine
from inventory import view_medicines
from inventory import delete_medicine
from inventory import reset_medicines
from inventory import sell_medicine
from inventory import add_stock


while True:

    print("\n" + "=" * 50)
    print("        PHARMACY ERP SYSTEM")
    print("=" * 50)

    print("1. Add Medicine")
    print("2. View Medicines")
    print("3. Delete Medicine")
    print("4. Sell Medicine")
    print("5. Add New Stock")
    print("6. Reset All Medicines")
    print("7. Exit")

    choice = input("\nEnter choice: ")

    if choice == '1':

        print("\n--- Add Medicine ---")

        name = input("Medicine Name: ")

        batch = input("Batch No: ")

        quantity = int(input("Quantity: "))

        price = float(input("Price: "))

        expiry = input("Expiry Date (YYYY-MM-DD): ")

        add_medicine(
            name,
            batch,
            quantity,
            price,
            expiry
        )

        print("\nMedicine Added Successfully")

    elif choice == '2':

        print("\n--- Medicine Inventory ---")

        view_medicines()

    elif choice == '3':

        print("\n--- Delete Medicine ---")

        med_id = int(input("Enter Medicine ID to delete: "))

        delete_medicine(med_id)

        print("\nMedicine Deleted Successfully")

    elif choice == '4':

        print("\n--- Sell Medicine ---")

        med_id = int(input("Enter Medicine ID: "))

        sold_quantity = int(input("Enter Sold Quantity: "))

        sell_medicine(med_id, sold_quantity)

    elif choice == '5':

        print("\n--- Add New Stock ---")

        med_id = int(input("Enter Medicine ID: "))

        added_quantity = int(input("Enter Added Quantity: "))

        add_stock(med_id, added_quantity)

    elif choice == '6':

        confirm = input(
            "\nAre you sure you want to delete ALL medicines? (yes/no): "
        )

        if confirm.lower() == 'yes':

            reset_medicines()

        else:

            print("\nReset Cancelled")

    elif choice == '7':

        print("\nClosing Pharmacy ERP System...")

        break

    else:

        print("\nInvalid Choice. Please try again.")