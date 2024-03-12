"""The `main` module is the core program that imports other modules and runs in the terminal"""

import file_reader
import file_writer
import invoice_generator
import operations
import user_interface


def main() -> None:
    """All the functions of other modules are called inside the `main` function."""
    raw_data = file_reader.read_inventory()
    products_in_inventory = operations.create_dictionary(raw_data)
    user_interface.init()
    while True:
        action = user_interface.prompt_for_action()
        if action == "QUIT":
            print("-" * 100 + "\nThank you for using the program!")
            break
        elif action == "BUY":
            buy_initializer = user_interface.buy_menu_initial()
            if buy_initializer is not None:
                company_name, company_address = buy_initializer
                bought_products = []
                while True:
                    order_type = user_interface.buy_menu()
                    if order_type is not None:
                        if order_type == "RESTOCK":
                            user_interface.view_inventory(products_in_inventory)
                            restock_order_details = (
                                user_interface.restock_existing_product(
                                    products_in_inventory
                                )
                            )
                            if restock_order_details is None:
                                break
                            else:
                                symbol_no, quantity_b = restock_order_details
                                products_in_inventory = operations.add_quantity(
                                    products_in_inventory, symbol_no, quantity_b
                                )
                                bought_products = operations.add_bought_product(
                                    products_in_inventory[symbol_no]["Model"],
                                    products_in_inventory[symbol_no]["Brand"],
                                    quantity_b,
                                    int(
                                        products_in_inventory[symbol_no][
                                            "Price"
                                        ].replace("$", "")
                                    ),
                                )
                                continue_buying = user_interface.continue_buying()
                                if continue_buying == "NO":
                                    break
                        elif order_type == "BUY_NEW":
                            new_product_details = user_interface.buy_new_product()
                            if new_product_details is None:
                                break
                            else:
                                products_in_inventory = operations.add_new_product(
                                    products_in_inventory, new_product_details
                                )
                                bought_products = operations.add_bought_product(
                                    new_product_details[0],
                                    new_product_details[1],
                                    int(new_product_details[3]),
                                    int(new_product_details[2]),
                                )
                                continue_buying = user_interface.continue_buying()
                                if continue_buying == "NO":
                                    break
                    else:
                        break
                if len(bought_products) > 0:
                    invoice_generator.create_buy_invoice(
                        company_name,
                        company_address,
                        bought_products,
                        sum(int(product[5]) for product in bought_products),
                    )
                    operations.close_buy()
                    print_invoice = user_interface.prompt_to_print_invoice()
                    if print_invoice == "YES":
                        invoice_generator.print_buy_invoice()
                    file_writer.update_inventory_file(products_in_inventory)
        elif action == "SELL":
            sell_initializer = user_interface.sell_menu_initial()
            if sell_initializer is not None:
                customer_name, customer_address = sell_initializer
                sold_products = []
                while True:
                    user_interface.view_inventory(products_in_inventory)
                    sell_order_details = user_interface.sell_product(
                        products_in_inventory
                    )
                    if sell_order_details is None:
                        break
                    else:
                        products_in_inventory = operations.deduct_quantity(
                            products_in_inventory,
                            int(sell_order_details[0]),
                            int(sell_order_details[1]),
                        )
                        sold_products = operations.add_sold_product(
                            products_in_inventory[int(sell_order_details[0])]["Model"],
                            products_in_inventory[int(sell_order_details[0])]["Brand"],
                            int(sell_order_details[1]),
                            int(
                                products_in_inventory[int(sell_order_details[0])][
                                    "Price"
                                ].replace("$", "")
                            ),
                        )
                        continue_selling = user_interface.continue_selling()
                        if continue_selling == "NO":
                            break
                if len(sold_products) > 0:
                    total_amount = sum(int(product[5]) for product in sold_products)
                    delivery_method = user_interface.prompt_for_delivery_method()
                    if delivery_method == "SHIPPING":
                        shipping_cost = 20
                    else:
                        shipping_cost = 0
                    invoice_generator.create_sell_invoice(
                        customer_name,
                        customer_address,
                        sold_products,
                        total_amount,
                        shipping_cost,
                    )
                    operations.close_sell()
                    file_writer.update_inventory_file(products_in_inventory)
                    print_invoice = user_interface.prompt_to_print_invoice()
                    if print_invoice == "YES":
                        invoice_generator.print_sell_invoice()

        elif action == "VIEW":
            user_interface.view_inventory(products_in_inventory)


if __name__ == "__main__":
    main()
