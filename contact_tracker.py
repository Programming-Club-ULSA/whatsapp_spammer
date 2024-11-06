import csv

def load_sent_contacts(file_path='sent_contacts.csv'):
    """Load contacts that have already received messages from a CSV file."""
    sent_contacts = set()
    try:
        with open(file_path, mode='r', newline='') as file:
            csv_reader = csv.reader(file)
            for row in csv_reader:
                if row:  # Ensure row is not empty
                    sent_contacts.add(row[0].strip())
    except FileNotFoundError:
        print("No existing sent contacts file found. Starting fresh.")
    return sent_contacts

def save_sent_contact(phone, file_path='sent_contacts.csv'):
    """Append a single contact to the sent contacts CSV file."""
    with open(file_path, mode='a', newline='') as file:
        csv_writer = csv.writer(file)
        csv_writer.writerow([phone])
