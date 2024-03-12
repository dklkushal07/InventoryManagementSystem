"""The `file_writer` module writes to the inventory, sale invoice, and order invoice text files"""
import os


def update_inventory_file(dictionary_of_products: dict[dict]) -> None:
    """This function takes a dictionary containing the information of all products in the inventory and writes it in the inventory.txt file

    :param dictionary_of_products: _description_
    :type dictionary_of_products: dict[dict]
    """
    with open("inventory.txt", "w") as file:
        for key in range(1, len(dictionary_of_products) + 1):
            file.write(
                dictionary_of_products[key]["Model"]
                + ", "
                + dictionary_of_products[key]["Brand"]
                + ", "
                + dictionary_of_products[key]["Price"]
                + ", "
                + dictionary_of_products[key]["Quantity"]
                + ", "
                + dictionary_of_products[key]["CPU"]
                + ", "
                + dictionary_of_products[key]["GPU"]
                + "\n"
            )


def create_sell_invoice(unique_id, list_of_strings):
    cur_dir = os.getcwd()
    filename = unique_id + ".txt"
    file_path = os.path.join(cur_dir, "Invoice", "sales", filename)
    with open(file_path, "w") as s_invoice:
        for each in list_of_strings:
            s_invoice.write(each)


def create_buy_invoice(unique_id, list_of_strings):
    cur_dir = os.getcwd()
    filename = unique_id + ".txt"
    file_path = os.path.join(cur_dir, "Invoice", "orders", filename)
    with open(file_path, "w") as b_invoice:
        for each in list_of_strings:
            b_invoice.write(each)
