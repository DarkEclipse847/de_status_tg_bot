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
    last_channel_id = (await client.get_messages(int(config.private_group_id), 1))[0]
    '''last_channel_id = int(last_channel_id)'''
    if save_ids.check_csv(int(last_channel_id.text)) == True:
        async with client:
            async for  message in client.iter_messages(int(last_channel_id.text), 1):
                print(last_channel_id.text)

    '''Use this to update dialogs.csv'''
    '''dialogs.csv is needed to avoid floodwait errors'''
    '''await update_ids_csv()'''


with client:
    client.loop.run_until_complete(main())
