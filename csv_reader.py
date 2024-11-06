import csv

# Constants for column names to ensure consistency
PREINSCRIPTION_PHONE_COL = 'phone'
PREINSCRIPTION_EMAIL_COL = 'email'
INSCRIPTION_EMAIL_COL = 'email'

def load_csv_as_dict(file_path, key_col, value_col):
    """Load CSV into a dictionary using specified columns as key-value pairs."""
    data = {}
    try:
        with open(file_path, mode='r', newline='', encoding='utf-8') as file:
            csv_reader = csv.DictReader(file)
            
            # Check for fieldnames
            fieldnames = csv_reader.fieldnames
            if key_col not in fieldnames or value_col not in fieldnames:
                print("Key or value not found")
                return

            for row in csv_reader:
                data[row[key_col]] = row[value_col]
    except FileNotFoundError:
        print(f"Error: File '{file_path}' not found.")
    except KeyError as e:
        print(f"Error: Missing column {e} in '{file_path}'.")
    return data

def load_csv_as_set(file_path, key_col):
    """Load a single column CSV as a set for efficient lookups."""
    data = set()
    try:
        with open(file_path, mode='r', newline='', encoding='utf-8') as file:
            csv_reader = csv.DictReader(file)
            for row in csv_reader:
                data.add(row[key_col])
    except FileNotFoundError:
        print(f"Error: File '{file_path}' not found.")
    except KeyError as e:
        print(f"Error: Missing column {e} in '{file_path}'.")
    return data

def intersect_contacts(preinscription, inscription):
    """Return contacts from pre-inscription that also appear in inscription."""
    intersected: dict = {}
    for email, phone in preinscription.items():
        if email in inscription:
            intersected[email] = phone

    return intersected