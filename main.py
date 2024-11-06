from selenium import webdriver
from selenium.webdriver.common.by import By
import time

import csv_reader
import contact_tracker  # Import the contact tracker module
import re

def clean_phone_number(phone_number):
    """Remove all non-numeric characters and add country code if missing."""
    # Remove all non-numeric characters
    cleaned_number = re.sub(r'\D', '', phone_number)
    
    # Check if the cleaned number is missing the country code and prepend it if necessary
    if not cleaned_number.startswith('505'):
        cleaned_number = '505' + cleaned_number  # Add country code
    
    return cleaned_number

# Function to load the welcome message from a text file
def load_welcome_message(file_path):
    """Load the welcome message from a text file."""
    with open(file_path, 'r', encoding='utf-8') as file:
        return file.read()

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

    phones = list(filtered_contacts.values())
    for phone in phones:
        phone = clean_phone_number(phone)

    return phones


def test():
    contacts_to_message = load_contacts()
    sent_contacts = contact_tracker.load_sent_contacts()

    # Filter out already messaged contacts
    new_contacts = [phone for phone in contacts_to_message if phone not in sent_contacts]
    
    print("Contacts to message (excluding already messaged):")
    print(new_contacts)

def send_messages(driver, contacts_to_message, message):
    """Send the welcome message to the contacts."""
    for number in contacts_to_message:
        # Open chat with the specific number
        driver.get(f"https://web.whatsapp.com/send?phone={number}&text={message}")
        time.sleep(5)  # wait for the chat to load
        
        # Click the send button
        try:
            send_button = driver.find_element(By.XPATH, "//span[@data-icon='send']")
            send_button.click()
            time.sleep(2)  # wait before moving to the next contact

            # Save this contact to sent contacts to avoid re-sending
            contact_tracker.save_sent_contact(number)
            print(f"Message sent to {number}")
        except Exception as e:
            print(f"Failed to send message to {number}: {e}")

def main():
    # Load contacts to message and already sent contacts
    contacts_to_message = load_contacts()
    sent_contacts = contact_tracker.load_sent_contacts()

    print('Pre sent filtering:\n', contacts_to_message)
    # Filter out contacts who have already been sent messages
    contacts_to_message = [phone for phone in contacts_to_message if phone not in sent_contacts]
    # contacts_to_message = ['89356532', '78485278', '76511390']
    print("Sending messages to:\n", contacts_to_message)
    # Initialize the WebDriver
    driver = webdriver.Chrome()  # or use another driver like Firefox
    driver.get("https://web.whatsapp.com")

    # Wait for user to scan the QR code
    input("Press Enter after scanning QR code...")

    # Community invite link
    welcome_message = load_welcome_message('welcome_message.txt')

    send_messages(driver, contacts_to_message, welcome_message)

    print("All invites have been sent.")
    driver.quit()

if __name__ == '__main__':
    main()
