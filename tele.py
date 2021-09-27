# importing all required libraries
import telebot
from telethon.sync import TelegramClient
from telethon.tl.functions.users import GetFullUserRequest
from telethon.tl.types import InputPeerUser, InputPeerChannel
from telethon import TelegramClient, sync, events

# get your api_id, api_hash, token
# from telegram as described above
api_id = 8954715
api_hash = '305c02d4bd5415ab2e3b962817f88ce6'
token = '2010162695:AAFNpjPZcScOByvdjY3cWULMhcjJhN5Zq6c'
message = "Hello World!"

# your phone number
phone = '+989912147018'

# creating a telegram session and assigning
# it to a variable client


def main():

    with TelegramClient('anon', api_id, api_hash) as client:
        client.loop.run_until_complete(client.send_message('me', 'Hello, myself!'))


if __name__ == '__main__':
    main()
