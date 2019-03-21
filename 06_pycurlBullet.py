#!/usr/bin/env python3
import requests
import json
import os

ACCESS_TOKEN = "o.Wk5VZJUjNRdUF4vRJ7VanyFGQMOoexTY"


def send_notification_via_pushbullet(title, body):
    """ Sending notification via pushbullet.
        Args:
            title (str) : title of text.
            body (str) : Body of text.
    """
    data_send = {"type": "note", "title": title, "body": body}

    resp = requests.post('https://api.pushbullet.com/v2/pushes', data=json.dumps(data_send),
                         headers={'Authorization': 'Bearer ' + ACCESS_TOKEN,
                                  'Content-Type': 'application/json'})
    if resp.status_code != 200:
        raise Exception('Something wrong')
    else:
        print('complete sending')

# main function


def main():
    ip_address = os.popen('hostname -I').read()
    send_notification_via_pushbullet(ip_address, "From Raspberry Pi - Reboot")


# Execute
main()
