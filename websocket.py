import asyncio
import websockets
import mariadb
import json

async def handle_message(websocket, message):
    
    json_data=json.loads(message) 
    db_connection = mariadb.connect(
    user="myuser",
    password="mypassword",
    host="192.168.2.208",
    database="mydb"
    )
#,SENSORNR,SENSORLOCATION,DATETIME (24,19,1,'Keller',NOW())
    cursor = db_connection.cursor()
    insert_data = """
    INSERT INTO DHT11(TEMPERATURE,HUMIDITY,SENSORNR,SENSORLOCATION,DATETIME)
    VALUES
        (%s,%s,%s,%s,NOW())
        
    """
    data = (json_data['temp'],json_data['hum'],json_data['sensornr'],json_data['sensorlocation'])
    
    cursor.execute(insert_data,data)
    db_connection.commit()
    cursor.close()    
    
    # Hier kannst du anpassen, wie der Server auf Nachrichten reagieren soll
    print(f"Received message: {message}")

    # Sende eine Antwort an den Client
    response = f"Received: {message}"
    await websocket.send(response)
    print(f"Sent response: {response}")
    

async def server(websocket, path):
    async for message in websocket:
        await handle_message(websocket, message)

if __name__ == "__main__":
    
    start_server = websockets.serve(server, '192.168.2.208', 8657)

    asyncio.get_event_loop().run_until_complete(start_server)
    print("WebSocket server started.")

    try:
        asyncio.get_event_loop().run_forever()
    except KeyboardInterrupt:
        
        print("WebSocket server stopped.")
