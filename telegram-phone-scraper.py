from telethon.sync import TelegramClient, events
import os
import phonenumbers
import json
from collections import defaultdict

CONFIG_FILE = "config.json"

# Function to get API credentials
def get_credentials():
    if os.path.exists(CONFIG_FILE):
        with open(CONFIG_FILE, "r") as file:
            config = json.load(file)
            return config["API_ID"], config["API_HASH"], config["PHONE_NUMBER"]
    else:
        api_id = input("Enter your API ID: ")
        api_hash = input("Enter your API HASH: ")
        phone_number = input("Enter your PHONE NUMBER: ")

        config = {
            "API_ID": api_id,
            "API_HASH": api_hash,
            "PHONE_NUMBER": phone_number
        }

        with open(CONFIG_FILE, "w") as file:
            json.dump(config, file)

        return api_id, api_hash, phone_number

# Get API credentials
API_ID, API_HASH, PHONE_NUMBER = get_credentials()

# Create the client
client = TelegramClient("session_name", API_ID, API_HASH)

# Function to determine country
def get_country(phone_number):
    try:
        parsed = phonenumbers.parse(phone_number)
        return phonenumbers.region_code_for_number(parsed)
    except phonenumbers.phonenumberutil.NumberParseException:
        return None

# Function to get desktop path
def get_desktop_path():
    return os.path.join(os.path.expanduser("~"), "Desktop")

# Start the bot
async def main():
    await client.start(PHONE_NUMBER)
    print("✅ Bot started! Send a message in a group to collect phone numbers.")

# Message handler (bot reacts when you send a message)
@client.on(events.NewMessage(outgoing=True))
async def handler(event):
    chat = await event.get_chat()
    if chat.broadcast:
        print("⚠ This is a channel! Unable to collect participants.")
        return

    chat_name = chat.title.replace(" ", "_")
    file_path = os.path.join(get_desktop_path(), f"{chat_name}.txt")

    participants = await client.get_participants(chat)

    countries = defaultdict(list)
    anonym_numbers = []

    total_users = users_with_numbers = users_without_numbers = 0

    for user in participants:
        total_users += 1
        username = user.username if user.username else user.first_name

        if user.phone:
            phone = user.phone
            country = get_country(f"+{phone}")
            if country:
                if phone.startswith("888"):
                    anonym_numbers.append(f"{phone} - @{username}")
                else:
                    countries[country].append(f"{phone} - @{username}")
            users_with_numbers += 1
        else:
            users_without_numbers += 1

    with open(file_path, "w", encoding="utf-8") as file:
        if anonym_numbers:
            file.write("Anonim NFT Numbers:\n" + "\n".join(anonym_numbers) + "\n\n")
        for country, numbers in countries.items():
            if numbers:
                file.write(f"{country}:\n" + "\n".join(numbers) + "\n\n")

    print(f"✅ Data saved on your desktop: {file_path}")
    print(f"📊 Total: {total_users}, 📞 With numbers: {users_with_numbers}, 🚫 Without numbers: {users_without_numbers}")

with client:
    client.loop.run_until_complete(main())
    client.run_until_disconnected()