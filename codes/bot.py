from telethon import TelegramClient, events
import  re
from g_search import main as g_main
import  time
import configparser
from wordcloud_conventor import wordcloud_conventor
import os.path
# Remember to use your own values from my.telegram.org!

# Reading Configs
config = configparser.ConfigParser()
config.read("config.ini")
api_id = config['Telegram']['api_id']
api_hash = config['Telegram']['api_hash']
bot_token = config['Telegram']['bot_token']

client =  TelegramClient('bot', api_id, api_hash)
regex_lsi = r"key\s?:\s?"

@client.on(events.NewMessage)
async def main(event):
    print("event handel")
    print(event)
    # print(event.message.peer_id.user_id)
    # Getting information about yourself
    client_message = event.message.message

    if(client_message == "/start")  : 
        text = """به بات **a28** خوش امدید.
        هدف این بات سهولت در پیداکردن کلمه کلیدی در هنگام سئو سایت هست.
        
        
        فقط کافیه کلمه کلیدی خودتو سرچ کنی. تا یه لیستی بلند بالا به همراه ابرکلمه اون دریافت کنید.
        **فقط حواستون باشه کلمه کلیدی باید بیش از سه حرف باشد.**"""
        sapmple ='This message has **bold**, `code`, __italics__ and ''a [nice website](https://example.com)!'
        message = await client.send_message(
            event.message.peer_id.user_id,
            text,
            link_preview=False
            )
    # sum(1 for _ in  re.finditer(regex_lsi, client_message, re.MULTILINE))>0
    if len(client_message)>=3 and client_message != "/start":
        keyword = re.sub(regex_lsi,"",client_message)
        text = """کلمه کلیدی شما : {}""".format(keyword)
        message = await client.send_message(
            event.message.peer_id.user_id,
            text,
            link_preview=False
            )
        send_me = await client.send_message(
            197418176,
            text,
            link_preview=False
            )
        message = await client.send_message(
            event.message.peer_id.user_id,
            "ممکنه چند دقیقه طول بکشه،صبور باشید!\n تموم که شد یه فایل براتون اینجا ارسال میشه .",
            link_preview=False
            )
        rec_file_name = 'rec'+str(int(time.time()))+"_a28_ir.txt"
        rel_file_name = 'rel'+str(int(time.time()))+"_a28_ir.txt"

        res_rec,res_rel = g_main(search_val=keyword,rec_search_dir=rec_file_name,rel_word_search_dir=rel_file_name) 
        # TODO : check rel_file_name sometime not avaiable
        if os.path.isfile(rel_file_name):
            with open(rec_file_name, 'a') as outfile:
                with open(rel_file_name) as infile:
                    for line in infile:
                        outfile.write(line)
                #     infile.close()
                outfile.close

        # print(res)
        await client.send_file(event.message.peer_id.user_id, rec_file_name)
        wordcloudFileName = wordcloud_conventor(fileLocation=rec_file_name)
        await client.send_file(event.message.peer_id.user_id, wordcloudFileName)
        #TODO:  remove file after send
        message = await client.send_message(
            event.message.peer_id.user_id,"ممنونم از همراهیتون :)",
            link_preview=False)
    else :
        message = await client.send_message(
            event.message.peer_id.user_id,
            ':/ میشه بیش از سه حرف برامون تایپ کنی ! آخه خیلی کمه ',
            link_preview=False
            )


client.start(bot_token=bot_token)
client.run_until_disconnected()



    # print(sum(1 for _ in  re.finditer(regex_lsi, client_message, re.MULTILINE)))
    # # "me" is a user object. You can pretty-print
    # # any Telegram object with the "stringify" method:
    # print(me.stringify())

    # # When you print something, you see a representation of it.
    # # You can access all attributes of Telegram objects with
    # # the dot operator. For example, to get the username:
    # username = me.username
    # print(username)
    # print(me.phone)

    # # You can print all the dialogs/conversations that you are part of:
    # async for dialog in client.iter_dialogs():
    #     print(dialog.name, 'has ID', dialog.id)

    # # You can send messages to yourself...
    # await client.send_message('me', 'Hello, myself!')
    # # ...to some chat ID
    # await client.send_message(-100123456, 'Hello, group!')
    # # ...to your contacts
    # await client.send_message('+34600123123', 'Hello, friend!')
    # # ...or even to any username
    # await client.send_message('username', 'Testing Telethon!')

    # You can, of course, use markdown in your messages:
    

    # Sending a message returns the sent message object, which you can use
    # print(message.raw_text)

    # You can reply to messages directly if you have a message object
    # await message.reply('Cool!')

    # Or send files, songs, documents, albums...
    # await client.send_file('me', '/home/me/Pictures/holidays.jpg')

    # You can print the message history of any chat:
    # async for message in client.iter_messages('me'):
    #     print(message.id, message.text)

    #     # You can download media from messages, too!
    #     # The method will return the path where the file was saved.
    #     if message.photo:
    #         path = await message.download_media()
    #         print('File saved to', path)  # printed after download is done

# with client:
#     client.loop.run_until_complete(main())

