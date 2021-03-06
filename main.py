import asyncio
import websockets

async def echo(websocket, path):
    async for message in websocket:
        print(message)
        await websocket.send('what')

async def main():
    async with websockets.serve(echo, "localhost", 8765):
        await asyncio.Future()

asyncio.run(main())