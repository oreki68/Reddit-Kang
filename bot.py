from config import bot, reddit_personal_use_script, reddit_secret, agent, subreddit, channel_id, main_channel_id
from telethon import events, Button
import asyncio
import asyncpraw

reddit = asyncpraw.Reddit(client_id = reddit_personal_use_script, client_secret = reddit_secret, user_agent = agent)

try:
    channel_id = int(channel_id)
except:
    channel_id = channel_id



#buttons=[Button.inline('approve', b'approve'),Button.inline('reject', b'reject')]
#buttons=[Button.inline("🍆 0", data="e1:0:0:0"), Button.inline("❤️ 0", data="e2:0:0:0"), Button.inline("👎🏻 0", data="e3:0:0:0")]  

loop = asyncio.get_event_loop()
async def kang_reddit():
    channel = await bot.get_entity(channel_id)
    last = ''
    while True:
        subred = await reddit.subreddit(subreddit)
        new = subred.new(limit = 1)
        async for i in new:
            if i.url != last:
                try:
                    split = i.title.split(" ")
                    await bot.send_message(
                    channel, 
                    f"{i.title}\n@{main_channel_id}", 
                    file=i.url
                )
                    await bot.send_message(
                    channel,
                    f"{i.title}\n@{main_channel_id}",
                    file=i.url,
                    name=split[0],
                    force_document=True,
                    buttons=[Button.inline('approve', b'approve'),Button.inline('reject', b'reject')]
                )
                    last = i.url
                except Exception as e:
                    print(e)
        await asyncio.sleep(60)    
        print("nothing")

@bot.on(events.NewMessage(pattern="/start"))
async def start(event):
    await bot.send_message(event.chat_id, "Bot is Running")

@bot.on(events.CallbackQuery(pattern=b"e1"))
async def emoji1(event):
    data = event.data.decode('utf-8')
    data_split = data.split(':')
    new_count = int(data_split[1]) +1
    await event.edit(buttons=[
        Button.inline(f"🍆 {new_count}", data=f"e1:{new_count}:{data_split[2]}:{data_split[3]}"), 
        Button.inline(f"❤️ {data_split[2]}", data=f"e2:{new_count}:{data_split[2]}:{data_split[3]}"), 
        Button.inline(f"👎🏻 {data_split[3]}", data=f"e3:{new_count}:{data_split[2]}:{data_split[3]}")
    ])

@bot.on(events.CallbackQuery(pattern=b"e2"))
async def emoji2(event):
    data = event.data.decode('utf-8')
    data_split = data.split(':')
    new_count = int(data_split[2]) + 1
    await event.edit(buttons=[
        Button.inline(f"🍆 {data_split[1]}", data=f"e1:{data_split[1]}:{new_count}:{data_split[3]}"), 
        Button.inline(f"❤️ {new_count}", data=f"e2:{data_split[1]}:{new_count}:{data_split[3]}"), 
        Button.inline(f"👎🏻 {data_split[3]}", data=f"e3:{data_split[1]}:{new_count}:{data_split[3]}")
    ])

@bot.on(events.CallbackQuery(pattern=b"e3"))
async def emoji3(event):
    data = event.data.decode('utf-8')
    data_split = data.split(':')
    new_count = int(data_split[3]) + 1
    await event.edit(buttons=[
        Button.inline(f"🍆 {data_split[1]}", data=f"e1:{data_split[1]}:{data_split[2]}:{new_count}"), 
        Button.inline(f"❤️ {data_split[2]}", data=f"e2:{data_split[1]}:{data_split[2]}:{new_count}"), 
        Button.inline(f"👎🏻 {new_count}", data=f"e3:{data_split[1]}:{data_split[2]}:{new_count}")
    ])

@bot.on(events.CallbackQuery)
async def click_handler(event):
    # channel = await bot.get_entity(f"t.me/{channel_id}")
    channel = await bot.get_entity(channel_id)
    main_channel = await bot.get_entity(f"t.me/{main_channel_id}")
    message = event.message_id
    userid = event.query.user_id
#     print(userid)
    user_info = await bot.get_entity(userid)
    messages = await bot.get_messages(channel,ids=message)
    try: 
        msg_txt = messages.message
    except:
        pass
    if event.data == b'approve':
        await bot.send_message(main_channel,messages,buttons = [Button.inline("🍆 0", data="e1:0:0:0"), Button.inline("❤️ 0", data="e2:0:0:0"), Button.inline("👎🏻 0", data="e3:0:0:0")])
        await bot.edit_message(channel,message,f"{msg_txt}\n\nthis message was posted by @{user_info.username}")
    elif event.data == b'reject':
        await bot.edit_message(channel,message,f"{msg_txt}\n\nthis message was rejected by @{user_info.username}")

loop.run_until_complete(kang_reddit())

bot.start()

bot.run_until_disconnected()
