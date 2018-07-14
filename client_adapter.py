import socket
import json
import time

socket3dScene = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
addres3dScene = ('localhost',9091)
socket3dScene.connect(addres3dScene)

socketPlanner = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
addresPlanner = ('localhost',9000)
socketPlanner.connect(addresPlanner)


def dataConvertJsonToStrByte(dataJson):
    dictName = {'fanuc': 'f', 'telega':'t'}
    dataStr = str(8)+str(dictName.get(dataJson.get('name')))+':'+dataJson.get('command')
    dataStrByte = dataStr.encode()
    return dataStrByte


def sendPlanner(dataJson):
    dataByteSend = dataConvertJsonToStrByte(dataJson)
    socketPlanner.send(dataByteSend)


def send3dScene(dataJson):
    dataSend = str(dataJson.get('flag'))
    dataByteSend = dataSend.encode()
    socket3dScene.send(dataByteSend)
    dataInto3dScene = socket3dScene.recv(2048)
    print('hui')
    return dataInto3dScene



socketUnity = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
socketUnity.bind(('localhost', 9090))
socketUnity.listen(100)
clientSocketUnity, addrUnity = socketUnity.accept()
while True:
    print(addrUnity)
    dataByte = clientSocketUnity.recv(1024)
    print(dataByte)
    dataJson = json.loads(dataByte.decode("utf-8"))
    print(type(dataJson))
    if dataJson.get('flag')==0:
        sendPlanner(dataJson)
    elif dataJson.get('flag') == 1:
        dataSendByte = send3dScene(dataJson)
        clientSocketUnity.send(dataSendByte)
    elif dataJson.get('flag') == 'e':
        socket3dScene.send(dataByte)
        socketPlanner.send(dataByte)
        time.sleep(3)
        break


clientSocketUnity.close()
socket3dScene.close()
