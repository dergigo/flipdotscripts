import socket
import tools 
import font
from FlipdotImage import FlipdotImage


class FlipdotMatrix():
    def __init__(self, 
                 udpHostAndPort = ("2001:7f0:3003:cafe:222:f9ff:fe01:c65",2323), 
                 imageSize=(40, 16)
                 ):
        self.__sock = socket.socket(socket.AF_INET6, socket.SOCK_DGRAM)
        self.udpHostAndPort=udpHostAndPort
        self.flipdotImage = FlipdotImage.newBlackFlipdotImage(imageSize[0], imageSize[1])
    
    def resetAll(self):
        width = self.flipdotImage.width
        height = self.flipdotImage.height
        blackImage = FlipdotImage.newBlackFlipdotImage(width, height)
        whiteImage = FlipdotImage.newWhiteFlipdotImage(width, height)
        self.show(blackImage)
        self.show(whiteImage)
    
    def __showSerializedArrayOfPixels(self, imageArray):
        udpPacket = FlipdotMatrix.__arrayToPacket(imageArray) 
        self.__sendUdpPackage(udpPacket)

    def show(self, image):
        self.__clearFlipdotImageWithoutUpdate()
        self.flipdotImage.blitImageAtPosition(image)
        self.__updateFlipdotMatrix()

    def showBlit (self, image, xPos=0, yPos=0):
        self.flipdotImage.blitImageAtPosition(image, xPos, yPos)
        self.__updateFlipdotMatrix()

    def __updateFlipdotMatrix(self):
        serializedImageArray = self.flipdotImage.serializeImageArray()
        self.__showSerializedArrayOfPixels(serializedImageArray)
    
    def clear(self):
        self.__clearFlipdotImageWithoutUpdate()
        self.__updateFlipdotMatrix()
    
    def __clearFlipdotImageWithoutUpdate(self):
        width = self.flipdotImage.width
        height = self.flipdotImage.height
        self.flipdotImage = FlipdotImage.newBlackFlipdotImage(width, height)

    def showText(self, text, linebreak = False, xPos=0, yPos = 0):
        self.__clearFlipdotImageWithoutUpdate()
        self.flipdotImage.blitTextAtPosition(text, linebreak, xPos, yPos)
        self.__updateFlipdotMatrix()

    def showBlitText(self, text, linebreak=False, xPos=0, yPos=0):
        self.flipdotImage.blitTextAtPosition(text, linebreak, xPos, yPos)
        self.__updateFlipdotMatrix()

    @classmethod
    def __arrayToPacket(cls, imageArray):
        return str(bytearray([tools.list2byte(imageArray[i*8:i*8+8]) for i in range(len(imageArray)/8)]))
    
    def __sendUdpPackage(self, udpPacket):
        self.__sock.sendto(udpPacket, self.udpHostAndPort)

#main
if (__name__=="__main__"):
    matrix = FlipdotMatrix()
    matrix.resetAll()
    
    
    
