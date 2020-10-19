#Using Python Pillow library for image processing
from PIL import Image, ImageDraw, ImageFont, ImageOps
 
# create map and resize to a standard size, thus ensuring proper map to symbol ratios
theMap = Image.open('Map.png')  #.resize((1000, 1000))
mapWidth = theMap.size[0]
mapHeight = theMap.size[1]

if mapWidth < mapHeight:
    symbolHeight = round(mapWidth * 0.05)
else:
    symbolHeight = round(mapHeight *0.05)

#Line 16/34 only needs to be run once - it resizes the symbol grid and ensures each symbol will be square
    #I manually went in and removed the background from the PNG file provided using GIMP - it was the easiest way I found
    #Math -> height = arbitrary (can be factor of map size)   width = height * # of symbols
    #Assumes the symbols are in one line and all occupy the same size pixel block

"""
numOfSymbols = 6
symbolHeight = 50   #in pixels
stripWidth = symbolHeight * numOfSymbols
symbols = Image.open('Modified_Symbols_Transparent.png').resize((stripWidth,symbolHeight)).convert('RGBA').save('Sized-Symbols.png')


#Saves each unique symbol to a variable 
    #theoretically could create a loop and save as an array (I think? Not sure with Python)
    #An array might not be useful, because you'd either have to add names within the array, or know the index of each symbol
symbols = 'Sized-Symbols.png'
triangle = Image.open(symbols).crop((symbolHeight*0, 0, symbolHeight*1, symbolHeight))
square = Image.open(symbols).crop((symbolHeight*1, 0, symbolHeight*2, symbolHeight))
circle = Image.open(symbols).crop((symbolHeight*2, 0, symbolHeight*3, symbolHeight))
uparc = Image.open(symbols).crop((symbolHeight*3, 0, symbolHeight*4, symbolHeight))
downarc = Image.open(symbols).crop((symbolHeight*4, 0, symbolHeight*5, symbolHeight))
star = Image.open(symbols).crop((symbolHeight*5, 0, symbolHeight*6, symbolHeight))
"""

numOfSymbolsWide = 5
#symbolHeight = 50   #in pixels
stripWidth = symbolHeight * numOfSymbolsWide
symbols = Image.open('Symbols.png').resize((stripWidth,symbolHeight)).convert('RGBA').save('Sized-Symbols.png')

symbols = 'Sized-Symbols.png'
triangle = Image.open(symbols).crop((symbolHeight*0,    0,              symbolHeight*1.1,   symbolHeight))
square = Image.open(symbols).crop((  symbolHeight*1.1,  0,              symbolHeight*2,     symbolHeight))
circle = Image.open(symbols).crop((  symbolHeight*2,    0,              symbolHeight*3,     symbolHeight))
uparc = Image.open(symbols).crop((   symbolHeight*3,    0,              symbolHeight*4,     symbolHeight/2))
downarc = Image.open(symbols).crop(( symbolHeight*3,    symbolHeight/2, symbolHeight*4,     symbolHeight))
star = Image.open(symbols).crop((    symbolHeight*4,    0,              symbolHeight*5,     symbolHeight))


#Allows symbols to be superimposed over the map
drawSymbol = ImageDraw.Draw(theMap)

#Color presets
red = 'rgb(255, 0, 0)'
green = 'rgb(0, 255, 0)'
blue = 'rgb(0, 0, 255)'

#Draw each symbol onto the map at given (x,y) coordinate - (0,0) is top left
drawSymbol.bitmap((270, 200), triangle, fill=blue)
drawSymbol.bitmap((900, 950), square, fill=green)
drawSymbol.bitmap((660, 690), circle, fill=red)
drawSymbol.bitmap((200, 1100), uparc, fill=green)
drawSymbol.bitmap((1500, 900), downarc, fill=red)

drawSymbol.bitmap((mapWidth*0.5, mapHeight*0.2), star, fill=red)
drawSymbol.bitmap((mapWidth*0.65, mapHeight*0.75), uparc.rotate(38), fill=blue)

drawSymbol.bitmap((2300, 200), square.rotate(150, expand='true'), fill=red)
drawSymbol.bitmap((2050, 800), star.resize((round(star.size[0]*2), round(star.size[1]*2))), fill=blue)



#Show the map (mostly for debugging)
theMap.show()

#Save the map
theMap.save('updatedMap.png')