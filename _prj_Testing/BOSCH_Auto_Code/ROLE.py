import socket

class CRole():
    def __init__(self):
        self.host = '192.168.1.253'      # Get local machine name
        self.port = 1030                 # Reserve a port for your service.

    def displayhex(self, bytes):
        ls = []
        for x in bytes:
            ls.append(hex(x))
        return ls

    def trigger(self, channel, state):
        s = socket.socket()         # Create a socket object
        data = bytes.fromhex('483A0170'+ channel + state + '00004544')
        s.connect((self.host, self.port))
        print('Send:' + str(self.displayhex(data)))
        s.send(data)
        data2 = s.recv(1024)
        print('Receive:' + str(self.displayhex(data2)))
        s.close()

    def OpenState(self):
        self.trigger('01', '00')

    def GNDState(self):
        self.trigger('01', '01')
        self.trigger('02', '00')

    def VCCState(self):
        self.trigger('01', '01')
        self.trigger('02', '01')

    def BusOFF_Pub_EN(self):
        self.trigger('05', '01')

    def BusOFF_Pub_DIS(self):
        self.trigger('05', '00')

    def BusOFF_Pri_EN(self):
        self.trigger('06', '01')

    def BusOFF_Pri_DIS(self):
        self.trigger('06', '00')

Role = CRole()

if __name__ == "__main__":
    Role.BusOFF_Pub_DIS()
    Role.BusOFF_Pri_DIS()