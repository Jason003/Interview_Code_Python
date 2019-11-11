import requests
import json


def replayJson():
    with open('./request-2.json', 'r') as f:
        infos = json.load(f)
        for info in infos:
            requestInfo = info['request']
            r = requests.request(method=requestInfo['method'], url='https://api.stripe.com' + requestInfo['url'],
                                 headers=requestInfo['headers'], data=requestInfo['body'])
            responseInfo = info['response']
            print(r.json())


replayJson()
# print('==================')


def replayJson2():
    toReplace = {}
    with open('./request-2.json', 'r') as f:
        infos = json.load(f)
        for info in infos:
            requestInfo = info['request']
            responseInfo = info['response']
            for before, after in toReplace.items():
                requestInfo['url'] = requestInfo['url'].replace(before, after)
                requestInfo['body'] = requestInfo['body'].replace(before, after)

            r = requests.request(method=requestInfo['method'], url='https://api.stripe.com' + requestInfo['url'],
                                 headers=requestInfo['headers'], data=requestInfo['body'])
            response = r.json()
            bodyInfo = json.loads(responseInfo['body'])
            if response['id'] != bodyInfo['id']:
                toReplace[bodyInfo['id']] = response['id']
            # print(r.status_code == responseInfo['code'])


# replayJson2()
