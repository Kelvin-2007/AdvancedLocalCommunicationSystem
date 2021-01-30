import ipaddress;from random import randint

globalNetworkData = {}

def _setup(address):
    global globalNetworkData
    if globalNetworkData:
        globalNetworkData[address] = {}
        others = []
        for _ in globalNetworkData:
            if _ != address:
                others.append(_)
        for other in others:
            globalNetworkData[other][address] = None
            globalNetworkData[address][other] = None
    else:
        globalNetworkData[address] = {}

class Entity:
    def __init__(self, address):
        if type(address) == IPv4Address and type(address) == IPv6Address:
            raise TypeError("Invalid: address")
        self.address = address.address
        self.addressType = type(address)
        global _setup
        _setup(self.address)

    def Transmit(self, Receiver, Data):
        if type(Receiver) == Entity:
            globalNetworkData[Receiver.address][self.address] = Data
        else:
            raise TypeError("Invalid: Receiver")

    def Receive(self, Sender):
        if type(Sender) == Entity:
            return globalNetworkData[self.address][Sender.address]
        else:
            raise TypeError("Invalid: Sender")

class IPv4Address:
    def __init__(self):
        self.address = ipaddress.IPv4Address._string_from_ip_int(randint(0, 2 ** 32 - 1))

    def __repr__(self):
        return f"IPv4Address({self.address})"

class IPv6Address:
    def __init__(self):
        self.address = ipaddress.IPv6Address._string_from_ip_int(randint(0, 2 ** 128 - 1))

    def __repr__(self):
        return f"IPv6Address({self.address})"

def printGlobalData():
    for object1 in globalNetworkData:
        print(object1+":")
        for object2 in globalNetworkData[object1]:
            print(" "*4+object2+":")
            print(" "*7, globalNetworkData[object1][object2])