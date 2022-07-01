completed = False
customizing = False
textamount = 0
temp = {}
everytext = {}
code = ""

def gradient(h1, h2, num):
    txt = everytext[num-1]
    t = temp[num-1].replace(txt+"</font></stroke>","")
    rgb1 = hex_to_rgb(h1)
    rgb2 = hex_to_rgb(h2)
    currentrgb = rgb1
    ratio = ((rgb2[0]-rgb1[0])/len(txt),(rgb2[1]-rgb1[1])/len(txt),(rgb2[2]-rgb1[2])/len(txt))
    result = ""
    for i in range(0,len(txt)):
        color = '#%02x%02x%02x' % (int(currentrgb[0]),int(currentrgb[1]),int(currentrgb[2]))
        currentrgb = (currentrgb[0]+ratio[0],currentrgb[1]+ratio[1],currentrgb[2]+ratio[2])
        if txt != " ":
            result += '<font color="'+color.upper()+'">'+txt[i]+"</font>"
        else:
            results += " "
    temp[num-1] = t+result+"</font></stroke>"

def hex_to_rgb(value):
    value = value.lstrip('#')
    lv = len(value)
    return tuple(int(value[i:i+lv//3], 16) for i in range(0, lv, lv//3))

while completed == False:
    print("Type in '>complete' to get your code or '>gradient' to replace text with a gradient")
    print("Found text: "+str(len(everytext)))
    text = input("Insert text > ")
    customizing = True
    if text.lower() == ">complete" or text.lower() == ">gradient":
        if text.lower() == ">gradient":
            hex1 = input("Insert color hex number 1 > ").upper()
            hex2 = input("Insert color hex number 2 > ").upper()
            chosentext = input("Insert a text id > ")
            if int(chosentext) and int(chosentext) <= len(everytext):
                gradient(hex1,hex2,int(chosentext))
            else:
                print("error has occurred")
        else:
            for i in range(0,len(temp)):
                code += temp[i]
            completed = True
    else:
        everytext[len(everytext)] = text
        sc = "#000000"
        st = "1" 
        fc = "#FFFFFF" 
        ff = "Gotham"
        while customizing == True:
            print("Type in 'finish' to stop customizing your text")
            print("Supported types: StrokeColor, StrokeThickness, FontColor, FontFace")
            typ = input("Insert type > ")
            if typ.lower() == "finish":
                temp[len(temp)] = '<stroke color="'+sc+'" thickness="'+st+'"><font color="'+fc+'" face="'+ff+'">'+text+"</font></stroke>"
                customizing = False
            if typ.lower() == "strokecolor":
                chex = input("Insert color hex > ")
                sc = chex.upper()
            if typ.lower() == "strokethickness":
                thickness = input("Insert thickness > ")
                st = thickness
            if typ.lower() == "fontcolor":
                chex = input("Insert color hex > ")
                fc = chex.upper()
            if typ.lower() == "fontface":
                face = input("Insert font face > ")
                ff = face.capitalize()
print("CODE---------------------------------")
print(code)
print("-------------------------------------")
print("WARN: If code doesnt work, either you did something wrong or the game is bugging.")
input("Press enter to close")
