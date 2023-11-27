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


def decodage_image_dans_image():
    image=Image.open(r"C:\Users\noahv\Desktop\NSI\encodage_image\babouin.png")
    new_image=image.copy()
    a=0
    for hauteur in range(image.height):
        for longueur in range(image.width):
            r,g,b=image.getpixel((longueur,hauteur))
            r="0"*(8-len(bin(r)[2:]))+bin(r)[2:]
            g="0"*(8-len(bin(g)[2:]))+bin(g)[2:]
            b="0"*(8-len(bin(b)[2:]))+bin(b)[2:]
            r2=int(r[2:],2)
            g2=int(g[2:],2)
            b2=int(b[2:],2)
            new_image.putpixel((longueur,hauteur),(r2,g2,b2))
        a+=1
    try:
        image.save(r"E:\image_code\\"+"babouin_revele.png")
        print("save sur clé")
    except:
        image.save(path / "babouin_revele.png")
        print("save sur pc")

    image.close()
    new_image.show()
    new_image.close()

def encode_image_dans_image(image):
    image_base=Image.open(path / "babouin.png")
    image=Image.open(path / image)
    a=0
    for hauteur in range(image_base.height):
        for longueur in range(image_base.width):
            r,g,b=image_base.getpixel((longueur,hauteur))
            r2,g2,b2=image.getpixel((longueur,hauteur))
            r="0"*(8-len(bin(r)[2:]))+bin(r)[2:][::4]
            g="0"*(8-len(bin(g)[2:]))+bin(g)[2:][::4]
            b="0"*(8-len(bin(b)[2:]))+bin(b)[2:][::4]
            r2="0"*(8-len(bin(r2)[2:]))+bin(r2)[2:][::4]
            g2="0"*(8-len(bin(g2)[2:]))+bin(g2)[2:][::4]
            b2="0"*(8-len(bin(b2)[2:]))+bin(r2)[2:][::4]
            image_base.putpixel((longueur,hauteur),(int(r+r2,2),int(g+g2,2),int(b+b2,2)))
        a+=1
    try:
        image_base.save(r"E:\image_code\\"+"babouin_super_secret.png")
        print("save sur clé")
    except:
        image_base.save(path / "babouin_super_secret.png")
        print("save sur pc")

    image_base.close()
    image.show()
    image.close()


decodage_image_dans_image()