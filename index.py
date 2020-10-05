#Using Python Pillow library for image processing
from PIL import Image, ImageDraw, ImageFont, ImageOps
 
# create map and resize to a standard size, thus ensuring proper map to symbol ratios
theMap = Image.open('Map.png').resize((1000, 1000))

#Line 14 only needs to be run once - it resizes the symbol grid and ensures each symbol will be square
    #I manually went in and removed the background from the PNG file provided using GIMP - it was the easiest way I found
    #Math -> height = arbitrary (can be factor of map size)   width = height * # of symbols
    #Assumes the symbols are in one line and all occupy the same size pixel block
numOfSymbols = 5
symbolHeight = 50   #in pixels
stripWidth = symbolHeight * numOfSymbols
symbols=Image.open('Symbols.png').resize((stripWidth,symbolHeight)).convert('RGBA').save('Sized-Symbols.png')

#Saves each unique symbol to a variable 
    #theoretically could create a loop and save as an array (I think? Not sure with Python)
    #An array might not be useful, because you'd either have to add names within the array, or memorize the indices of each symbol
symbols = 'Sized-Symbols.png'
triangle = Image.open(symbols).crop((symbolHeight*0, 0, symbolHeight*1, symbolHeight))
square = Image.open(symbols).crop((symbolHeight*1, 0, symbolHeight*2, symbolHeight))
circle = Image.open(symbols).crop((symbolHeight*2, 0, symbolHeight*3, symbolHeight))
arc = Image.open(symbols).crop((symbolHeight*3, 0, symbolHeight*4, symbolHeight))
star = Image.open(symbols).crop((symbolHeight*4, 0, symbolHeight*5, symbolHeight))

#Allows symbols to be superimposed over the graph
drawSymbol = ImageDraw.Draw(theMap)

#Not sure why, but the transparency mask I'm using turns the symbols to white, so have to reset to red
red = 'rgb(255, 0, 0)'

#Draw each symbol onto the map at given (x,y) coordinate - (0,0) is top left
drawSymbol.bitmap((200, 200), triangle, fill=red)
drawSymbol.bitmap((600, 250), square, fill=red)
drawSymbol.bitmap((660, 690), circle, fill=red)
drawSymbol.bitmap((200, 700), arc, fill=red)
drawSymbol.bitmap((900, 900), star, fill=red)
 
#Show the map (mostly for debugging)
theMap.show()

#Save the map
theMap.save('updatedMap.png')