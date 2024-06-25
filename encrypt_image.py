from PIL import Image
def encrypt(image_name, enc):
    image = Image.open(image_name)
    new_image = image.load()

    w, h = image.size
    for i in range(w):
        for j in range(h):
            r, g, b = image.getpixel((i, j))
            new_image[i, j] = (r + enc, g + enc, b + enc)
    image.save("encrypt_"+image_name, format="png")
    print("done")

def decrypt(enc_image, enc):
    dec_image = Image.open(enc_image)
    new_image = dec_image.load()
    w, h = dec_image.size
    for i in range(w):
        for j in range(h):
            r, g, b = dec_image.getpixel((i, j))

            new_image[i, j] = (r - enc, g - enc, b - enc)
    dec_image.save("decrypt_" + enc_image, format="png")
    print("done")
while True:
    print("1. Encryption \n2. Decryption \n\n99. Exit")
    to_do = int(input("Wnat you want to do -: "))

    if to_do == 1:
        image_name = input("Enter the image name -: ")
        encrypt(image_name, 99)

    elif to_do == 2:
        image_name = input("Enter the image name -: ")
        decrypt(image_name, 99)

    elif to_do == 99:
        break

    else:
        print("Wrong Input....")

    print("\n\n")