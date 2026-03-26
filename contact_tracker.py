import csv

def load_sent_contacts(file_path='sent_contacts.csv'):
    """Load contacts that have already received messages from a CSV file."""
    sent_contacts = set()
    try:
        with open(file_path, mode='r', newline='', encoding='utf-8') as file:
            csv_reader = csv.reader(file)
            for row in csv_reader:
                if row:  # Ensure row is not empty
                    sent_contacts.add(row[0].strip())
    except FileNotFoundError:
        print("No existing sent contacts file found. Starting fresh.")
    return sent_contacts

def save_sent_contact(contact_dict, file_path='sent_contacts.csv'):
    """Append a single contact to the sent contacts CSV file."""
    phone = contact_dict.get('phone')
    email = contact_dict.get('email')
    name = contact_dict.get('userName')

    with open(file_path, mode='a', newline='', encoding='utf-8') as file:
        csv_writer = csv.writer(file)
        csv_writer.writerow([name, email, phone])
