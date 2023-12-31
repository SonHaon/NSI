from convert_str_utf8 import str_vers_utf8,utf8_vers_str
from PIL import Image
import time
from pathlib import Path

path = Path(__file__).parent

def split3(message:str):
    message_new=[]
    triple=""
    a=1
    for bit in message:
        triple=triple+bit
        if a==3:
            message_new.append(triple)
            triple=""
            a=1
        else:
            a+=1
    message_new.append(triple)
    
    return message_new


def decodage_image_dans_image(image):
    try:
        image=Image.open(r"E:\image_code\\"+"babouinception.png")
        print("ouvert sur clé")
    except:
        image=Image.open(path / image)
        print("ouvert sur pc")
    new_image=image.copy()
    a=0
    for hauteur in range(image.height):
        for longueur in range(image.width):
            # time.sleep(2)
            r,g,b=image.getpixel((longueur,hauteur))
            # print(bin(r),bin(g),bin(b))
            r="0"*(8-len(bin(r)[2:]))+bin(r)[2:]
            g="0"*(8-len(bin(g)[2:]))+bin(g)[2:]
            b="0"*(8-len(bin(b)[2:]))+bin(b)[2:]
            # print(r,g,b)
            r2=int(r[-3:]+"1000",2)
            g2=int(g[-3:]+"1000",2)
            b2=int(b[-3:]+"1000",2)
            # print(r2,g2,b2)
            new_image.putpixel((longueur,hauteur),(r2,g2,b2))
        a+=1

    image.close()
    new_image.show()
    new_image.close()

def encode_image_dans_image(image):
    image_base=Image.open(path / "babouin.png")
    image=Image.open(path / image).convert("RGB")
    print(image.mode)
    a=0
    for hauteur in range(image_base.height):
        for longueur in range(image_base.width):
            r,g,b=image_base.getpixel((longueur,hauteur))
            # print(r,g,b)
            # print(image.getpixel((longueur,hauteur)))
            r2,g2,b2=image.getpixel((longueur,hauteur))
            r="0"*(8-len(bin(r)[2:]))+bin(r)[2:][:-3]
            g="0"*(8-len(bin(g)[2:]))+bin(g)[2:][:-3]
            b="0"*(8-len(bin(b)[2:]))+bin(b)[2:][:-3]
            # print(int(r+"0000",2),int(g+"0000",2),int(b+"0000",2))
            # print(r,g,b)
            # print(bin(r2),bin(g2),bin(b2))
            r2="0"*(8-len(bin(r2)[2:]))+bin(r2)[2:][:-5]
            g2="0"*(8-len(bin(g2)[2:]))+bin(g2)[2:][:-5]
            b2="0"*(8-len(bin(b2)[2:]))+bin(b2)[2:][:-5]
            # print(r2,g2,b2)
            # print(((r+r2),(g+g2),(b+b2)))
            # print((int(r+r2,2),int(g+g2,2),int(b+b2,2)))
            image_base.putpixel((longueur,hauteur),(int(r+r2,2),int(g+g2,2),int(b+b2,2)))
            r,g,b=image_base.getpixel((longueur,hauteur))
            # print(r,g,b)
            # print(bin(r),bin(g),bin(b))
        a+=1
    try:
        image_base.save(r"E:\image_code\\"+"babouinception.png")
        print("save sur clé")
    except:
        image_base.save(path / "babouinception.png")
        print("save sur pc")

    image_base.close()
    image.close()

encode_image_dans_image("IncepBabouin.png")
# decodage_image_dans_image("matrix_code.png")


decodage_image_dans_image("babouinception.png")