import paho.mqtt.client as mqtt



def on_log(client, userdata, level, buf):
    print("log: ", buf)

# The callback for when the client receives a CONNACK response from the server.
def on_connect(client, userdata, flags, rc):
    client.subscribe([
        ('test', 2)
    ])

# The callback for when a PUBLISH message is received from the server.
def on_message(client, userdata, msg):
    # print(msg.topic," ",data)
    # print('timestamp', msg.timestamp)
    # print('state', msg.state)
    # print('info', msg.info)
    print('payload', msg.payload)

client = mqtt.Client()
client.on_log=on_log
client.on_connect = on_connect
client.on_message = on_message

client.username_pw_set('server', 'pass_anykey21')
client.connect('localhost')

client.loop_forever()
