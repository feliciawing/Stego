# Felicia Angelina - 2301892793
# Referensi https://docs.replit.com/tutorials/13-steganography
import png
import base64

ENDOFMESSAGE = "010101100100010101101000010010100101010100110000011011000101010001010010010101010011100101000111"

def encode_message_as_bytestring(message):
	b64 = message.encode("utf8")
	bytes_ = base64.encodebytes(b64)
	bytestring = "".join(["{:08b}".format(x) for x in bytes_])
	bytestring += ENDOFMESSAGE
	return bytestring

def get_pixels(imgName):
    img = png.Reader(imgName).read()
    pixels = img[2]
    return pixels

def encode_images(pixels, bystring):
    enc_pixels = []
    string_i = 0
    for row in pixels:
        enc_row = []
        for i, char in enumerate(row):
            if string_i >= len(bystring):
                pixel = row[i]
            else:
                if row[i] % 2 != int(bystring[string_i]):
                    if row[i] == 0:
                        pixel = 1
                    else:
                        pixel = row[i] - 1
                else:
                    pixel = row[i]
            enc_row.append(pixel)
            string_i+=1

        enc_pixels.append(enc_row)
    return enc_pixels
    
def newImage(pixels, newImage):
    png.from_array(pixels, 'RGB').save(newImage)

def decode_message(bystring):
    bystring = bystring.split(ENDOFMESSAGE)[0]
    msg = int(bystring, 2).to_bytes(len(bystring) // 8, byteorder='big')
    msg = base64.decodebytes(msg).decode('utf-8')
    return msg

def decode_images(pixels):
    bystring = []
    for row in pixels:
        for i in row:
            bystring.append(str(i%2))
    bystring = ''.join(bystring)
    message = decode_message(bystring)
    print(message)

def enc_imgur():
    Img = 'Img.png'
    Msg = 'secret but not so secret'
    newImg = 'newImg.png'
    print("Encoding in Progress...")
    pixels = get_pixels(Img)
    bystring = encode_message_as_bytestring(Msg)
    encoded = encode_images(pixels, bystring) 
    newImage(encoded, newImg)

def dec_imgur():
    Img = input("Please enter filename: ")
    print("Decoding in Progress...")
    pixels = get_pixels(Img)
    decode_images(pixels)

# kalau mau langsung enc dan dec message pada png
# if __name__ == "__main__":
#     enc_imgur()
#     dec_imgur()