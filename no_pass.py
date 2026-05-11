#!/usr/bin/env python3
import asyncio, websockets, json

async def save_replay():
    async with websockets.connect('ws://localhost:4455') as ws:
        await ws.recv()  # hello
        await ws.send(json.dumps({'op': 1, 'd': {'rpcVersion': 1}}))
        await ws.recv()  # identified
        await ws.send(json.dumps({'op': 6, 'd': {'requestType': 'SaveReplayBuffer', 'requestId': '1'}}))
        print('Replay saved!')

asyncio.run(save_replay())
