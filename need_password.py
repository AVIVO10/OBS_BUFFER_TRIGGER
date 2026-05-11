#!/usr/bin/env python3
import asyncio, websockets, json, base64, hashlib

PASSWORD = 'YOUR-PASSWORD-HERE'

async def save_replay():
    async with websockets.connect('ws://localhost:4455') as ws:
        hello = json.loads(await ws.recv())
        salt = hello['d']['authentication']['salt']
        challenge = hello['d']['authentication']['challenge']
        secret = base64.b64encode(hashlib.sha256((PASSWORD + salt).encode()).digest()).decode()
        auth = base64.b64encode(hashlib.sha256((secret + challenge).encode()).digest()).decode()
        await ws.send(json.dumps({'op': 1, 'd': {'rpcVersion': 1, 'authentication': auth}}))
        await ws.recv()
        await ws.send(json.dumps({'op': 6, 'd': {'requestType': 'SaveReplayBuffer', 'requestId': '1'}}))
        print('Replay saved!')

asyncio.run(save_replay())
