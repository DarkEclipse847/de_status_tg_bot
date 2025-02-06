from telethon import TelegramClient
from telethon.tl.functions.channels import JoinChannelRequest
from telethon.tl.functions.channels import LeaveChannelRequest

import save_ids
import config

client = TelegramClient("session_name", config.api_id, config.api_hash)

async def join_channel(channel_id):
    with client:
        result = client(functions.channels.JoinChannelRequest(
            channel = channel_id
        ))
        await print(result.stringify())

async def leave_channel(channel_id):
    with client:
        result = client(functions.channels.LeaveChannelRequest(
            channel = channel_id
         ))
        await print(result.stringify())

'''iter_dialogs() can cause floodwait errors.'''
'''Be careful, use this rarely!!'''
async def update_ids_csv():
    dialogs_array = []
    async for dialog in client.iter_dialogs():
        dialogs_array.append(dialog.id)
    return save_ids.write_csv([dialogs_array])

async def main():
    await client.send_message("me", "Test?")
    '''Use this to update dialogs.csv'''
    '''dialogs.csv is needed to avoid floodwait errors'''
    '''await update_ids_csv()'''


with client:
    client.loop.run_until_complete(main())
