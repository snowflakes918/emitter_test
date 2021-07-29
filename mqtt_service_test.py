try:
    from .emitter import Client
except ImportError:
    from emitter import Client
import tkinter

emitter = Client()
root = tkinter.Tk()

channel_key = tkinter.StringVar(root, value="input password")
channel = tkinter.StringVar(root, value="input channel")
text_message = tkinter.StringVar(root, value="Hello world")



def connect():
    emitter.connect(host="api.emitter.io", port=8080, secure=False)
    # emitter.connect()

    emitter.on_connect = lambda: result_text.insert("0.0", "Connected\n\n")
    emitter.on_disconnect = lambda: result_text.insert("0.0", "Disconnected\n\n")
    emitter.on_presence = lambda p: result_text.insert("0.0", "Presence message on channel: '" + str(p) + "'\n\n")
    emitter.on_message = lambda m: result_text.insert("0.0",
                                                      "Message received on default handler, destined to " + m.channel + ": " + m.as_string() + "\n\n")
    emitter.on_error = lambda e: result_text.insert("0.0", "Error received: " + str(e) + "\n\n")
    emitter.on_me = lambda me: result_text.insert("0.0", "Information about Me received: " + str(me) + "\n\n")
    emitter.loop_start()


def disconnect():
    emitter.loop_stop()
    emitter.disconnect()


def subscribe():
    str_key = channel_key.get()
    str_channel = channel.get()
    emitter.subscribe(str_key,
                      str_channel,
                      optional_handler=lambda m: result_text.insert("0.0",
                                                                    "Message received on handler for " + str_channel + ": " + m.as_string() + "\n\n")
                      )
    result_text.insert("0.0", "Subscribtion to '" + str_channel + "' requested.\n\n")


def unsubscribe():
    str_key = channel_key.get()
    str_channel = channel.get()
    emitter.unsubscribe(str_key, str_channel)
    result_text.insert("0.0", "Unsubscribtion to '" + str_channel + "' requested.\n\n")


def presence():
    str_key = channel_key.get()
    str_channel = channel.get()
    emitter.presence(str_key, str_channel, status=True,
                     changes=True)  # optional_handler=lambda p: result_text.insert("0.0", "Optional handler: '" + str(p) + "'\n\n"))
    result_text.insert("0.0", "Presence on '" + str_channel + "' requested.\n\n")


def message():
    emitter.publish(channel_key.get(), channel.get(), text_message.get(), {})
    result_text.insert("0.0", "Test message send through '" + channel.get() + "'.\n\n")


def me():
    emitter.me()


# UI Interface
root.title('Emitter test')

# Col 1
tkinter.Label(root, text="Channel : ").grid(column=1, row=1)
channel_entry = tkinter.Entry(root, width=40, textvariable=channel)
channel_entry.grid(column=1, row=2)

tkinter.Label(root, text="Channel key : ").grid(column=1, row=3)
channel_key_entry = tkinter.Entry(root, width=40, textvariable=channel_key)
channel_key_entry.grid(column=1, row=4)

tkinter.Label(root, text="Message : ").grid(column=1, row=5)
message_entry = tkinter.Entry(root, width=40, textvariable=text_message)
message_entry.grid(column=1, row=6)

# Col 2
connect_button = tkinter.Button(root, text="Connect", width=30, command=connect)
connect_button.grid(column=2, row=1)

disconnect_button = tkinter.Button(root, text="Disconnect", width=30, command=disconnect)
disconnect_button.grid(column=2, row=2)

# Col 3
send_button = tkinter.Button(root, text="Publish to channel", width=30, command=message)
send_button.grid(column=3, row=1)

subscribe_button = tkinter.Button(root, text="Subscribe", width=30, command=subscribe)
subscribe_button.grid(column=3, row=2)

unsubscribe_button = tkinter.Button(root, text="Unsubscribe", width=30, command=unsubscribe)
unsubscribe_button.grid(column=3, row=3)

# Col 4
presence_button = tkinter.Button(root, text="Presence", width=30, command=presence)
presence_button.grid(column=4, row=1)

me_button = tkinter.Button(root, text="Me", width=30, command=me)
me_button.grid(column=4, row=2)

# Text area
result_text = tkinter.Text(root, height=30, width=120)
result_text.grid(column=1, row=15, columnspan=4)

root.mainloop()
