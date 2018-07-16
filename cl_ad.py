def client_addapter_func(client, json_data):
    while True:
        message = client.recv(1024).decode()
        if message == '1':
            data = json_data.get()
            client.send(data.decode())
        if message == 'e':
            json_data.exit=True
        # TODO: try except construction then client end connection
    client.close()
