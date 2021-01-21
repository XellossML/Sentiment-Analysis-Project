# Reads only the messages within the mbox file from Google 
# Still a work in progress

import mailbox
import quopri, base64


def getcharsets(msg):
    charsets = set({})
    for c in msg.get_charsets():
        if c is not None:
            charsets.update([c])
        return charsets

def handleerror(errmsg, emailmsg, cs):
    print()
    print(errmsg)
    print("This error occured while decoding with ", cs ," charset.")
    print("These charsets were found in the one email.", getcharsets(emailmsg))
    print("This is the subject:", emailmsg['subject'])
    print("This is the sender:", emailmsg['From'])

def getbodyfromemail(msg):
    body = None
    if msg.is_multipart():
        for part in msg.walk():
            if part.is_multipart():
                for subpart in part.walk():
                    if subpart.get_content_type() == 'text/plain':
                        body = subpart.get_payload(decode = True)
                        charset = subpart.get_payload(decode = True)
            elif part.get_content_type() == 'text/plain':
                body = part.get_payload(decode = True)
                charset = part.get_charset()

    elif msg.get_content_type() == 'text/plain':
        body = msg.get_payload(decode=True)
       

    for charset in getcharsets(msg):
        try:
            body = body.decode(charset)
        except UnicodeDecodeError:
            handleerror("UnicodeDecodeError: encountered.", msg, charset)
        except AttributeError:
            handleerror("AttributeError: encountered", msg, charset)
    
    return body

mbox_file = input("Enter file name: ")
bodylist = []
for thisemail in mailbox.mbox(mbox_file):
    body = getbodyfromemail(thisemail)
    body = str(body)
    bodylist.append(body)
    partially_cleaned_emails = open('Partially-Clean-Emails-Pro.txt', 'w')
    partially_cleaned_emails.write(body)
    partially_cleaned_emails.close()

most_recent_email = bodylist[-1]
testemail = open('sentimentemailsample.txt', 'w')
testemail.write(most_recent_email)
testemail.close()

'''
import mailbox
def print_payload(message):
    if message.is_multipart():
        for part in message.get_payload():
            print(part)
    else:
        print(message.get_payload(decode=True))

mbox = mailbox.mbox('All-mail-Including-Spam-and-Trash.mbox')
for message in mbox:
    print(message['subject'])
    print(message.get_payload)
'''


'''
import mailbox

mbox_file = input('Enter File Name: ')
for message in mailbox.mbox(mbox_file):
    mstring = message.as_string()
    print(mstring)
'''

'''
import os, mailbox, sys, pprint

print("Reading emails: ")
mbox_file = input('Enter File Name: ')
print('Processing', mbox_file)
mbox = mailbox.mbox(mbox_file)

for key in mbox.iterkeys():
    try:
        message = mbox[key]
    except mbox.errors.MessageParseError:
        continue

    print("From:", message['from'])
    print("To:", message['to'])
    print("Subject: ", str(message['Subject']))
    print('---------------------------')
    print('Body\n')
    print(message)
    print('*********************')
'''
