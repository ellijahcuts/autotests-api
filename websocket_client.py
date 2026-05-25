import asyncio
import websockets


async def client():
    uri = 'ws://localhost:8765'
    async with websockets.connect(uri) as websocket:
        message = 'Здарова, сервачек!'
        print(f'Отправка: {message}')
        await websocket.send(message)

        for i in range(10):
            response = await websocket.recv()
            print(f'Ответ от сервера: {response}')

asyncio.run(client())