# WhatsApp Automation Script

This repository contains a simple Python script for automating message sending on WhatsApp using the Selenium WebDriver. The script is designed to work with the Firefox browser, but it can be adapted for use with Chrome or other browsers that support Selenium.

## Prerequisites

Before running the script, make sure you have the following installed:

- Python 3
- Selenium Python package
- Firefox browser
- [geckodriver](https://github.com/mozilla/geckodriver/releases) for Firefox

## Setup

1. Install the Selenium package using pip if you haven't already:

   ```bash
   pip install selenium
   ```

2. Download the `geckodriver` executable for your operating system from the [geckodriver releases page](https://github.com/mozilla/geckodriver/releases), and place it in a directory that is in your system's PATH.

## Usage

1. Run the script using Python:

   ```bash
   python whatsapp_automation.py
   ```

2. A Firefox window will open, prompting you to scan the QR code using WhatsApp on your phone to log in.

3. After logging in to WhatsApp Web, press Enter in the console to continue.

4. The script will search for the contact named "Mr Kelvin" and send the message "hahahahahahaha" continuously.

## Customization

To customize the script for your use:

- Replace `'Mr Kelvin'` with the name of the contact you wish to send messages to.
- Replace `'hahahahahahaha'` with the message you wish to send.

## Warning

Automating message sending on WhatsApp can be considered spam and may lead to your account being temporarily or permanently banned. Use this script responsibly and at your own risk.

## Disclaimer

This script is for educational purposes only. The author is not responsible for any misuse or damage caused by this script.