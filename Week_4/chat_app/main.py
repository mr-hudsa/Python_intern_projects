from fastapi import FastAPI, WebSocket, WebSocketDisconnect

app = FastAPI(title="Week 4 - Chat App with WebSocket")

# Store connected clients
clients = []

@app.websocket("/ws/{username}")
async def websocket_endpoint(websocket: WebSocket, username: str):
    # Accept connection
    await websocket.accept()
    clients.append((username, websocket))
    try:
        while True:
            # Receive message
            data = await websocket.receive_text()
            # Broadcast message to all clients
            for user, conn in clients:
                if conn != websocket:  # don't send back to self
                    await conn.send_text(f"{username}: {data}")
    except WebSocketDisconnect:
        clients.remove((username, websocket))
        for user, conn in clients:
            await conn.send_text(f"⚠️ {username} left the chat")
