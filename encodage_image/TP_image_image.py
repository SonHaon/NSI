from convert_str_utf8 import str_vers_utf8,utf8_vers_str
from PIL import Image
import time

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


def decodage_message_dans_image(image,image_base):
    image=Image.open(r"C:\Users\noahv\Desktop\NSI\encodage_image\image_dans_image.png")
    a=0
    for hauteur in range(image.height):
        for longueur in range(image.width):
            r,g,b=image.getpixel((longueur,hauteur))
            r=bin(r)[:2]
        a+=1

    message="".join(message).rstrip("0")+"0000000000"
    # print(message)
    message=utf8_vers_str(message)

    image.close()
    image_base.close()
    return message