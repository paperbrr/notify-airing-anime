import requests
import xml.etree.ElementTree as ET
import time
import json
from format_json import format_json
import os

url = 'https://www.livechart.me/feeds/episodes'
webhook_token = os.environ['WEBHOOKTOKEN']

def modify_previous_data(action, data, data_type):
    file_path = 'previous_data.json'
    if action == 'retrieve':
        with open(file_path, 'r') as f:
            previous = json.load(f)
        return (previous[data_type] if data_type != 'both' else previous)
    elif action == 'edit':
        previous = modify_previous_data('retrieve', None, 'both')
        previous[data_type] =  data
        with open(file_path, 'w') as f:
            json.dump(previous, f)

def send_set(airing_list):
    global webhook_token
    last_sent = modify_previous_data('retrieve', None, 'last_sent')
    for i in range(len(airing_list)):
        if airing_list[i]['Title'] == last_sent:
            modify_previous_data('edit', airing_list[0]['Title'], 'last_sent')
            break
        requests.post(webhook_token, json = format_json(airing_list[i]['Title'], airing_list[i]['Category'], airing_list[i]['Link'], airing_list[i]['Thumbnail']))
        time.sleep(1)
         
 
def airing_to_dict(root):
    now_airing = []
    for channel in root:
        for item in channel:
            if item.tag == 'item':
                now_airing.append({'Title':item[2].text,
                                   'PubDate':item[3].text,
                                   'Category': 'OVA' if item[4].text[6:10] == 'OVAs' else ('Episode' if item[4].text[6:16] == 'Television' else item[4].text[6:12]),
                                   'Link':item[1].text,
                                   'Thumbnail':item[6].text})
    return now_airing

def get_data():
    global url
    last_modified = modify_previous_data('retrieve', None, 'last_modified')
    new_data = requests.get(url, headers = {'If-Modified-Since' : last_modified})
    if new_data.status_code == 304:
        print('Not updated yet.')
        return False
    elif new_data.status_code == 200:
        print('Updated.')
        modify_previous_data('edit', new_data.headers['last-modified'], 'last_modified')
        send_set(airing_to_dict(ET.fromstring(new_data.content)))
    else:
        print('An unknown error occurred.')
        return False

#keep_alive()

while True:
    print(f'last iteration at {time.strftime("%H:%M:%S", time.localtime())}')
    if get_data():
        pass
    else:
        time.sleep(600)


