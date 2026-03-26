import csv_funcs.csv_reader as csv_reader
import re

def clean_name_by_mail(name):
    user_part = name.split('@')[0]
    name_parts = user_part.split('.')
    clean_name = " ".join(name_parts).title()

    return clean_name

def load_contacts():
    preinscription_path = 'preinscription.csv'  # Path to pre-inscription CSV
    inscription_path = 'inscription.csv'  # Path to inscription CSV

    # Load and intersect contacts
    preinscription_data = csv_reader.load_csv_as_dict(preinscription_path, csv_reader.PREINSCRIPTION_EMAIL_COL, csv_reader.PREINSCRIPTION_PHONE_COL)
    inscription_data = csv_reader.load_csv_as_set(inscription_path, csv_reader.INSCRIPTION_EMAIL_COL)
    # print("Preinscription data:\n", preinscription_data)
    # print("Inscription data:\n", inscription_data)
    filtered_contacts = csv_reader.intersect_contacts(preinscription_data, inscription_data)
    # print("Filtered data:\n", filtered_contacts)

    final_contacts = []

    for email, phone in filtered_contacts.items():
        clean_name = clean_name_by_mail(email)

        phone_cleaned = clean_phone_number(phone)

        contact_info = {
            'userName': clean_name,
            'email': email,
            'phone': phone_cleaned
        }

        final_contacts.append(contact_info)

    print(f"Loaded {len(final_contacts)} formatted contacts.")

    return final_contacts

# Function to load the welcome message from a text file
def load_welcome_message(file_path):
    """Load the welcome message from a text file."""
    with open(file_path, 'r', encoding='utf-8') as file:
        return file.read()
    
def clean_phone_number(phone_number):
    """Remove all non-numeric characters and add country code if missing."""
    # Remove all non-numeric characters
    cleaned_number = re.sub(r'\D', '', phone_number)
    
    # Check if the cleaned number is missing the country code and prepend it if necessary
    if not cleaned_number.startswith('505'):
        cleaned_number = '505' + cleaned_number  # Add country code
    
    return cleaned_number