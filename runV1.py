completed = False
customizing = False
textamount = 0
stroke = ""
font = ""
code = ""
while completed == False:
    print("Type in '>complete' to get your code")
    print("Found text: "+str(textamount))
    text = input("Insert text > ")
    textamount += 1
    customizing = True
    if text.lower() == ">complete":
        completed = True
    else:
        sc = False 
        st = False 
        fc = False 
        ff = False
        while customizing == True:
            print("Type in 'finish' to stop customizing your text")
            print("Supported types: StrokeColor, StrokeThickness, FontColor, FontFace")
            typ = input("Insert type > ")
            if typ.lower() == "finish":
                code += "<stroke "+stroke+"><font "+font+">"+text+"</font></stroke>"
                customizing = False
                stroke = ""
                font = ""
            if typ.lower() == "strokecolor":
                if sc == False:
                    sc = True
                    chex = input("Insert color hex > ")
                    stroke += 'color="'+chex.upper()+'" '
                else:
                    print("WARN: Stroke color was already added!")
            if typ.lower() == "strokethickness":
                if st == False:
                    st = True
                    thickness = input("Insert thickness > ")
                    stroke += 'thickness="'+thickness+'" '
                else:
                    print("WARN: Stroke thickness was already added!")
            if typ.lower() == "fontcolor":
                if fc == False:
                    fc = True
                    chex = input("Insert color hex > ")
                    font += 'color="'+chex.upper()+'" '
                else:
                    print("WARN: Font color was already added!")
            if typ.lower() == "fontface":
                if ff == False:
                    ff = True
                    face = input("Insert font face > ")
                    font += 'face="'+face+'" '
                else:
                    print("WARN: Font face was already added!")
print("CODE---------------------------------")
print(code)
print("-------------------------------------")
print("WARN: If code doesnt work, either you did something wrong or the game is bugging.")
input("Press enter to close")
