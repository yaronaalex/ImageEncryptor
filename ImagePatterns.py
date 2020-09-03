import random
from PIL import Image

def patternBottom(originalImageLocation, encryptionSize, copyLocation):
    originalImage = Image.open(originalImageLocation)
    height = originalImage.height
    width = originalImage.width
    random.seed()

    #decine how many rows to add to bottom of the image
    newline = 1
    widthcount = 0
    
    while widthcount < encryptionSize:
        newline = newline + 1
        widthcount = widthcount + width

    #create image to hold encryption
    encryptedImage = Image.new('RGB', (width, height + newline))
    encryptedImage.paste(originalImage)

    #apply encryption to new rows
    xloc = 0
    yloc = height

    for i in range (0, encryptionSize):
        encryptedImage.putpixel((xloc, yloc), (random.randrange(0, 255, 1), random.randrange(0, 255, 1), random.randrange(0, 255, 1)))
        xloc = xloc + 1
        if xloc == originalImage.width:
            xloc = 0
            yloc = yloc + 1    

    #save the image
    encryptedImage.save(copyLocation)

def patternEvenDistribution(originalImageLocation, copyLocation, encryptionArray):
    originalImage = Image.open(originalImageLocation)
    
    #decide spacing size to spread encrypted pixels
    width = originalImage.width
    height = originalImage.height
    encryptionSize = len(encryptionArray[0])
    stepsize = int((width * height) / encryptionSize)
    
    #Store the image to encrypt
    encryptedImage = originalImage
    
    #apply encryption
    xloc = 0
    yloc = 0 
    location = 0
    for i in range(0, encryptionSize):
        location = i * stepsize

        xloc = location % width
        yloc = int(location / width)
        
        encryptedImage.putpixel((xloc, yloc), (encryptionArray[0][i], encryptionArray[1][i], encryptionArray[2][i]))
        
    #save the image
    xloc = encryptedImage.width - 1
    yloc = encryptedImage.height - 1
    encryptedImage.putpixel((xloc, yloc), (0, encryptionSize, 0))
    encryptedImage.save(copyLocation)

def returnEvenDistribution(encryptedImageLocation):
    encryptedImage = Image.open(encryptedImageLocation)
    width = encryptedImage.width
    height = encryptedImage.height

    xloc = width - 1
    yloc = height -1

    encryptedPixel = encryptedImage.getpixel((xloc, yloc))
    encryptionSize = encryptedPixel[1]
    stepsize = int((width * height) / encryptionSize)
    
    encryptedString = []

    xloc = 0
    yloc = 0 
    location = 0
    for i in range(0, encryptionSize):
        location = i * stepsize

        xloc = location % width
        yloc = int(location / width)
        
        temp = encryptedImage.getpixel((xloc, yloc))
        encryptedString.append(temp[0])
        encryptedString.append(temp[1])
        encryptedString.append(temp[2])

    return encryptedString
        
def patternClockStriping(originalImageLocation, encryptionSize, copyLocation):
    random.seed()

    originalImage = Image.open(originalImageLocation)
    width = originalImage.width
    height = originalImage.height
    statemachine = 1

    #prep the four clock hands to hold encryption
    Clock3X = int(width - 1)
    Clock3Y = int(0)

    Clock6X = int(width -1)
    Clock6Y = int(height - 1)

    Clock9X = int(0)
    Clock9Y = int(height - 1)

    Clock12X = int(0)
    Clock12Y = int(0)
    
    #prep the delta steps 
    deltaX = width/encryptionSize
    deltaY = height/encryptionSize

    #prep the encrypted image
    encryptedImage = originalImage

    #calculate clock pattern pixel placement
    for i in range (0, encryptionSize):
    
        if statemachine == 1:
            xloc =  Clock3X
            yloc =  Clock3Y 
            Clock3X = Clock3X - 1 # int(Clock3X - deltaX)
            Clock3Y = int(Clock3Y + deltaY)

        if statemachine == 2:
            xloc =  Clock6X
            yloc =  Clock6Y
            Clock6X = int(Clock6X - deltaX)
            Clock6Y = Clock6Y - 1 #int(Clock6Y - deltaY)

        if statemachine == 3:
            xloc =  Clock9X
            yloc =  Clock9Y
            Clock9X = Clock9X + 1 #int(Clock9X + deltaX)
            Clock9Y = int(Clock9Y - deltaY)
        
        if statemachine == 4:
            xloc =  Clock12X
            yloc =  Clock12Y
            Clock12X = int(Clock12X + deltaX)
            Clock12Y = Clock12Y + 1 #int(Clock12Y + deltaY)

        #change state machine
        statemachine = statemachine  + 1
        if statemachine is 5:
            statemachine = 1

        #place pixel
        encryptedImage.putpixel((xloc, yloc), (random.randrange(0, 255, 1), random.randrange(0, 255, 1), random.randrange(0, 255, 1)))

    #save the image
    encryptedImage.save(copyLocation)
    