from telethon import TelegramClient
from telethon.tl.functions.channels import EditBannedRequest
from telethon.tl.types import ChatBannedRights
import asyncio
import datetime
import time

session_name = "smartbot"
api_id = 10956225
api_hash = '78f50dacad7c81fbe9c7f14baf73f9fc'
chat_id = "@blockchaingalaxyco"


async def clear_chat(client):
    group = chat_id
    deleted_accounts = 0
    while True:
        async for user in client.iter_participants(group):
            if user.deleted:
                try:
                    deleted_accounts += 1
                    await client(EditBannedRequest(group, user, ChatBannedRights(
                        until_date=datetime.timedelta(minutes=1),
                        view_messages=True
                    )))
                except Exception as exc:
                    print(f"Failed to kick one deleted account because: {str(exc)}")
        if deleted_accounts:
            print(f"Kicked {deleted_accounts} Deleted Accounts")
        else:
            print(f"No deleted accounts found in {group}")
        time.sleep(0.5)


with TelegramClient(session_name, api_id, api_hash) as client:
    asyncio.get_event_loop().run_until_complete(clear_chat(client))
