import asyncio
import signal
import functools
import websockets

async def send_message(websocket, message):
    await websocket.send(message)

async def user_input_loop(websocket, pseudo):
    try:
        while True:
            message = input("Entre ton message : ")
            if message.lower() == "exit":
                break

            formatted_message = f"{pseudo}|{message}"
            await send_message(websocket, formatted_message)
    except asyncio.CancelledError:
        pass

async def receive_messages(websocket):
    try:
        while True:
            message = await websocket.recv()
            print(message)
    except asyncio.CancelledError:
        pass

async def main():
    pseudo = input("Choisi ton pseudo: ")

    async with websockets.connect('ws://127.0.0.1:8888') as websocket:
        await send_message(websocket, f"Hello | {pseudo} ")

        user_input_task = asyncio.create_task(user_input_loop(websocket, pseudo))
        receive_messages_task = asyncio.create_task(receive_messages(websocket))

        loop = asyncio.get_running_loop()
        loop.add_signal_handler(signal.SIGINT, loop.stop)

        await asyncio.gather(user_input_task, receive_messages_task)

        websocket.close()
        await websocket.wait_closed()

async def handle_client_shutdown(user_input_task, receive_messages_task, *args):
    print("Déconnexion du serveur. Programme terminé.")
    
    user_input_task.cancel()
    receive_messages_task.cancel()

if __name__ == '__main__':
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        pass
