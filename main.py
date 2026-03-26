from selenium.webdriver.chrome.options import Options
from selenium import webdriver
import contact_tracker  # Import the contact tracker module
from whatsapp.functions import load_contacts, load_welcome_message
from whatsapp.send import send_messages

def test():
    contacts_to_message = load_contacts()
    sent_contacts = contact_tracker.load_sent_contacts()

    # Filter out already messaged contacts
    new_contacts = [phone for phone in contacts_to_message if phone not in sent_contacts]
    
    print("Contacts to message (excluding already messaged):")
    print(new_contacts)

def main():
    # Load contacts to message and already sent contacts
    contacts_to_message = load_contacts()
    sent_contacts = contact_tracker.load_sent_contacts()

    options = Options()
    options.page_load_strategy = 'eager'

    print('Pre sent filtering:\n', contacts_to_message)
    # Filter out contacts who have already been sent messages
    contacts_to_message = [contact for contact in contacts_to_message if contact['phone'] not in sent_contacts]
    # contacts_to_message = ['89356532', '78485278', '76511390']
    contacts_to_mail = [contact['email'] for contact in contacts_to_message]
    print("Sending messages to:\n", contacts_to_message)
    # Initialize the WebDriver
    driver = webdriver.Chrome(options=options)  # or use another driver like Firefox
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
