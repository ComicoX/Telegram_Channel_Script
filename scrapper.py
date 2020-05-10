from telethon.sync import TelegramClient
from telethon.tl.functions.messages import GetDialogsRequest
from telethon.tl.types import InputPeerEmpty, InputPeerChannel, InputPeerUser
from telethon.errors.rpcerrorlist import PeerFloodError, UserPrivacyRestrictedError
from telethon.tl.functions.channels import InviteToChannelRequest
import sys
import csv
import traceback
import time

api_id = 00000
api_hash = '000000000pppppp0pppppp0000000'
phone = 000000000

session_name = ''

client = TelegramClient(str(session_name), api_id, api_hash)

client.connect()
if not client.is_user_authorized():
    client.send_code_request(phone)
    client.sign_in(phone, input('Enter the code: '))

print('Fetching Members...')
all_participants = []

#enter target group or channel
target = '000000000000000'

all_participants = client.get_participants(target, aggressive=True)

print('Saving In file...')
with open("members.csv","w",encoding='UTF-8') as f:#Enter your file name.
    writer = csv.writer(f, delimiter=",", lineterminator="\n")
    writer.writerow(['sr. no.','username', 'user id', 'name', 'group', 'group id'])
    i = 0
    for user in all_participants:

        i += 1
        if user.username:
            username = user.username
        else:
            username = ""
        if user.first_name:
            first_name = user.first_name
        else:
            first_name = ""
        if user.last_name:
            last_name = user.last_name
        else:
            last_name = ""
        name = (first_name + ' ' + last_name).strip()
        writer.writerow([i,username, user.id, name, 'group name', 'groupid'])
print('Members scraped successfully.')

