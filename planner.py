def planner_func(client, json_data):
    while True:
        data = json_data.get()
        message = client.recv(1024).encode()
        if message == "get_scene":
            client.send(data.encode())
        if json_data.exit:
            exit()
        # TODO: try except construction then client end connection

    client.close()