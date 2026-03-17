from fastapi import WebSocket, WebSocketDisconnect
from .manager import manager

async def chat_endpoint(websocket: WebSocket, room: str):

    await manager.connect(room, websocket)

    try:
        while True:

            data = await websocket.receive_text()

            await manager.broadcast(room, data)

    except WebSocketDisconnect:
        manager.disconnect(room, websocket)