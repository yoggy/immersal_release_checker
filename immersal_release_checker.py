#!/usr/bin/python3
import sys
import os
import yaml
import urllib
import requests
import re
import pickle
import shelve
import json

immersal_sdk_config_url = "https://developers.immersal.com/js/sdkconfig.js"

os.chdir(os.path.dirname(os.path.abspath(__file__)))

# read config.yaml
with open("config.yaml", "r") as f:
    config = yaml.safe_load(f)
    slack_webhook_url = config["slack_webhook_url"]

# GET sdkconfig.js
res = requests.get(immersal_sdk_config_url)
lines = res.text.splitlines()
for l in lines:
    if "var SDK_VERSION" in l:
        # l == 'var SDK_VERSION         = "1_16_1";'
        m = re.match(r'^.+\"(.+)\";$', l)

        #print(m.groups()[0])
        immersal_sdk_version = m.groups()[0]

# check lastest version
s = shelve.open('.dict.shelve')
if "immersal_sdk_version" in s and s["immersal_sdk_version"] == immersal_sdk_version:
    s.close()
    sys.exit(0)

s["immersal_sdk_version"] = immersal_sdk_version
s.close()

# POST
json_body = {"text": f"{immersal_sdk_version} released!!"}
h = {'Content-Type': 'application/json'}
res = requests.post(slack_webhook_url, headers=h, json=json_body)

print(res)
