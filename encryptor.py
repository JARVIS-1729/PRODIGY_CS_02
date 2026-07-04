import argparse
from PIL import Image
import os
import random
def imaenc(mode,image_path,key):
    try:
        img = Image.open(image_path).convert("RGB")
        pixels = bytearray(img.tobytes())

        random.seed(key)

        for i in range(len(pixels)):
            pixels_key = random.randint(0,255)
            pixels[i] = pixels[i] ^ pixels_key
        
        new_img =Image.frombytes("RGB",img.size,bytes(pixels))

        basename = os.path.basename(image_path)
        name , extension = os.path.splitext(basename)

        if mode == "encrypt":
            op_filename = f"encrypted_{name}.png"
        elif mode == "decrypt":
            op_filename = f"decrypted_{name}.jpg"
        
        new_img.save(op_filename)
        print(f"the {mode}ed file saved to the folder with name {op_filename}")
    except FileNotFoundError :
        print(f"{image_path} file doesn't exist")
    except Exception as e:
        print(f"another exception caught {e}")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Image Encryptor Using Pixel Manipulator")

    parser.add_argument("mode" ,choices=["encrypt","decrypt"],help="choose the mode:")
    parser.add_argument("image_path",help="select the name of image you want to encrypt exactly: ")
    parser.add_argument("key",type=int,help="enter a key between 0 and 255:")

    args=parser.parse_args()

    if(0<=args.key<=255):
        imaenc(args.mode,args.image_path,args.key)
    else:
        print("please enter a key which is between 0 and 255: ")