#!/usr/bin/env python
import rospy
from chat_server.msg import Message

nam = "Anon"


def receive(data):
    global name
    if data.sender != name:
        print "%s: %s" % (data.sender, data.message)


pub = rospy.Publisher('chat_in', Message, queue_size=10)
rospy.init_node('hampus_client', anonymous=True)
rospy.Subscriber('chat_out', Message, receive)


tmp = raw_input("Your name is: ")
if tmp:
    name = tmp

while not rospy.is_shutdown():
    text = raw_input()
    pub.publish(sender=name, message=text)