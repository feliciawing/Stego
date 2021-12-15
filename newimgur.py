# Felicia Angelina - 2301892793
# Referensi https://github.com/vprusso/youtube_tutorials/tree/master/imgur_python
from authentication import authenticate
from stegoImg import enc_imgur
import datetime as datetime

imgSource = enc_imgur()

def upload_image(client):
    # uploading the image to imgur
    config = {
        'album': 'GSLC',
        'name': 'GSLC Stego Image',
        'title': 'Stego Image',
        'description': 'testing upload at {0}'.format(datetime.datetime.now())
    }

    print('Uploading image ...')
    image = client.upload_from_path(imgSource, config=config, anon=False)
    print('Image upload completed')

    return image

if __name__ == "__main__":
    client = authenticate()
    image = upload_image(client)
    
    print(f"Image link : {image['link']}")



