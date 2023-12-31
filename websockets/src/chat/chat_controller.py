from inspira.decorators.websocket import websocket
from inspira.websockets import WebSocket


@websocket("/chat")
class ChatController:

    async def on_open(self, websocket: WebSocket):
        print("Inside On Open")
        await websocket.on_open()

    async def on_message(self, websocket: WebSocket, message):
        print(f"Inside On Message. Received message: {message}")

        # Modify the message before echoing back
        modified_message = f"Server response to: {message.get('text', '')}"

        await websocket.send_text(modified_message)

    async def on_close(self, websocket: WebSocket):
        print("Inside On Close")
        await websocket.on_close()
