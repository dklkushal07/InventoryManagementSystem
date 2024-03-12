import datetime

import file_writer

global sell_invoice
global buy_invoice
global s_uid
global b_uid


def create_sell_invoice(
    name_of_customer: str,
    address_of_customer: str,
    products,
    total_amount,
    shipping_cost,
) -> None:
    global sell_invoice
    sell_invoice = []
    global s_uid
    now = datetime.datetime.now()
    date_string = "Date: " + now.strftime("%Y-%m-%d")
    time_string = "Time: " + now.strftime("%H:%M:%S")
    customer_string = "Name of Customer: " + name_of_customer
    address_string = "Address: " + address_of_customer
    s_uid = name_of_customer.replace(" ", "") + now.strftime("_%y_%m_%d_%H_%M_%S")
    sell_invoice.append(
        str(
            "=" * 100
            + "\n"
            + "Islington Shop".center(100, " ")
            + "\n"
            + "Kamalpokhari, Kathmandu".center(100, " ")
            + "\n"
            + "98XXXXXXXX".center(100, " ")
            + "\n"
            + "=" * 100
            + "\n"
            + "INVOICE".center(100, " ")
            + "\n"
            + "-" * 100
            + "\n"
            + customer_string
            + " " * (100 - len(date_string) - len(customer_string))
            + date_string
            + "\n"
            + address_string
            + " " * (100 - len(time_string) - len(address_string))
            + time_string
            + "\n"
            + "-" * 100
        )
    )
    sell_invoice.append(add_products_to_invoice(products))
    twosc_string = "Total(without shipping cost): " + "$" + str(total_amount)
    sc_string = "Shipping cost: " + "$" + str(shipping_cost)
    twsc_string = (
        "Total(with shipping cost): " + "$" + str(total_amount + shipping_cost)
    )
    sell_invoice.append(
        str(
            "-" * 100
            + "\n"
            + " " * (98 - len(twosc_string))
            + twosc_string
            + "\n"
            + " " * (98 - len(sc_string))
            + sc_string
            + "\n"
            + " " * (98 - len(twsc_string))
            + twsc_string
            + "\n"
            + "=" * 100
        )
    )
    file_writer.create_sell_invoice(s_uid, sell_invoice)


def add_products_to_invoice(products):
    title = ["S.N", "Model", "Brand", "Quantity", "Unit Price($)", "Amount($)"]
    max_len_cols = [
        max(len(title[col]), max(len(product[col]) for product in products))
        for col in range(len(title))
    ]

    product_string = (
        "\n"
        + title[0]
        + " " * (max_len_cols[0] - len(title[0]) + 8)
        + title[1]
        + " " * (max_len_cols[1] - len(title[1]) + 8)
        + title[2]
        + " " * (max_len_cols[2] - len(title[2]) + 8)
        + title[3]
        + " " * (max_len_cols[3] - len(title[3]) + 8)
        + title[4]
        + " " * (max_len_cols[4] - len(title[4]) + 8)
        + title[5]
        + "\n"
    )

    for product in products:
        product_string += str(
            str(product[0])
            + " " * (max_len_cols[0] - len(str(product[0])) + 8)
            + product[1]
            + " " * (max_len_cols[1] - len(product[1]) + 8)
            + product[2]
            + " " * (max_len_cols[2] - len(product[2]) + 8)
            + str(product[3])
            + " " * (max_len_cols[3] - len(str(product[3])) + 8)
            + str(product[4])
            + " " * (max_len_cols[4] - len(str(product[4])) + 8)
            + str(product[5])
            + "\n"
        )
    return product_string


def create_buy_invoice(
    name_of_distributor, address_of_distributor, products, total_amount
):
    global buy_invoice
    buy_invoice = []
    global b_uid
    now = datetime.datetime.now()
    date_string = "Date: " + now.strftime("%Y-%m-%d")
    time_string = "Time: " + now.strftime("%H:%M:%S")
    distributor_string = "Name of distributor: " + name_of_distributor
    address_string = "Address: " + address_of_distributor
    b_uid = name_of_distributor.replace(" ", "") + now.strftime("_%y_%m_%d_%H_%M_%S")
    buy_invoice.append(
        str(
            "=" * 100
            + "\n"
            + "Islington Shop".center(100, " ")
            + "\n"
            + "Kamalpokhari, Kathmandu".center(100, " ")
            + "\n"
            + "98XXXXXXXX".center(100, " ")
            + "\n"
            + "=" * 100
            + "\n"
            + "INVOICE".center(100, " ")
            + "\n"
            + "-" * 100
            + "\n"
            + distributor_string
            + " " * (100 - len(date_string) - len(distributor_string))
            + date_string
            + "\n"
            + address_string
            + " " * (100 - len(time_string) - len(address_string))
            + time_string
            + "\n"
            + "-" * 100
        )
    )
    buy_invoice.append(add_products_to_invoice(products))
    twov_string = "Total(without VAT): " + "$" + str(total_amount)
    vat_string = "VAT Amount(13%): " + "$" + str(int(0.13 * total_amount))
    twv_string = "Total(with VAT): " + "$" + str(int(1.13 * total_amount))
    buy_invoice.append(
        str(
            "-" * 100
            + "\n"
            + " " * (98 - len(twov_string))
            + twov_string
            + "\n"
            + " " * (98 - len(vat_string))
            + vat_string
            + "\n"
            + " " * (98 - len(twv_string))
            + twv_string
            + "\n"
            + "=" * 100
        )
    )
    file_writer.create_buy_invoice(b_uid, buy_invoice)


def print_sell_invoice():
    global sell_invoice
    for each in sell_invoice:
        print(each)


def print_buy_invoice():
    global buy_invoice
    for each in buy_invoice:
        print(each)
