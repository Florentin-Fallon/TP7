import asyncio
import websockets

async def handle_client(websocket, path):
    try:
        message = await websocket.recv()
        while True:
            print("Message reçu:", message)
            message = await websocket.recv()
    except websockets.exceptions.ConnectionClosedOK:
        pass
    except websockets.exceptions.ConnectionClosedError:
        pass
    finally:
        print("Connexion fermée")

async def main():
    server = await websockets.serve(
        handle_client, '127.0.0.1', 8888)

    try:
        async with server:
            await server.serve_forever()
    except asyncio.exceptions.CancelledError:
        pass

if __name__ == '__main__':
    asyncio.run(main())
