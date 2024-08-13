#!/usr/bin/python3

import requests
import json
import urllib3
urllib3.disable_warnings()


pano_ip = 'your pano ip'
dg = 'device group name'
new_security_profile = 'new profile'
headers = {
  'Content-Type': 'application/json',
  'X-PAN-KEY': 'your key'
}
get_payload = {}

rule_name_list = ["put your list here"]

for rule_name in rule_name_list:
    get_url = f"https://{pano_ip}/restapi/v10.2/Policies/SecurityPreRules?location=device-group&device-group={dg}&name={rule_name}"
    get_response = requests.request("GET", get_url, headers=headers, data=get_payload, verify=False)
    parsed = json.loads(get_response.text)
    entry = parsed['result']['entry']
    updated_profile_entry = []
    for entryy in entry:
        entryy['profile-setting']['group']['member'] = new_security_profile
        updated_profile_entry= entryy
        put_payload = json.dumps({"entry": updated_profile_entry})
        put_url = f"https://{pano_ip}/restapi/v10.2/Policies/SecurityPreRules?location=device-group&device-group={dg}&name={rule_name}"
        put_response = requests.request("PUT", put_url, headers=headers, data=put_payload, verify=False)
        print(put_response.text)