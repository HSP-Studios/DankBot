# --- CONFIGURABLE SECRETS ---
DISCORD_TOKEN = "YOUR_DISCORD_TOKEN_HERE"
DISCORD_CHANNEL_URL = "YOUR_DISCORD_CHANNEL_URL_HERE"
COOKIE_STRIPE_MID = "YOUR_STRIPE_MID_HERE"
COOKIE_DCFDUID = "YOUR_DCFDUID_HERE"
COOKIE_SDCFDUID = "YOUR_SDCFDUID_HERE"
COOKIE_CFRUID = "YOUR_CFRUID_HERE"
COOKIE_CFUVID = "YOUR_CFUVID_HERE"
COOKIE_CF_CLEARANCE = "YOUR_CF_CLEARANCE_HERE"
# --- END CONFIGURABLE SECRETS ---

import requests
import json
import time
import random

url = DISCORD_CHANNEL_URL

headers = {
    "accept": "*/*",
    "accept-language": "en-US,ja;q=0.9,en-AU;q=0.8",
    "authorization": DISCORD_TOKEN,
    "content-type": "application/json",
    "origin": "https://discord.com",
    "priority": "u=1, i",
    "referer": "https://discord.com/channels/1365964662050521098/1366700749672677446",
    "sec-ch-ua": '"Not?A_Brand";v="99", "Chromium";v="130"',
    "sec-ch-ua-mobile": "?0",
    "sec-ch-ua-platform": '"Windows"',
    "sec-fetch-dest": "empty",
    "sec-fetch-mode": "cors",
    "sec-fetch-site": "same-origin",
    "x-debug-options": "bugReporterEnabled",
    "x-discord-locale": "en-US",
    "x-discord-timezone": "Australia/Brisbane",
    "x-super-properties": "eyJvcyI6IldpbmRvd3MiLCJicm93c2VyIjoiRGlzY29yZCBDbGllbnQiLCJyZWxlYXNlX2NoYW5uZWwiOiJzdGFibGUiLCJjbGllbnRfdmVyc2lvbiI6IjEuMC45MTg5Iiwib3NfdmVyc2lvbiI6IjEwLjAuMjI2MzUiLCJvc19hcmNoIjoieDY0IiwiYXBwX2FyY2giOiJ4NjQiLCJzeXN0ZW1fbG9jYWxlIjoiZW4tVVMiLCJoYXNfY2xpZW50X21vZHMiOmZhbHNlLCJicm93c2VyX3VzZXJfYWdlbnQiOiJNb3ppbGxhLzUuMCAoV2luZG93cyBOVCAxMC4wOyBXaW42NDsgeDY0KSBBcHBsZVdlYktpdC81MzcuMzYgKEtIVE1MLCBsaWtlIEdlY2tvKSBkaXNjb3JkLzEuMC45MTg5IENocm9tZS8xMzAuMC42NzIzLjE5MSBFbGVjdHJvbi8zMy40LjAgU2FmYXJpLzUzNy4zNiIsImJyb3dzZXJfdmVyc2lvbiI6IjMzLjQuMCIsIm9zX3Nka192ZXJzaW9uIjoiMjI2MzUiLCJjbGllbnRfYnVpbGRfbnVtYmVyIjozOTUxMzQsIm5hdGl2ZV9idWlsZF9udW1iZXIiOjYyNTU5LCJjbGllbnRfZXZlbnRfc291cmNlIjpudWxsfQ=="
}

cookies = {
    "__stripe_mid": COOKIE_STRIPE_MID,
    "__dcfduid": COOKIE_DCFDUID,
    "__sdcfduid": COOKIE_SDCFDUID,
    "__cfruid": COOKIE_CFRUID,
    "_cfuvid": COOKIE_CFUVID,
    "cf_clearance": COOKIE_CF_CLEARANCE
}

def make_command_data():

    command = "pls beg " + str(random.randint(1000, 9999))
    nonce = str(int(time.time() * 1000)) + str(random.randint(100, 999))
    return {
        "mobile_network_type": "unknown",
        "content": command,
        "nonce": nonce,
        "tts": False,
        "flags": 0
    }

# Send multiple messages with randomized command and nonce
for _ in range(4):
    data = make_command_data()
    response = requests.post(url, headers=headers, cookies=cookies, json=data)
    print("Status:", response.status_code)
    print("Response:", response.text)
    print("Headers:", response.headers)
    time.sleep(0)