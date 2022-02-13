import qrcode
from PIL import Image

data = str(input("Enter Link or Text :>>\n"))
bsize = int(input("Enter Box Size :\n"))
border_size = int(input("Enetr Border Size :\n"))
qr=qrcode.QRCode(version=10,error_correction=qrcode.constants.ERROR_CORRECT_Q,
                 box_size=bsize,border=border_size)
qr.add_data(data)
qr.make(fit=True)
col = str(input("Enter The Color :\n"))
b_col = str(input("Enter Background Color :\n"))
pic=qr.make_image(fill_color=col,back_color=b_col)
pic.save("Result.png")
print("Saved.>>")
