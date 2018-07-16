import socket
from cl_ad import client_addapter_func
from planner import planner_func
from RCA import rca_func
import threading
sock_main = socket.socket()
sock_main.bind(('',9095))
sock_main.listen(3)

while True:
    client, adress = sock_main.accept()
    who_is_it = client.recv(1024).encode()
    if who_is_it == 'planner':
        planer_thread = threading.Thread(target=planner_func, args=(client, json_data))
        planer_thread.start()
    elif who_is_it == 'RCA':
        rca_thread = threading.Thread(target=rca_func, args=(client, json_data))
        rca_thread.start()
    elif who_is_it == 'ClAd':
        client_addapter_thread = threading.Thread(target=client_addapter_func, args=(client, json_data))
        client_addapter_thread.start()
    else:
        continue