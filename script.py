import fbchat
from fbchat import Client
from getpass import getpass
import time

passw = input("passw: ")
username = input("username: ")
id = "100053264810540"
client = fbchat.Client(username, passw)
# friends = client.searchForUsers("Bogdan Dovzhnyi")
# friend = friends[0]
print(friend.uid)

while True:
    try:
        messages = client.fetchThreadMessages(thread_id=id, limit=20)
    except:
        print("disconnected, retrying...")
        time.sleep(60)
        client = fbchat.Client(username, passw)
        messages = client.fetchThreadMessages(thread_id=id, limit=20)

    for message in messages:
        if message.author != id:
            break
        # elif "🖕" in message.text and message.author == id:
        elif message.author == id:
            try:
                sent = client.send(fbchat.models.Message("🖕"), id)
            except:
                print("disconnected, retrying...")
                time.sleep(60)
                client = fbchat.Client(username, passw)
                sent = client.send(fbchat.models.Message("🖕"), id)

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
