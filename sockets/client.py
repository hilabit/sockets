import socket
import generated.log_message_pb2 as log_message

HOST = "127.0.0.1"
PORT = 15000

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((HOST, PORT))

    lm = log_message.LogMessage()
    lm.log_level = 'ERROR'
    lm.logger = 'main'
    lm.mac = bytes([0xaa, 0xbb, 0xcc, 0xdd, 0xee, 0xff])
    lm.message = 'test message'
    payload = lm.SerializeToString()

    s.sendall(payload)


print(lm)


