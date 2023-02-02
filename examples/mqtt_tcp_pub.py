"""
MQTT is used for synchronous communications where each question is responded with a single answer,
for example remote procedure calls (RPCs).
Like Pipeline, it also can perform load-balancing.
This is the only reliable messaging pattern in the suite, as it automatically will retry if a request is not matched with a response.

"""
import sys
import pynng
import curio

helper = "Usage:\n\tmqttpub.py <topic> <qos> <payload>"

address = "mqtt-tcp://192.168.1.238:1883"

async def main():
  with pynng.Mqtt_tcp(address) as mqtt:
    print(f"Make a connect msg")
    connmsg = pynng.Mqttmsg()
    connmsg.set_packet_type(1) # 0x01 Connect
    connmsg.set_connect_proto_version(4) # MqttV311
    mqtt.dial_msg(address, connmsg)
    print(f"Connection packet sent.")
    pubmsg = pynng.Mqttmsg()
    pubmsg.set_packet_type(3) # 0x03 Publish
    pubmsg.set_publish_payload(sys.argv[3])
    pubmsg.set_publish_topic(sys.argv[1])
    pubmsg.set_publish_qos(int(sys.argv[2]))
    await mqtt.asend_msg(pubmsg)
    print(f"Publish packet sent.")

if __name__ == "__main__":
  if len(sys.argv) != 4:
    print(helper)
    exit(0)
  try:
    curio.run(main)
  except KeyboardInterrupt:
    # that's the way the program *should* end
    exit(0)
