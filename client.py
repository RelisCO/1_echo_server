import socket

# Функции получения и отправки сообщения
def sending(sock, msg):
    sock.send(("{0:0>10}".format(len(msg)) + msg).encode())    

def receiving(sock):
    try: # Если клиент отключился получим пустое сообщение
        length = int(sock.recv(10).decode()) # Поэтому ловим ошибку перевода пустого сообщения в int
    except: # Для клиента это бесполезно, но функция скопированна из сервера и зачем её менять
        return None # И так работает
    msg = sock.recv(length).decode()
    return msg


sock = socket.socket() # Создаём соке

host = input("Введите имя хоста: ")
if host == "": host = "localhost"
while True:
    port = input("Введите номер порта: ")
    if port == "": 
        port = 9090
        break
    else:
        try:
            port = int(port)
        except:
            print("Номер порта - целое число")

sock.connect((host, port)) # Подключаемся к серверу
print("Соединение с сервером")


print("Для выхода введите exit")
while True:
    msg = input() # Считываем сообщение
    if msg == 'exit': # Если сообщение exit - выходим из цикла
        break
    sending(sock, msg) # Отправляем сообщение на сервер
    print("Отправка данных серверу")
    data = receiving(sock) # Получаем данные с сервера
    print("Получение данных от сервера")
    print(data) # Выводим полученные данные

sock.close() # Закрываем сокет