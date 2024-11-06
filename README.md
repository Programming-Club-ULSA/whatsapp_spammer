# WhatsApp Community Invitation Automation
## Overview
This Python script automates the process of sending WhatsApp community invitations to users from a filtered contact list. It uses the Selenium WebDriver to interact with the WhatsApp Web interface, sending a pre-written welcome message to each contact.

The script processes contacts from two CSV files: one for pre-inscription data and another for inscription data. After filtering the contacts, it sends personalized invitations to WhatsApp users.

## Features:
Cleans phone numbers to ensure they are in a valid format (removes non-numeric characters).
Loads contact information from CSV files.
Loads a personalized welcome message from a text file.
Automates WhatsApp Web to send messages to a list of phone numbers.
Avoids re-sending messages by tracking sent contacts.

## Requirements
Python 3.x
selenium library
csv module (standard Python library)
A Google Chrome WebDriver or Firefox WebDriver installed locally.

## Install Dependencies
### To use this script, make sure to install Selenium:

```bash
pip install selenium
```

Also, download the appropriate WebDriver for your browser:

ChromeDriver: Download here
GeckoDriver (Firefox): Download here

### Files Required:
preinscription.csv: A CSV file containing the pre-inscription data with phone numbers and emails.
inscription.csv: A CSV file containing the inscription data with phone numbers.
welcome_message.txt: A text file containing the welcome message to be sent to the contacts.

## How It Works:
### Load and Clean Contacts:

The script reads phone numbers from preinscription.csv and inscription.csv, filtering only those that are present in both files.
It then cleans these numbers by removing non-numeric characters, and ensures that each number includes the correct country code (e.g., 505 for Nicaragua).

### Load Welcome Message:
The welcome message is loaded from welcome_message.txt to ensure that you can easily modify it without touching the code.
### Send Messages:
Using Selenium, the script opens WhatsApp Web and waits for the user to scan the QR code.
It then sends the invitation message to each contact in the filtered list, excluding contacts that have already received the message.
### Track Sent Messages:

Contacts that have already received the message are tracked in the sent_contacts list to avoid re-sending messages.

## Functions:
clean_phone_number(phone_number)
Removes all non-numeric characters and ensures the number has the correct country code.

load_welcome_message(file_path)
Loads the welcome message from a text file.

load_contacts()
Reads and filters the contacts from preinscription.csv and inscription.csv, cleaning and preparing the phone numbers for sending.

test()
Checks which contacts have been filtered and are ready to receive a message. It excludes contacts that have already been sent the message.

send_messages(driver, contacts_to_message, message)
Uses Selenium WebDriver to send a message to each contact through WhatsApp Web.

main()
Orchestrates the entire flow:

Loads contacts.
Filters out already sent contacts.
Sends the welcome message to each remaining contact.

## Usage
Prepare the CSV Files:

Ensure preinscription.csv contains phone numbers and emails of users who have pre-registered.
Ensure inscription.csv contains the phone numbers of users who are officially registered.
Prepare the Welcome Message:

Edit welcome_message.txt with your message. This will be the content sent to your contacts.
### Run the Script:
Execute the script using:
```bash
python your_script_name.py
```
Scan QR Code:

Once the script runs, it will open WhatsApp Web. Scan the QR code with your phone to authenticate.
Monitor the Process:

The script will send the message to each eligible contact, and print the status in the console.
## Example:
```bash
python send_whatsapp_invitations.py
```

## Notes:
Ensure that the phone numbers in the CSV files are in a consistent format and include the country code (e.g., +505 8201 5583).
The script uses the selenium WebDriver to automate WhatsApp Web. If you're using Chrome, make sure you have the corresponding ChromeDriver version installed.
The invitation link used in the message is hardcoded into the script but can be modified in the welcome message.

## License
This project is licensed under the MIT License. See the LICENSE file for more details.