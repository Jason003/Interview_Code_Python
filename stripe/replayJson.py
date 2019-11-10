import requests
import json


def replayJson():

    with open('./request-2.json', 'r') as f:
        infos = json.load(f)
        for info in infos:
            requestInfo = info['request']
            r = requests.request(method=requestInfo['method'], url='https://api.stripe.com' + requestInfo['url'],
                                 headers=requestInfo['headers'], data=requestInfo['body'])
            print(r.json())
            responseInfo = info['response']
            print(r.json() == responseInfo['body'])

# replayJson()

def replayJson2():

    with open('./request-2.json', 'r') as f:
        infos = json.load(f)
        validCustomer = validCharge = validRefund = amount = currency = None
        for info in infos[:2]:
            requestInfo = info['request']
            r = requests.request(method=requestInfo['method'], url='https://api.stripe.com' + requestInfo['url'],
                                 headers=requestInfo['headers'], data=requestInfo['body'])
            response = r.json()
            if response['object'] == 'customer':
                validCustomer = response['id']
            elif response['object'] == 'charge':
                validCharge = response['id']
            if 'amount' in response:
                amount = response['amount']
            if 'currency' in response:
                currency = response['currency']

        body = 'amount={0}&currency={1}&customer={2}'.format(amount, currency, validCustomer)

        for info in infos[2:]:
            requestInfo = info['request']
            if requestInfo['body']:
                requestInfo['body'] = body

            url = requestInfo['url'].strip('/')
            strs = url.split('/')
            for i in range(len(strs) - 1):
                if strs[i] == 'charges':
                    strs[i + 1] = validCharge
                elif strs[i] == 'refunds':
                    strs[i + 1] = validRefund
            newUrl = '/' + '/'.join(strs)
            requestInfo['url'] = newUrl

            r = requests.request(method=requestInfo['method'], url='https://api.stripe.com' + requestInfo['url'],
                                 headers=requestInfo['headers'], data=requestInfo['body'])
            response = r.json()
            if response['object'] == 'refund':
                validRefund = response['id']
            print(response)

replayJson2()