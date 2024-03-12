def init():
    print(
        "\n"
        + "-" * 100
        + "\n"
        + "Islington Shop Admin Portal".center(100, " ")
        + "\n"
        + "Kamalpokhari, Kathmandu".center(100, " ")
        + "\n"
        + "98XXXXXXXX".center(100, " ")
    )


def prompt_for_action() -> str:
    while True:
        print("-" * 100)
        print("What would you like to do?\n")
        print(" B = Buy from company")
        print(" S = Sell to customer")
        print(" V = View inventory")
        print(" Q = Quit the program")
        action = input("\n> ").strip().upper()
        if action == "B":
            return "BUY"
        elif action == "S":
            return "SELL"
        elif action == "V":
            return "VIEW"
        elif action == "Q":
            return "QUIT"
        else:
            print_custom_error("Invalid action!")


def view_inventory(products_in_inventory):
    print("-" * 100 + "\n" + "Inventory".center(100, " ") + "\n" + "-" * 100)
    if not products_in_inventory:
        print("The inventory is empty")
    else:
        max_len_sn_col = max(len(str(max(products_in_inventory.keys()))), len("S.N."))
        desc_cols = ["Model", "Brand", "Price", "Quantity", "CPU", "GPU"]
        max_len_desc_cols = [
            max(
                len(col),
                max(len(value[col]) for value in products_in_inventory.values()),
            )
            for col in desc_cols
        ]

        print(
            "S.N."
            + " " * (max_len_sn_col - len("S.N.") + 5)
            + desc_cols[0]
            + " " * (max_len_desc_cols[0] - len(desc_cols[0]) + 5)
            + desc_cols[1]
            + " " * (max_len_desc_cols[1] - len(desc_cols[1]) + 5)
            + desc_cols[2]
            + " " * (max_len_desc_cols[2] - len(desc_cols[2]) + 5)
            + desc_cols[3]
            + " " * (max_len_desc_cols[3] - len(desc_cols[3]) + 5)
            + desc_cols[4]
            + " " * (max_len_desc_cols[4] - len(desc_cols[4]) + 5)
            + desc_cols[5]
            + " " * (max_len_desc_cols[5] - len(desc_cols[5]) + 5)
        )
        for key, value in products_in_inventory.items():
            print(
                str(key)
                + " " * (max_len_sn_col - len(str(key)) + 5)
                + value["Model"]
                + " " * (max_len_desc_cols[0] - len(value["Model"]) + 5)
                + value["Brand"]
                + " " * (max_len_desc_cols[1] - len(value["Brand"]) + 5)
                + value["Price"]
                + " " * (max_len_desc_cols[2] - len(value["Price"]) + 5)
                + value["Quantity"]
                + " " * (max_len_desc_cols[3] - len(value["Quantity"]) + 5)
                + value["CPU"]
                + " " * (max_len_desc_cols[4] - len(value["CPU"]) + 5)
                + value["GPU"]
                + " " * (max_len_desc_cols[5] - len(value["GPU"]) + 5)
            )


def buy_menu():
    while True:
        print("-" * 100)
        print("What would you like to do?")
        print("\n R = Restock existing product")
        print(" N = Buy new product")
        action = (
            input("\n(Write :q to discard and return to main menu)\n\n> ")
            .strip()
            .upper()
        )
        if action == "R":
            return "RESTOCK"
        elif action == "N":
            return "BUY_NEW"
        elif action == ":Q":
            return None
        else:
            print_custom_error("Invalid action!")


def buy_new_product():
    print("-" * 100)
    while True:
        brand_b = input(
            "Enter the name of the brand (Write :q to discard and return to main menu)\n> "
        )
        if brand_b == ":q":
            return None
        if brand_b.replace(" ", "").isalpha():
            break
        else:
            print_custom_error(
                "The name of the brand must not contain special characters or numbers"
            )
    while True:
        model_b = input(
            "Enter the name of the model (Write :q to discard and return to main menu)\n> "
        )
        if model_b == ":q":
            return None
        if model_b.replace(" ", "").isalnum():
            break
        else:
            print_custom_error("The model should not contain special characters")
    while True:
        quantity_b = input(
            "Enter the quantity (Write :q to discard and return to main menu)\n> "
        )
        if quantity_b == ":q":
            return None
        try:
            quantity_b = int(quantity_b)
            if quantity_b <= 0:
                print_custom_error(
                    "Enter a valid quantity (The quantity is out of range)"
                )
            else:
                break
        except ValueError:
            print_custom_error("Invalid Input!")
    while True:
        price_b = input(
            "Quote the price($) (Write :q to discard and return to main menu)\n> "
        ).replace("$", "")
        if price_b == ":q":
            return None
        try:
            price_b = int(price_b)
            if price_b <= 0:
                print_custom_error("Enter a valid price (The price is out of range)")
            else:
                break
        except ValueError:
            print_custom_error("Invalid Input!")
    while True:
        cpu_b = input(
            "Enter the CPU variant (Write :q to discard and return to main menu)\n> "
        )
        if cpu_b == ":q":
            return None
        if cpu_b.replace(" ", "").isalnum():
            break
        else:
            print_custom_error("The CPU name should not contain special characters")
    while True:
        gpu_b = input(
            "Enter the GPU variant (Write :q to discard and return to main menu)\n> "
        )
        if gpu_b == ":q":
            return None
        if gpu_b.replace(" ", "").isalnum():
            break
        else:
            print_custom_error("The GPU name should not contain special characters")
    buy_success_message = (
        "Successfully bought " + str(quantity_b) + " " + model_b + " laptop"
    )
    if quantity_b == 1:
        print_success_message(buy_success_message)
    else:
        print_success_message(buy_success_message + "s")
    return model_b, brand_b, price_b, quantity_b, cpu_b, gpu_b


