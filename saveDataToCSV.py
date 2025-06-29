import pandas as pd
import os

#['American Eagle\ncargo\nmid blue shade\n700\n1599\ndenim material\n22-3\n24-4\n26-3\n28-3\n30-2\n32-2\n34-2']

# Function to process user-supplied data
def process_input_data(data_string):
    # Split the data by lines
    lines = data_string.strip().split('\n')
    
    # Extract the relevant fields from the input
    data = {
        "Name": lines[0],
        "Category": lines[1],
        "Color": lines[2],
        "Weight": lines[3],
        "Price": lines[4],
        "Material & Care": lines[5],
        "Size-Quantity": lines[6:]
    }

    return data

# Function to process data and save it to Excel
def store_product_data(file_name):
    # If file exists, load existing data, else create a new DataFrame
    if os.path.exists(file_name):
        df = pd.read_excel(file_name)
    else:
        df = pd.DataFrame()

    while True:
        # Ask user for input in the specified format
        print("Please enter product details in the following format:\n")
        print("American Eagle\nCargo\nMid blue shade\n700 gm\n₹1599\nDenim material\n22-3\n24-4\n...")
        print("\nEnter the details below (one product at a time):")

        user_input = []
        while True:
            line = input()
            if line:
                user_input.append(line)
            else:
                break

        # Process the input data
        product_data = process_input_data("\n".join(user_input))

        # Extract static product info (Name, Category, Color, Material & Care) for the first row
        size_quantity_rows = []
        for i, size_quantity in enumerate(product_data["Size-Quantity"]):
            size, quantity = size_quantity.split("-")
            if i == 0:  # First row with product info and size-quantity
                row_data = {
                    "Name": product_data["Name"],
                    "Category": product_data["Category"],
                    "Color": product_data["Color"],
                    "Material & Care": product_data["Material & Care"],
                    "Size": size,
                    "Quantity": int(quantity)  # Convert quantity to integer
                }
            else:  # Subsequent rows with only size and quantity
                row_data = {
                    "Name": "",  # Blank for subsequent rows
                    "Category": "",
                    "Color": "",
                    "Material & Care": "",
                    "Size": size,
                    "Quantity": int(quantity)
                }
            size_quantity_rows.append(row_data)

        # Create a DataFrame for the current product's rows
        df_product_rows = pd.DataFrame(size_quantity_rows)

        # Add the new product's data to the main DataFrame
        df = pd.concat([df, df_product_rows], ignore_index=True)

        # Ask if the user wants to continue
        another_entry = input("Do you want to add another product? (yes/no): ").lower()
        if another_entry != 'yes':
            break

    # Save the DataFrame to an Excel file without NaN, ensuring blank cells
    df.to_excel(file_name, index=False, na_rep="")

    print(f"Data successfully saved to {file_name}")

# Save data to Excel repeatedly
store_product_data("client_product_data.xlsx")
