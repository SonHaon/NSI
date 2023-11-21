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



def encodage_message_dans_image(image,message):
    message=split3(str_vers_utf8(message))
    image=Image.open(r"C:\Users\noahv\Desktop\NSI\encodage_image\\"+image)
    hauteur=0
    longueur=0
    for triple_bit in message:
        red,green,blue=image.getpixel((longueur,hauteur))
        try:
            if triple_bit[0]=="1":
                if red!=255:red+=1
                else:red-=1
            if triple_bit[1]=="1":
                if green!=255:green+=1
                else:green-=1
            if triple_bit[2]=="1":
                if blue!=255:blue+=1
                else:blue-=1
        except:pass
        image.putpixel((longueur,hauteur),(red,green,blue))
        if longueur==image.width-1:
            longueur=0
            hauteur+=1
        else:
            longueur+=1
    
    image.save(r"C:\Users\noahv\Desktop\NSI\encodage_image\\"+"babouin_secret.png")

def decodage_message_dans_image(image,image_base):
    image=Image.open(r"E:\image_code\\"+image)
    image_base=Image.open(r"C:\Users\noahv\Desktop\NSI\encodage_image\\"+image_base)
    message=[]
    a=0
    for hauteur in range(image.height):
        for longueur in range(image.width):
            pixel_edit=image.getpixel((longueur,hauteur))
            pixel=image_base.getpixel((longueur,hauteur))
            for i in range(3):
                if pixel_edit[i]==pixel[i]:
                    message.append("0")
                else:
                    message.append("1")
        a+=1
    
    
    message="".join(message).rstrip("0")
    # message=utf8_vers_str(message)

    image.close()
    image_base.close()
    return message

message = "bon mon code marche pas alors je t'envoie ca"
# encodage_message_dans_image("babouin.png",message)
print(decodage_message_dans_image("babouin_secret.png","babouin.png"))