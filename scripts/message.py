#!/usr/bin/env python
import datetime


class ChatMessage:
    def __init__(self, sender, message):
        self.sender = sender
        self.message = message
        self.received = datetime.datetime.now()