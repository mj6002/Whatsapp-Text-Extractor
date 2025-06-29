'''
FORMAT REQUIRED FOR INPUT DATA:
 ['American Eagle\nCargo\nmid blue shade\n700\n1599\ndenim material\nno description\n22-3\n24-4\n26-3\n28-3\n30-2\n32-2\n34-2']
'''

# Function to process input
def process_input_data(data):
    lines = data[0].strip().split('\n')
    
    # Extract relevant fields
    name = lines[0]
    category = lines[1]
    color = lines[2]
    weight = lines[3]
    price = lines[4]
    material_care = lines[5]
    description = lines[6] if len(lines) > 6 else ""  # Add description if it exists
    size_quantity = lines[7:]

    size_quantity_data = []
    
    for sq in size_quantity:
        if '-' in sq:  # Check if '-' is present
            size, quantity = sq.split('-')
            size_quantity_data.append((size.strip(), quantity.strip()))  # Strip to remove any extra whitespace
            print
        else:
            print(f"Warning: Invalid size-quantity format: {sq}")  # Handle the case where the format is not as expected

    metafield_size = ";".join([size for size, _ in size_quantity_data])




    try:
        collection = {"Shirt" : "Apparel & Accessories > Clothing > Clothing Tops > Shirts",
                      "Coord Set" : "Apparel & Accessories > Clothing > Outfit Sets",
                      "Tops" : "Apparel & Accessories > Clothing > Shirts & Tops > Tops",
                      "T-Shirts" : "Apparel & Accessories > Clothing > Shirts & Tops > T-Shirts",
                      "Denim" : "Apparel & Accessories > Clothing > Pants > Jeans",
                      "Cargo" : "Apparel & Accessories > Clothing > Pants > Cargo Pants",
                      "Korean Pants" : "Apparel & Accessories > Clothing > Pants > Korean Pants",
                      "Shirts" : "Apparel & Accessories > Clothing > Shirts & Tops > Shirts",
                      "Shorts" : "Apparel & Accessories > Clothing > Shorts & Skirts",
                      "Skirts" : "Apparel & Accessories > Clothing > Shorts & Skirts",
                      "Dresses" : "Apparel & Accessories > Clothing > Dresses",
                      "Jackets" : "Apparel & Accessories > Clothing > Outerwear > Jackets",
                      "Sweatshirts" : "Apparel & Accessories > Clothing > Sweatshirts",
                      "Sweaters" : "Apparel & Accessories > Clothing > Sweaters"
        }
        if category in collection:
            category = collection[category]
            

    except Exception:
        print(f"WARNING: Category '{category}' not found in collection.")        

    
    return {
        "Name": name,
        "Title": name,
        "Product Category": category,
        "Tags": category,
        "Option1 Value": color,
        "Variant Grams": weight,
        "Variant Price": price,
        "Material & Care": material_care,
        "Description": description,
        "Size-Quantity": size_quantity_data,
        "Size (product.metafields.shopify.size)": metafield_size,
        # "Color (product.metafields.shopify.color-pattern)" : metafield_color
    }


process_input_data()