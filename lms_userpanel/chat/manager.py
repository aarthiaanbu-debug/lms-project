from fastapi import WebSocket

class ConnectionManager:

    def __init__(self):
        self.active_connections = {}

    async def connect(self, room: str, websocket: WebSocket):
        await websocket.accept()

        if room not in self.active_connections:
            self.active_connections[room] = []

        self.active_connections[room].append(websocket)

    def disconnect(self, room: str, websocket: WebSocket):
        self.active_connections[room].remove(websocket)

    async def broadcast(self, room: str, message: str):

        for connection in self.active_connections.get(room, []):
            await connection.send_text(message)


manager = ConnectionManager()