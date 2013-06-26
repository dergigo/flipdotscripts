import socket
import tools 

class FlipdotMatrix():

    def __init__(
                 self, 
                 udpHostAndPort = ("2001:7f0:3003:cafe:222:f9ff:fe01:c65",2323), 
                 imageSize=(40, 16)
                 ):
        self.__sock = socket.socket(socket.AF_INET6, socket.SOCK_DGRAM)
        self.udpHostAndPort=udpHostAndPort
        self.imageSize=imageSize
    
    def showTestPattern(self):
        testPattern = tools.generateTestPatternImageArray()
        self.show(testPattern)
    
    def resetAll(self):
        self.show(tools.generateAllOnImageArray(self.imageSize))
        self.show(tools.generateAllOffImageArray(self.imageSize))
        
    
    def show(self, imageArray):
        udpPacket = self.__arrayToPacket(imageArray) 
        self.__sendUdpPackage(udpPacket)
    
    def __arrayToPacket(self, imageArray):
        return str(bytearray([tools.list2byte(imageArray[i*8:i*8+8]) for i in range(len(imageArray)/8)]))
    
    def __sendUdpPackage(self, udpPacket):
        self.__sock.sendto(udpPacket, self.udpHostAndPort)

#main
if (__name__=="__main__"):
    FlipdotMatrix().resetAll()
