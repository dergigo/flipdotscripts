import font
from font import font8px

class FlipdotImage(object):
    BLACKPIXEL = 0
    WHITEPIXEL = 1

    def __init__(self, pixel2DArray):
        self.width = len(pixel2DArray[0])
        self.height = len(pixel2DArray)
        self.rowArrayOfLineArraysOfPixels =  pixel2DArray

    def blitImageAtPosition(self, flipdotImage, xPos=0, yPos=0):
        for lineNr in range(self.height):
            newImageLineNr = lineNr-yPos
            if newImageLineNr >= 0 and flipdotImage.height > newImageLineNr:
                self.__blitLineAtPosition(flipdotImage, lineNr, newImageLineNr, xPos, yPos)
    
    def __blitLineAtPosition(self, flipdotImage, lineNr, newImageLineNr, xPos, yPos):
        for rowNr in range(self.width):
            newImageRowNr = rowNr - xPos
            if newImageRowNr >= 0 and flipdotImage.width > newImageRowNr:
                self.rowArrayOfLineArraysOfPixels[lineNr][rowNr] = flipdotImage.rowArrayOfLineArraysOfPixels[newImageLineNr][newImageRowNr]

    def blitTextAtPosition(self, text, autoLineBreak = False, xPos = 0, yPos = 0, __indentXPos=None):
        if __indentXPos==None:
            __indentXPos = xPos

        if len(text) <= 0:
            return
        
        letterImage = self.__getLetterImageForNextLetter(text)
        
        if autoLineBreak and self.__isLineBreakRequired(letterImage, xPos):
            xPos = __indentXPos
            yPos = yPos + font.font8px["lineheight"]
            
        self.blitImageAtPosition(letterImage, xPos, yPos)
        
        nextLetterXPos = xPos + letterImage.width + font.font8px["whitespace"]
        self.blitTextAtPosition(text[1:], autoLineBreak, nextLetterXPos, yPos, __indentXPos)
        
                
    def __isLineBreakRequired(self, letterImage, xPos):
        return letterImage.width > self.width-xPos

    def __getLetterImageForNextLetter(self, text):
        nextLetter = text[:1].upper()
        if not nextLetter in font.font8px:
            nextLetter="?"
        return FlipdotImage(font8px[nextLetter])

    def serializeImageArray(self):
        imageArray = []
        for y in range(self.height):
            for x in range(self.width):
                imageArray.append(self.rowArrayOfLineArraysOfPixels[y][x])
        return imageArray


    def getLine(self, line):
        return self.rowArrayOfLineArraysOfPixels[line]
        
    @classmethod
    def newBlackFlipdotImage(cls, width, height):
        pixel2DArray = cls.generateColoredRowArrayOfLineArraysOfPixels(width, height, FlipdotImage.BLACKPIXEL) 
        return cls(pixel2DArray)

    @classmethod
    def newWhiteFlipdotImage(cls, width, height):
        pixel2DArray = cls.generateColoredRowArrayOfLineArraysOfPixels(width, height, FlipdotImage.WHITEPIXEL) 
        return cls(pixel2DArray)
    
    @classmethod
    def generateColoredRowArrayOfLineArraysOfPixels(cls, width, height, color):        
        rowArrayOfLineArrayOfPixels = []
        for y in range(height):
            rowArrayOfLineArrayOfPixels.append(FlipdotImage.generateColoredLineArrayOfPixels(width, color))
        return rowArrayOfLineArrayOfPixels

    @classmethod
    def generateColoredLineArrayOfPixels(cls, width, color):
        lineArrayOfPixels = []
        for x in range(width):
            lineArrayOfPixels.append(color)
        return lineArrayOfPixels
                
                     
        