import qrcode
from PIL import Image

qr = qrcode.QRCode(box_size = '20',
                   version = 1,
                   error_correction = qrcode.constants.ERROR_CORRECT_H,
                   border = '10')

qr.add_data("https://short-url-s.netlify.app")
qr.make(fit=True)

img = qr.make_image(fill_color = 'green',
                    back_color = 'black')

img.save("./shortify.png")
