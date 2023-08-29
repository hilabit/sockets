from twisted.internet import protocol, reactor, endpoints
import generated.log_message_pb2 as log_message

HOST = "127.0.0.1"
PORT = 15000


class Echo(protocol.Protocol):
    def dataReceived(self, data):
        log_msg = log_message.LogMessage()
        log_msg.ParseFromString(data)
        print(log_msg)


class EchoFactory(protocol.Factory):
    def buildProtocol(self, addr):
        return Echo()


endpoints.serverFromString(reactor, f'tcp:{PORT}').listen(EchoFactory())
reactor.run()

