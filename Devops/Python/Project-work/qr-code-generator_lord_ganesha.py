import qrcode
from PIL import Image

image_url = 'https://tse3.mm.bing.net/th/id/OIP.vrGE-XDv6lBnwY17HCl4UAHaEJ?r=0&cb=thfc1&rs=1&pid=ImgDetMain&o=7&rm=3'
filename = input('Enter the filename: ').strip()
qr = qrcode.QRCode(box_size=10, border=4, error_correction=qrcode.constants.ERROR_CORRECT_H,)
qr.add_data(image_url)
qr.make(fit=True)
image = qr.make_image(fill_color='black', back_color='white').convert('RGB')
image.save(filename)
print(f'QR code has been saved in {filename}')