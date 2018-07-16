def rca_func(client, json_data):
    while True:
        data = client.recv(1024).encode()
        json_data.set(data)
        if json_data.exit:
            exit()
        #TODO: try except construction then client end connection
    client.close()