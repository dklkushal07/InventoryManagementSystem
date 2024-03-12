global products
global sold_products
global bought_products


def create_dictionary(raw_data: list[str]) -> dict[dict]:
    """This function takes a list of strings as raw data and inserts its contents into a nested dictionary

    :type raw_data: list[str]
    :return: A dictionary whose keys are the symbol numbers of the products and the value is a dictionary that contains details of the product.
    :rtype: dict[dict]
    """
    global products
    products = {}
    for index in range(len(raw_data)):
        product_data = raw_data[index].strip().split(",")
        for sub_index in range(len(product_data)):
            product_data[sub_index] = product_data[sub_index].strip()
            match sub_index:
                case 0:
                    product_model = product_data[sub_index]
                case 1:
                    product_brand = product_data[sub_index]
                case 2:
                    product_price = product_data[sub_index]
                case 3:
                    product_quantity = product_data[sub_index]
                case 4:
                    product_cpu = product_data[sub_index]
                case 5:
                    product_gpu = product_data[sub_index]
        product_details = {
            "Model": product_model,
            "Brand": product_brand,
            "Price": product_price,
            "Quantity": product_quantity,
            "CPU": product_cpu,
            "GPU": product_gpu,
        }
        products[index + 1] = product_details
    return products


def add_quantity(
    products_in_inventory: dict[dict], symbol_no: int, quantity_to_add: int
) -> dict[dict]:
    global products
    products_in_inventory[symbol_no]["Quantity"] = str(
        int(products_in_inventory[symbol_no]["Quantity"]) + quantity_to_add
    )
    products = products_in_inventory
    return products


def deduct_quantity(
    products_in_inventory: dict[dict], symbol_no: int, quantity_to_deduct: int
) -> dict[dict]:
    products_in_inventory[symbol_no]["Quantity"] = str(
        int(products_in_inventory[symbol_no]["Quantity"]) - quantity_to_deduct
    )
    return products_in_inventory


def add_sold_product(
    model: str, brand: str, quantity: int, unit_price: int
) -> list[str]:
    global sold_products
    if not hasattr(add_sold_product, "symbol_no"):
        add_sold_product.symbol_no = 1
        sold_products = []
    else:
        add_sold_product.symbol_no += 1
    sold_products.append(
        [
            str(add_sold_product.symbol_no),
            model,
            brand,
            str(quantity),
            str(unit_price),
            str(unit_price * quantity),
        ]
    )
    return sold_products


def close_sell() -> None:
    delattr(add_sold_product, "symbol_no")


def add_bought_product(
    model: str, brand: str, quantity: int, unit_price: int
) -> list[str]:
    global bought_products
    if not hasattr(add_bought_product, "symbol_no"):
        add_bought_product.symbol_no = 1
        bought_products = []
    else:
        add_bought_product.symbol_no += 1
    bought_products.append(
        [
            str(add_bought_product.symbol_no),
            model,
            brand,
            str(quantity),
            str(unit_price),
            str(unit_price * quantity),
        ]
    )
    return bought_products


def close_buy() -> None:
    delattr(add_bought_product, "symbol_no")


def add_new_product(products_in_inventory: dict[dict], new_product_details: list):
    exists_in_inventory = False
    for key in range(1, len(products_in_inventory) + 1):
        if (
            products_in_inventory[key]["Model"] == new_product_details[0]
            and products_in_inventory[key]["Brand"] == new_product_details[1]
            and products_in_inventory[key]["Price"] == "$" + str(new_product_details[2])
            and products_in_inventory[key]["CPU"] == new_product_details[4]
            and products_in_inventory[key]["GPU"] == new_product_details[5]
        ):
            print("The product already exists in inventory so it will be restocked")
            products_in_inventory = add_quantity(
                products_in_inventory, key, int(new_product_details[3])
            )
            exists_in_inventory = True
    if not exists_in_inventory:
        key = len(products_in_inventory) + 1
        products_in_inventory[key] = {
            "Model": new_product_details[0],
            "Brand": new_product_details[1],
            "Price": "$" + str(new_product_details[2]),
            "Quantity": str(new_product_details[3]),
            "CPU": new_product_details[4],
            "GPU": new_product_details[5],
        }
    return products_in_inventory
