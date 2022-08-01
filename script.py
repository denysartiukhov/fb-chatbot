import fbchat
from fbchat import Client
from getpass import getpass
import time

passw = input("passw: ")
username = input("username: ")
friend_name = input("friend full name: ")

client = fbchat.Client(username, passw)
friends = client.searchForUsers(friend_name)
friend = friends[0]

while True:
    try:
        messages = client.fetchThreadMessages(thread_id=friend.uid, limit=20)
    except:
        print("disconnected, retrying...")
        time.sleep(60)
        client = fbchat.Client(username, passw)
        messages = client.fetchThreadMessages(thread_id=friend.uid, limit=20)

    for message in messages:
        if message.author != friend.uid:
            break
        # elif "🖕" in message.text and message.author == friend.uid:
        elif message.author == friend.uid:
            try:
                sent = client.send(fbchat.models.Message("🖕"), friend.uid)
            except:
                print("disconnected, retrying...")
                time.sleep(60)
                client = fbchat.Client(username, passw)
                sent = client.send(fbchat.models.Message("🖕"), friend.uid)

            if sent:
                print("Message sent successfully!")
            break
    # if message[0].text == "🖕" and message[0].author == "100053264810540":
    #     sent = client.send(fbchat.models.Message("🖕"), 100053264810540)
    #     if sent:
    #         print("Message sent successfully!")
    print("loop")
    time.sleep(5)

# print(friend.uid)
