from ALCS import IPv4Address, IPv6Address, Entity

ip1 = IPv4Address()
ip2 = IPv4Address()

# IPAddress are basically strings so you play around with them

object1 = Entity(ip1)
object2 = Entity(ip2)

object1.Transmit(object2, "Hello World!")
print(object2.Receive(object1))

# you can also stuff Entity inside list so you can put a bunch of Entity inside a list and you can access it by Bunch[index].Transmit or whatever you want to do with that
