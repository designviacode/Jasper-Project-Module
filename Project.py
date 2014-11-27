# -*- coding: utf-8-*-
import random
import re

WORDS = ["SEMESTER", "BEST", "PROJECT"]


def handle(text, mic, profile):
    """
        Responds to user-input, typically speech text, by relaying the
        meaning of life.

        Arguments:
        text -- user-input, typically transcribed speech
        mic -- used to interact with the user (for both input and output)
        profile -- contains information related to the user (e.g., phone
                   number)
    """
    messages = ["Its Simple, It's Me, I'm the Best Project ha ha ha",
                "It's Me, you Idiot or what ?"]

    message = random.choice(messages)

    mic.say(message)


def isValid(text):
    """
        Returns True if the input is related to the meaning of life.

        Arguments:
        text -- user-input, typically transcribed speech
    """
    return bool(re.search(r'\bminor project\b', text, re.IGNORECASE))
