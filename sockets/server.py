from twisted.internet import protocol, reactor, endpoints

HOST = "127.0.0.1"
PORT = 15000


class Echo(protocol.Protocol):
    def dataReceived(self, data):
        self.transport.write(data)


class EchoFactory(protocol.Factory):
    def buildProtocol(self, addr):
        return Echo()


endpoints.serverFromString(reactor, f'tcp:{PORT}').listen(EchoFactory())
reactor.run()

