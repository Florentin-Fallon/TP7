import asyncio
import websockets

async def hello(websocket):
    name = await websocket.recv()
    print(f"<<< {name}")
    string = await websocket.recv()
    print(f"<<< {string}")
    greeting = f"Salut {name} ! Tu as dit : {string}"
    await websocket.send(greeting)
    print(f">>> {greeting}")


async def main():
    async with websockets.serve(hello, "localhost", 8765):
        await asyncio.Future()

if __name__ == "__main__":
    asyncio.run(main())