def restock_existing_product(products_in_inventory):
    print("-" * 100)
    while True:
        symbol_no_r = input(
            "Enter the S.N. of the product (Write :q to discard and return to main menu)\n> "
        )
        if symbol_no_r == ":q":
            return None
        try:
            symbol_no_r = int(symbol_no_r)
            if symbol_no_r > len(products_in_inventory) or symbol_no_r <= 0:
                print_custom_error(
                    "Enter a valid S.N (The symbol number is out of range)"
                )
            else:
                break
        except ValueError:
            print_custom_error("Invalid input!")
    while True:
        quantity_r = input(
            "Enter the quantity (Write :q to discard and return to main menu)\n> "
        )
        if quantity_r == ":q":
            return None
        try:
            quantity_r = int(quantity_r)
            if quantity_r <= 0:
                print_custom_error(
                    "Enter a valid quantity (The quantity is out of range)"
                )
            else:
                break
        except ValueError:
            print_custom_error("Invalid Input!")
    model = products_in_inventory[symbol_no_r]["Model"]
    restock_success_message = (
        "Successfully restocked " + str(quantity_r) + " " + model + " laptop"
    )
    if quantity_r == 1:
        print_success_message(restock_success_message)
    else:
        print_success_message(restock_success_message + "s")
    return symbol_no_r, quantity_r


def sell_menu_initial():
    print("-" * 100)
    while True:
        customer_name = input(
            "Enter the name of customer (Write :q to discard and return to main menu)\n> "
        )
        if customer_name == ":q":
            return None
        if customer_name.replace(" ", "").isalpha():
            break
        else:
            print_custom_error(
                "The name of customer should not contain numeric or special characters"
            )
    customer_address = input(
        "Enter the address of customer (Write :q to discard and return to main menu)\n> "
    ).strip()
    if customer_address == ":q":
        return None
    return customer_name, customer_address


def sell_product(dictionary_of_products):
    print("-" * 100)
    while True:
        symbol_no_s = input(
            "Enter the S.N. of the product (Write :q to discard and return to main menu)\n> "
        )
        if symbol_no_s == ":q":
            return None
        try:
            symbol_no_s = int(symbol_no_s)
            if symbol_no_s > len(dictionary_of_products) or symbol_no_s <= 0:
                print_custom_error(
                    "Enter a valid S.N (The symbol number is out of range)"
                )
            else:
                quantity_in_inventory = int(
                    dictionary_of_products[symbol_no_s]["Quantity"]
                )
                model = dictionary_of_products[symbol_no_s]["Model"]
                if quantity_in_inventory == 0:
                    print_custom_error(
                        "Please select another product (" + model + " is out of stock)"
                    )
                else:
                    break
        except ValueError:
            print_custom_error("Invalid input")
    while True:
        quantity_s = input(
            "Enter the quantity (Write :q to discard and return to main menu)\n> "
        )
        if quantity_s == ":q":
            return None
        try:
            quantity_s = int(quantity_s)
            if quantity_s > quantity_in_inventory or quantity_s <= 0:
                print_custom_error(
                    "Quantity out of bounds (Only "
                    + str(quantity_in_inventory)
                    + " "
                    + model
                    + " laptops are left in stock)"
                )
            else:
                break
        except ValueError:
            print_custom_error("Invalid Input!")
    sell_success_message = (
        "Successfully sold " + str(quantity_s) + " " + model + " laptop"
    )
    if quantity_s == 1:
        print_success_message(sell_success_message)
    else:
        print_success_message(sell_success_message + "s")
    return symbol_no_s, quantity_s


def continue_selling():
    while True:
        print("-" * 100)
        cont = (
            input("Do you want to sell more products to the same customer?(y/n)\n> ")
            .upper()
            .strip()
        )
        if cont == "Y":
            return "YES"
        elif cont == "N":
            return "NO"
        else:
            print_custom_error("Invalid action!")


def continue_buying():
    while True:
        print("-" * 100)
        cont = input("Do you want to buy more products from the same company?(y/n)\n> ")
        if cont.upper().strip() == "Y":
            return "YES"
        elif cont.upper().strip() == "N":
            return "NO"
        else:
            print_custom_error("Invalid action!")


def buy_menu_initial():
    print("-" * 100)
    while True:
        company_name = input(
            "Enter the name of company (Write :q to discard and return to main menu)\n> "
        )
        if company_name == ":q":
            return None
        if company_name.replace(" ", "").isalpha():
            break
        else:
            print_custom_error(
                "The name should not contain numeric or special characters"
            )
    company_address = input(
        "Enter the address of company (Write :q to discard and return to main menu)\n> "
    ).strip()
    if company_address == ":q":
        return None
    return company_name, company_address


def prompt_for_delivery_method():
    while True:
        print("-" * 100)
        print("How does the customer want to receive the products?\n")
        print(" S = Shipped to their location")
        print(" P = In-store Pickup")
        shipping = input("\n> ")
        if shipping.upper().strip() == "S":
            return "SHIPPING"
        elif shipping.upper().strip() == "P":
            return "PICKUP"
        else:
            print_custom_error("Invalid action!")


def prompt_to_print_invoice():
    while True:
        print("-" * 100)
        print("Do you want to print the invoice on the screen?(y/n)")
        user_input = input("> ").upper().strip()
        if user_input == "Y":
            return "YES"
        if user_input == "N":
            print("")
            return "NO"
        else:
            print_custom_error("Invalid action!")


def print_custom_error(error_text: str):
    # print("\033[93m" + "Warning: " + error_text + "\033[0m")
    print(error_text)


def print_success_message(success_text: str):
    # print("\033[92m" + success_text + "\033[0m")
    print(success_text)
