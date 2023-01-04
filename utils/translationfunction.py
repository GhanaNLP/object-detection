#!/usr/bin/env python
# coding: utf-8

import urllib.request, json

def translate_class(class_name):
    try:
        url = "https://translation-api.ghananlp.org/v1/translate"

        hdr ={
        # Request headers
        'Content-Type': 'application/json',
        'Cache-Control': 'no-cache',
        'Ocp-Apim-Subscription-Key': '9889af7976cc4aec9cc9a3f4d97e7ab5',
        }

        # Request body
        data =  {
                "in": class_name,
                "lang": "en-tw"
                }
        data = json.dumps(data)
        req = urllib.request.Request(url, headers=hdr, data = bytes(data.encode("utf-8")))

        req.get_method = lambda: 'POST'
        response = urllib.request.urlopen(req)
        return response.read().decode("utf-8")
     
    except Exception as e:
        print(e)
