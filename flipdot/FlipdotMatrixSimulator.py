from Tkinter import *
import thread

class FlipdotMatrixSimulator(object):
    def __init__(self, 
                 udpHostAndPort = False, 
                 imageSize = (40,16)
                 ):
        self.imageSize=imageSize
        self.simulatorWidget = FlipdotMatrixSimulatorWidget()
    
    def show(self, imageArray):
        self.simulatorWidget.show(imageArray)

class FlipdotMatrixSimulatorWidget():
    BLACKCOLOR = 1
    WHITECOLOR = 0
    
    def __init__(self,
                 imageSize = (40,16)): 
        self.imageSize = imageSize
        self.master = Tk()
        self.canvas = Canvas(self.master, width=imageSize[0]*10, height=imageSize[1]*10)
        self.canvas.pack()
        self.initEmptyPixels()
        
    def initEmptyPixels(self):
        self.clearPixels
        for xValue in range(self.imageSize[0]):
            for yValue in range(self.imageSize[1]):
                self.addPixel(xValue, yValue, self.BLACKCOLOR)

    def show(self, imageArray):
        self.clearPixels()
        for xValue in range(self.imageSize[0]):
            for yValue in range(self.imageSize[1]):
                i = self.imageSize[0]*yValue + xValue
                color = imageArray[i]
                self.addPixel(xValue, yValue, color)
        self.canvas.update_idletasks()

    def clearPixels(self):
        self.canvas.delete(ALL)
        self.canvas.update_idletasks()
    
    def addPixel(self, xValue, yValue, color):
        xmin = xValue * 10
        xmax = xmin + 9
        ymin = yValue * 10
        ymax = ymin + 9
        if color == self.BLACKCOLOR:
                rectcolor = "black"
        else:
                rectcolor = "white"
        self.canvas.create_rectangle(xmin, ymin, xmax, ymax, fill=rectcolor)

if (__name__=="__main__"):
    sim = FlipdotMatrixSimulator()
    
                