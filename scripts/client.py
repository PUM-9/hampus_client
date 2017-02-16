#!/usr/bin/env python
import rospy
from chat_server.msg import Message

nam = "Anon"
muted = []


def receive(data):
    global name
    if data.sender not in muted and data.message:
        if len(data.sender) > 10:
            data.sender = data.sender[:9]
        print "%s: %s" % (data.sender, data.message)


pub = rospy.Publisher('chat_in', Message, queue_size=10)
rospy.init_node('hampus_client', anonymous=True)
rospy.Subscriber('chat_out', Message, receive)


tmp = raw_input("Your name is: ")
if tmp:
    name = tmp
muted.append(name)

while not rospy.is_shutdown():
    text = raw_input()
    if text[0] == "/":
        text = text[0:]
        text = text.split(' ')
        if text[0] == "mute":
            muted.append(text[1])
            print "muted %s" % text[1]
    else:
        pub.publish(sender=name, message=text)
