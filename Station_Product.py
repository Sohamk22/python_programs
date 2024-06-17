import random

def read_input_file(input_file):
    stations = {}
    with open(input_file, 'r') as file:
        for line in file:
            station, *products = line.strip().split('-')
            stations[station.strip()] = [product.strip() for product in products]
    return stations

def assign_products(stations):
    assigned_products = set()
    for station, products in stations.items():
        available_products = [product for product in products if product not in assigned_products]
        if available_products:
            selected_product = random.choice(available_products)
            assigned_products.add(selected_product)
            print(f"Assigned {selected_product} to {station}")
        else:
            print(f"No available products for {station}")

def write_output_file(output_file, assignments):
    with open(output_file, 'w') as file:
        for station, product in assignments.items():
            file.write(f"{station} - {product}\n")

if __name__ == '__main__':
    input_file = r'C:\Users\soham\Desktop\stations_products.txt'  # Update with your input file path
    output_file = r'C:\Users\soham\Downloads\assigned_products.txt'  # Update with desired output file path

    stations = read_input_file(input_file)
    assignments = {}
    for station, products in stations.items():
        available_products = [product for product in products if product not in assignments.values()]
        if available_products:
            selected_product = random.choice(available_products)
            assignments[station] = selected_product
        else:
            print(f"No available products for {station}")

    write_output_file(output_file, assignments)
