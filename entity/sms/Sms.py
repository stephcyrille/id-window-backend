import requests
import json


class Sms:
    BASE_URL = 'https://api.orange.com'

    client_id = ''

    client_secret = ''

    credentials = ''

    token = ''

    def __init__(self):
        self.credentials = self.client_id + ':' + self.client_secret



    def sendSMS(self, senderAddress, receiverAddress, message, senderName='DGSN'):
        self.getClientTokenKey()
        proxies = {
                    'https': None,
                    'http': None
                }

        url = "https://api.orange.com/smsmessaging/v1/outbound/" + senderAddress + "/requests"

        headers = {
                    'Authorization' : 'Bearer ' + self.getTokenKey(),  # here we will ourselfs encode credentials
                    'Content-Type': 'application/json'
        }

        body = {
                "outboundSMSMessageRequest" : {
                    "address"                 : receiverAddress,
                    "senderAddress"           : senderAddress,
                    "senderName"              : senderName,
                    "outboundSMSTextMessage" : {
                        "message"               :  message
                    }
                }
        }

        print(json.dumps(body))

        r = requests.post(url, headers=headers, data=json.dumps(body), proxies=proxies)
        rJson = r.json()

        print(rJson)


    def getClientTokenKey(self):

        proxies = {
                    'https': None,
                    'http': None
                }

        url = self.BASE_URL + '/oauth/v2/token'

        headers = {
                    'Authorization' : 'Basic b1NzWkJuVUdEQUJGUUxtMVVrOUlTUGxGT1JOSjBFZ0k6ZTFZQXU4Y0dvNjJSREVndQ==',  # here we will ourselfs encode credentials
                    'Content-Type': 'application/x-www-form-urlencoded'
        }

        payload = {'grant_type': 'client_credentials'}

        r = requests.post(url, headers=headers, data=payload, proxies=proxies)

        rJson = r.json()

        if(rJson['access_token']):
            token = rJson['access_token']
            self.setTokenKey(token)

        return rJson


    def setTokenKey(self, token):
        self.token = token

    def getTokenKey(self):
        return self.token