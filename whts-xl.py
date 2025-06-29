import pandas as pd
import os

# Input data
input_data = ['WIDE LEG\ndenim\ncharcoal grey\n500\n1799\ndenim\nNO DESCRIPTION\n22-5\n24-7\n26-21\n28-14\n30-21\n32-5\n34-9\n36-4']

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
        else:
            print(f"Warning: Invalid size-quantity format: {sq}")  # Handle the case where the format is not as expected

    return {
        "Name": name,
        "Category": category,
        "Color": color,
        "Weight": weight,
        "Price": price,
        "Material & Care": material_care,
        "Description": description,
        "Size-Quantity": size_quantity_data
    }

# Process the input data
product_data = process_input_data(input_data)

# Create a DataFrame from the processed product data
size_quantity_data = product_data['Size-Quantity']
new_df = pd.DataFrame(size_quantity_data, columns=['Size', 'Quantity'])

# Add product information only in the first row
new_df['Title'] = product_data['Name']
new_df['Product Category'] = product_data['Category']
new_df['Option1 Value'] = product_data['Color']
new_df['Variant Grams'] = float(product_data['Weight'])  # Convert to float
new_df['Variant Price'] = float(product_data['Price'])  # Convert to float
new_df['Material & Care'] = product_data['Material & Care']
new_df['Description'] = product_data['Description']  # Add Description column

# Insert size and quantity values directly into Option2 Value and Variant Inventory Qty columns
new_df['Option2 Value'] = new_df['Size']
new_df['Variant Inventory Qty'] = new_df['Quantity']

# Rearrange columns to have product info at the beginning
new_df = new_df[['Title', 'Product Category', 'Option1 Value', 'Variant Grams', 'Variant Price', 'Material & Care', 'Description', 'Option2 Value', 'Variant Inventory Qty']]

# Ensure only the first row has product information
new_df.loc[1:, ['Title', 'Product Category', 'Option1 Value', 'Variant Grams', 'Variant Price', 'Material & Care', 'Description']] = None

# Define the CSV file name
file_name = "products_export - Copy.csv"

# Check if the file exists
if os.path.exists(file_name):
    # Load existing data
    existing_df = pd.read_csv(file_name)

    # Check for relevant columns
    for column in ['Title', 'Product Category', 'Option1 Value', 'Variant Grams', 'Variant Price', 'Material & Care', 'Description', 'Option2 Value', 'Variant Inventory Qty']:
        if column not in existing_df.columns:
            print(f"Warning: Column '{column}' not found in existing CSV. It will be ignored.")

    # Insert new data into specific columns of the existing DataFrame
    combined_df = existing_df.copy()

    # Concatenate the new data to the combined DataFrame
    combined_df = pd.concat([combined_df, new_df], ignore_index=True)

else:
    # If the file does not exist, use the new DataFrame as the combined DataFrame
    combined_df = new_df

# Save the combined DataFrame back to the CSV file
combined_df.to_csv(file_name, index=False)

print("Data successfully appended to 'products_export - Copy.csv'.")
