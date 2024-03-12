def read_inventory() -> list[str]:
    """This function reads the lines of inventory.txt file to a list and then returns the list

    :return: A list of strings where each string is a line of the inventory.txt file
    :rtype: list[str]
    """
    try:
        with open("inventory.txt", "r") as file:
            raw_data = file.readlines()
    except IOError:
        raw_data = []
    return raw_data
