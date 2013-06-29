import socket
import tools 
import font
from string import uppercase

class FlipdotMatrix():

    def __init__(
                 self, 
                 udpHostAndPort = ("2001:7f0:3003:cafe:222:f9ff:fe01:c65",2323), 
                 imageSize=(40, 16)
                 ):
        self.__sock = socket.socket(socket.AF_INET6, socket.SOCK_DGRAM)
        self.udpHostAndPort=udpHostAndPort
        self.imageSize=imageSize
        self.oldImageArray2d = self.generateEmptyImageArray2d()
        
    def generateEmptyImageArray2d(self):
        imageArray2d = []
        for y in range(self.imageSize[1]):
            imageArray = []
            for x in range(self.imageSize[0]):
                imageArray.append(0)
            imageArray2d.append(imageArray)
        return imageArray2d
                
    
    def showTestPattern(self):
        testPattern = tools.generateTestPatternImageArray()
        self.show(testPattern)
    
    def resetAll(self):
        self.show(tools.generateAllOnImageArray(self.imageSize))
        self.show(tools.generateAllOffImageArray(self.imageSize))
        
    
    def show(self, imageArray):
        udpPacket = self.__arrayToPacket(imageArray) 
        self.__sendUdpPackage(udpPacket)

    def addImageArray2dToImageArray(self, oldImageArray2d, imageArray2dToAdd, position=(0,0)):
        size = (len(imageArray2dToAdd[0]), len(imageArray2dToAdd))
        newImageArray2d = oldImageArray2d
        for y in range(self.imageSize[1]):
            for x in range(self.imageSize[0]):
                if not(x-position[0]<0 or y-position[1]<0 or x-position[0]>=size[0] or y-position[1]>=size[1]):
                    coord = (x-position[0], y-position[1])
                    newImageArray2d[y][x] = imageArray2dToAdd[coord[1]][coord[0]]
        return newImageArray2d

    def showBlit (self, imageArray2d, position = (0,0)):
        imageArray=[]
        size = (len(imageArray2d[0]), len(imageArray2d))
        
        for y in range(self.imageSize[1]):
            for x in range(self.imageSize[0]):
                if (x-position[0]<0 or y-position[1]<0):
                    imageArray.append(self.oldImageArray2d[y][x])
                elif (x-position[0]>=size[0] or y-position[1]>=size[1]):
                    imageArray.append(self.oldImageArray2d[y][x])
                else:
                    coord = (x-position[0], y-position[1])
                    imageArray.append(imageArray2d[coord[1]][coord[0]])
        
        return self.show(imageArray)
    
    def showText(self, text, position):
        imageArray2d = self.oldImageArray2d
        imageArray2d = self.addTextToImageArray2d(imageArray2d, text, (0,0))
        self.showBlit(imageArray2d)
        
    def addTextToImageArray2d(self, imageArray2d, text, position):
        if (len(text)<=0):
            return imageArray2d
        else:
            nextLetter = text[:1].upper()
            if not nextLetter in font.font8px:
                nextLetter="?"
            
            if position[0]+len(font.font8px[nextLetter][0])>self.imageSize[0]:
                position=(0,position[1]+8)
            
            imageArray2d = self.addImageArray2dToImageArray(imageArray2d, font.font8px[nextLetter], position)
            newposition = (position[0]+len(font.font8px[nextLetter][0]), position[1])
            
            imageArray2d = self.addTextToImageArray2d(imageArray2d, text[1:], newposition)
            return imageArray2d
    
    def __arrayToPacket(self, imageArray):
        return str(bytearray([tools.list2byte(imageArray[i*8:i*8+8]) for i in range(len(imageArray)/8)]))
    
    def __sendUdpPackage(self, udpPacket):
        self.__sock.sendto(udpPacket, self.udpHostAndPort)

#main
if (__name__=="__main__"):
    #matrix = FlipdotMatrix(("::1",2323))
    matrix = FlipdotMatrix()
    #matrix.resetAll()
    matrix.showText("fnord", (0,0))
    
    
    
