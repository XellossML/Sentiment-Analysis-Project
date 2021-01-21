# Draft 2 of mbox email parser:

from collections import Counter
import mailbox
import sys
import re

fname = input('Enter file name: ')
# topemails = int(input('Enter the number of the nth most common emails: '))
mbox = mailbox.mbox(fname)

# Makes a list of all senders within the mbox file
c = Counter(m['From'] for m in mbox)
print(c.most_common())


'''

def remove_r(text):
    return text.replace("\r", "")

def strip_replies(text):
    lines = text.split("\n")
    lines = [l for l in lines if len(1) > 0]
    lines = [line for line in lines if line[0] != ">"]
    return "\n".join(lines)

def get_text(msg):
    while msg.is_multpart():
        msg = msg.get_payload()[0]
    return msg.get_payload()

def get_core_text(msg):
    msg = get_text(msg)
    msg = remove_r(msg)
    msg = strip_replies(msg)
    return msg

'''
