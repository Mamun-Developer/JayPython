def get_cars():
    """
    Return a dictionary of cars with count
    :return:
    """
    no_of_brands = input("HOW MANY BRANDS? : ")
    no_of_brands = int(no_of_brands)
    cars = {}
    for i in range(0, no_of_brands):
        brand = input("BRAND : ")
        count = input(f"No of {brand} : ")
        cars[brand] = count

    return cars


def get_frequency(d: list):
    """
    Return the frequency of the data in the list
    Example:
    Input: ["B", "A", "B", "C", "A", "B", "A"]
    Output: {'B': 3, 'A': 3, 'C': 1}
    :param d:
    :return:
    """
    frequency = {}
    for data in d:
        if data in frequency:
            frequency[data] += 1
        else:
            frequency[data] = 1
    return frequency


if __name__ == "__main__":
    print(get_frequency(["B", "A", "B", "C", "A", "B", "A"]))
