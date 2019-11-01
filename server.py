import socket
import errno

# Функции получения и отправки сообщения
def sending(sock, msg):
    sock.send(("{0:0>10}".format(len(msg)) + msg).encode())
    
def receiving(sock):
    try: # Если клиент отключился получим пустое сообщение
        length = int(sock.recv(10).decode()) # Поэтому ловим ошибку перевода пустого сообщения в int
    except:
        return None
    msg = sock.recv(length).decode()
    return msg


sock = socket.socket() # Создаём сокет
port = 9090 # Стартовое значение порта
while True:
    try:
        sock.bind(('', port)) # Задаём хост и порт
    except socket.error as e:
        if e.errno == errno.EADDRINUSE:
            port += 1 # Если порт занят увеличиваем его на единицу
    else:
        break
print(f"Слушаю порт {port}")    

    
with open('log.txt', 'a') as file:
    file.write("Запуск сервера\n")
sock.listen(1) # Начинаем прослушивание
with open('log.txt', 'a') as file:
    file.write("Начало прослушивания\n")

while True:
    try:
        conn, addr = sock.accept() # Принимаем подключение
        with open('log.txt', 'a') as file:
            file.write("Подключение клиента\n")
        while True:
            data = receiving(conn) # Получаем сообщение от клиента
            with open('log.txt', 'a') as file:
                file.write("Получение данных от клинета\n")
            if not data:
                break # Если сообщения нет - клинет отключился, значит выходим из цикла
            sending(conn, data) # Отправляем клиенту его сообщение обратно
            with open('log.txt', 'a') as file:
                file.write("Отправка данных клиенту\n")
            
        conn.close() # Закрываем соединение
        with open('log.txt', 'a') as file:
            file.write("Отключение клиента\n")
    except KeyboardInterrupt:
        break
sock.close() # Закрываем сокет
with open('log.txt', 'a') as file:
    file.write("Закрытие сервера\n")
    