from mail.mail import enviar_correo_bienvenida
from selenium.webdriver.common.by import By
import time

import contact_tracker
from whatsapp.functions import clean_name_by_mail


def send_messages(driver, contacts_to_message, message):
    """Send the welcome message to the contacts."""

    for contact in contacts_to_message:
        enviar_correo_bienvenida(contact['email'], clean_name_by_mail(contact['email']))
        
        driver.get(f"https://web.whatsapp.com/send?phone={contact['phone']}&text={message}")
        time.sleep(15)  # wait for the chat to load
        
        # Click the send button
        try:
            send_button = driver.find_element(By.XPATH, "//span[@data-icon='send']")
            send_button.click()
            time.sleep(10)  # wait before moving to the next contact

            # Save this contact to sent contacts to avoid re-sending
            contact_tracker.save_sent_contact(contact)
            print(f"Message sent to {contact}")
        except Exception as e:
            print(f"Failed to send message to {contact}: {e}")